from fastapi import FastAPI, status, HTTPException, Query, Path
import uvicorn
from typing import Annotated
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client['transaction']

transaction_collection = db['transaction']

collections_in_db = db.list_collection_names()

transaction_user_day_collection = db['transaction_user_day_collection']
if transaction_user_day_collection.find_one() is None:
    pipeline = [
        {
            "$group": {
                "_id": {
                    "merchantId": {"$toString": "$merchantId"},
                    "createdAt": {
                        "$dateToString": {
                            "format": "%Y-%m-%d",
                            "date": "$createdAt"
                        }
                    }
                },
                "totalAmount": {"$sum": "$amount"},
                "transactions_count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "_id.createdAt": 1
            }
        }
    ]

    result = db.transaction.aggregate(pipeline)
    transaction_user_day_collection.insert_many(result)

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get(
    "/search"
)
def search_transaction(
        time_period: Annotated[str, Query(..., enum=["week", "day", "month", "year"])],
        amount_or_count: Annotated[str, Query(..., enum=["amount", "count"])],
        tomans_or_rials: Annotated[str, Query(..., enum=["rials", "tomans"])],
        date_from: str,  # Annotated[str, Path(...)],
        date_to: str,
        merchant_id: str = None
):
    match_query = {}
    group_query = {}
    total_value = ""
# merchant id categorizing
    if merchant_id:
        match_query = {"$and": [{
            "_id.createdAt": {"$gte": f'{date_from}', "$lt": f'{date_to}'}}, {"_id.merchantId": f'{merchant_id}'}]}
    else:
        match_query = {
            "_id.createdAt": {"$gte": f'{date_from}', "$lt": f'{date_to}'}}


# count or amount categorizing
    if amount_or_count == "amount":
        total_value = "totalAmount"
    else:
        total_value = "transactions_count"


# Time period categoring
    if time_period == "year":
        group_query = {"_id": {
            "$substr": [
                "$_id.createdAt",
                0,
                4
            ]
        },
            f"{total_value}": {"$sum": f"${total_value}"}
        }
    elif time_period == "month":
        group_query = {"_id": {
            "$substr": [
                "$_id.createdAt",
                0,
                7
            ]
        },
            f"{total_value}": {"$sum": f"${total_value}"}
        }
    elif time_period == "day":
        group_query = {"_id": {
            "$substr": [
                "$_id.createdAt",
                0,
                9
            ]
        },
            f"{total_value}": {"$sum": f"${total_value}"}
        }
    elif time_period == "week":
        group_query = {
            "_id": {
                "year": {"$year": {"$toDate": "$_id.createdAt"}},
                "week": {"$isoWeek": {"$toDate": "$_id.createdAt"}}
            },
            f"{total_value}": {"$sum": f"${total_value}"}
        }

    docs = list(transaction_user_day_collection.aggregate(
        [{'$match': match_query},
         {'$group': group_query}
         ]))

    return docs


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True, host="127.0.0.1")
