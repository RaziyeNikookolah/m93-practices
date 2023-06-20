from fastapi import FastAPI, status, HTTPException, Query, Path
import uvicorn
from pydantic import BaseModel
from enum import Enum
from datetime import date, datetime
from typing import Annotated
from pymongo import MongoClient
from bson.objectid import ObjectId

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
                "count": {"$sum": 1}
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
        search_item: Annotated[str, Query(..., enum=["week", "day", "month", "year"])],
        amount_or_count: Annotated[str, Query(..., enum=["amount", "count"])],
        tomans_or_rials: Annotated[str, Query(..., enum=["rials", "tomans"])],
        date_from: str,  # Annotated[str, Path(...)],
        date_to: str,
        merchant_id: str = None
):

    if merchant_id:
        query = {"$and": [{
            "_id.createdAt": {"$gte": f'{date_from}', "$lt": f'{date_to}'}}, {"_id.merchantId": f'{merchant_id}'}]}
    else:
        query = {
            "_id.createdAt": {"$gte": f'{date_from}', "$lt": f'{date_to}'}}

    docs = list(transaction_user_day_collection.find(query))

    return docs


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True, host="127.0.0.1")

# def get_transactions():
#     transactions = list(transaction_collection.find())
#     for trnsc in transactions:
#         trnsc["_id"] = str(trnsc["_id"])
#         trnsc["merchantId"] = str(trnsc["merchantId"])

#     return transactions


# def search(type: TimePeriod, day: datetime, input: str):
#     docs = list(transaction_collection.find({f'{type}': input}))
#     for trnsc in docs:
#         trnsc["_id"] = str(trnsc["_id"])
#         trnsc["merchantId"] = str(trnsc["merchantId"])
#     return docs


# def get_by_id(id: str):
#     trnsc = transaction_collection.find_one({"_id": ObjectId(id)})
#     trnsc["_id"] = str(trnsc["_id"])
#     trnsc["merchantId"] = str(trnsc["merchantId"])
#     return trnsc


# def get_by_merchant_id(id: str):
#     trnscs = list(transaction_collection.find({"merchantId": ObjectId(id)}))
#     for trnsc in trnscs:
#         trnsc["_id"] = str(trnsc["_id"])
#         trnsc["merchantId"] = str(trnsc["merchantId"])

#     return trnscs


# class TransactionInDB(BaseModel):
#     class Config:
#         arbitrary_types_allowed = True
#     _id: ObjectId
#     merchantId: ObjectId
#     amount: int
#     createdAt: datetime


# @app.get(
#     "/{trnsc_id}"  # , response_model=TransactionInDB
# )
# def get_transaction_by_transc_id(id: str):
#     # transc = TransactionInDB(**get_by_id(id))
#     transc = get_by_merchant_id(id)
#     if not transc:
#         raise HTTPException(status.HTTP_404_NOT_FOUND)
#     return transc


# @app.get(
#     "/{merchant_id}"  # , response_model=TransactionInDB
# )
# def get_transaction_by_merchant_id(id: str):
#     # transc = TransactionInDB(**get_by_id(id))
#     transc = get_by_merchant_id(id)
#     if not transc:
#         raise HTTPException(status.HTTP_404_NOT_FOUND)
#     return transc
