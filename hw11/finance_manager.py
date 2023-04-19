from transaction.operations import PersonalFinanceManager
from transaction.models import Transaction, TransactionType
from core.util import date_validation, amount_validation
import argparse


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
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
    view_parser.add_argument("--start_date", type=str, help="Start date (YYYY-MM-DD)")
    view_parser.add_argument("--end_date", type=str, help="End date (YYYY-MM-DD)")
    # Report transactions subcommand
    report_parser = subparsers.add_parser(
        "report", help="generate a summary report of transactions between two dates"
    )
    report_parser.add_argument("--start_date", type=str, help="Start date (YYYY-MM-DD)")
    report_parser.add_argument("--end_date", type=str, help="End date (YYYY-MM-DD)")
    return parser.parse_args()


args = parse_args()


def main() -> None:
    """Main function."""
    args = parse_args()
    if (
        args.command == "add"
    ):  # TODO rasis error if not ok and make it lowercase for check and all inputes are entered
        # TODO validation on getting type

        date_validation(args.date)
        amount_validation(args.amount)
        transaction = Transaction(
            args.type, args.amount, args.date, args.category, args.description
        )
        PersonalFinanceManager.add_transaction(transaction)
        print("Transaction added successfully..")

    elif args.command == "view":  # check dates are valedate
        date_validation(args.start_date)
        date_validation(args.end_date)
        PersonalFinanceManager.view_transactions_between_two_dates(
            args.start_date, args.end_date
        )

    elif args.command == "report":  # check dates are valedate
        date_validation(args.start_date)
        date_validation(args.end_date)
        PersonalFinanceManager.view_summary_report_between_two_dates(
            args.start_date, args.end_date
        )


"""Run project just from here"""
if __name__ == "__main__":
    main()
