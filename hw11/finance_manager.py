"""
This module provides a Personal Finance Manager that allows users to add transactions, view transactions
between two dates, and generate a summary report of transactions between two dates.

The module provides a command-line interface that can be used by running the script.

This module uses the argparse module to parse command-line arguments and the PersonalFinanceManager,
Transaction, and TransactionType classes from the transaction package.

This module also uses the date_validation and amount_validation functions from the core.util module
to validate the date and amount arguments.

This module raises InvalidCommandException if an invalid command is provided.

This module requires Python 3.x to run.

Usage:
    python personal_finance_manager.py add --type TYPE --date DATE --amount AMOUNT --category CATEGORY [--description DESCRIPTION]
    python personal_finance_manager.py view [--start_date START_DATE] [--end_date END_DATE]
    python personal_finance_manager.py report [--start_date START_DATE] [--end_date END_DATE]

"""

from transaction.operations import PersonalFinanceManager
from transaction.models import Transaction, TransactionType
from core.util import date_validation, amount_validation
from core.exceptions import InvalidCommandException
import argparse


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Namespace object containing the parsed arguments.

    """
    parser = argparse.ArgumentParser(description="Personal finance manager")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add transaction subcommand
    add_parser = subparsers.add_parser("add", help="Add a new transaction")
    add_parser.add_argument(
        "--type",
        type=TransactionType,
        choices=list(TransactionType),
        required=True,
        help="Transaction type (income or expence)",
    )
    add_parser.add_argument(
        "--date", type=str, required=True, help="Transaction date (YYYY-MM-DD)"
    )
    add_parser.add_argument(
        "--amount", type=str, required=True, help="Transaction amount"
    )
    add_parser.add_argument(
        "--category", type=str, required=True, help="Transaction category"
    )
    add_parser.add_argument("--description", type=str, help="Transaction description")

    # View transactions subcommand
    view_parser = subparsers.add_parser(
        "view", help="View transactions between two dates"
    )
    view_parser.add_argument(
        "--start_date", type=str, help="Start date (YYYY-MM-DD)", required=True
    )
    view_parser.add_argument(
        "--end_date", type=str, help="End date (YYYY-MM-DD)", required=True
    )
    # Report transactions subcommand
    report_parser = subparsers.add_parser(
        "report", help="generate a summary report of transactions between two dates"
    )
    report_parser.add_argument(
        "--start_date", type=str, help="Start date (YYYY-MM-DD)", required=True
    )
    report_parser.add_argument(
        "--end_date", type=str, help="End date (YYYY-MM-DD)", required=True
    )
    return parser.parse_args()


args = parse_args()


def main() -> None:
    """
    Main function that handles the command-line arguments and executes the corresponding action.

    Raises:
        InvalidCommandException: If an invalid command is provided.

    """
    args = parse_args()
    if args.command == "add":
        date_validation(args.date)
        amount_validation(args.amount)
        transaction = Transaction(
            args.type, args.amount, args.date, args.category, args.description
        )
        PersonalFinanceManager.add_transaction(transaction)
        print("Transaction added successfully..")

    elif args.command == "view":
        date_validation(args.start_date)
        date_validation(args.end_date)
        PersonalFinanceManager.view_transactions_between_two_dates(
            args.start_date, args.end_date
        )

    elif args.command == "report":
        date_validation(args.start_date)
        date_validation(args.end_date)
        PersonalFinanceManager.view_summary_report_between_two_dates(
            args.start_date, args.end_date
        )
    else:
        raise InvalidCommandException()


"""Run project just from here"""
if __name__ == "__main__":
    main()
