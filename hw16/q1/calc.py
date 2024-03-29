from fastapi import FastAPI, HTTPException
from functools import reduce
from typing import Optional

app = FastAPI()
i = 5
operations = [
    {
        "id": 1,
        "numbers": [
            1,
            2,
            3,
            4,
        ],
        "operation_type": "add",
        "result": 10,
    },
    {
        "id": 2,
        "numbers": {"minuend": 10, "subtrahend": 5},
        "operation_type": "subtract",
        "result": 5,
    },
    {"id": 3, "numbers": [1, 2, 3], "operation_type": "multiply", "result": 6},
    {
        "id": 4,
        "numbers": {"dividend": 10, "divisor": 5},
        "operation_type": "divide",
        "result": 2,
    },
]


@app.post("/calculate/add")
def add(numbers: dict):
    global i
    result = sum(numbers["numbers"])
    operations.append(
        {
            "id": i,
            "numbers": numbers["numbers"],
            "operation_type": "add",
            "result": result,
        }
    )
    print(
        {
            "id": i,
            "numbers": numbers["numbers"],
            "operation_type": "add",
            "result": result,
        }
    )
    i += 1
    return result


@app.post("/calculate/subtract")
def subtract(numbers: dict):
    global i

    result = numbers["minuend"] - numbers["subtrahend"]
    operations.append(
        {
            "id": i,
            "numbers": numbers,
            "operation_type": "subtract",
            "result": result,
        }
    )
    i += 1
    return result


@app.post("/calculate/multiply")
def multiply(numbers: dict):
    global i

    result = reduce(lambda x, y: x * y, numbers["factors"])
    operations.append(
        {
            "id": i,
            "numbers": numbers["factors"],
            "operation_type": "multiply",
            "result": result,
        }
    )
    i += 1
    return result


@app.post("/calculate/divide")
def divide(numbers: dict):
    global i

    if numbers["divisor"] == 0:
        raise HTTPException(status_code=400, detail="Divisor cannot be zero")
    result = numbers["dividend"] / numbers["divisor"]
    operations.append(
        {
            "id": i,
            "numbers": numbers,
            "operation_type": "divide",
            "result": result,
        }
    )
    i += 1
    return result


@app.get("/calculate/history")
def operation_history(limit: Optional[int] = None, operator: Optional[str] = None):
    valid_operators = ("add", "subtract", "multiply", "divide")
    if operator and operator not in valid_operators:
        raise HTTPException(status_code=400, detail="Invalid operator")
    if operator and limit:
        output = list(
            filter(
                lambda op: op["operation_type"] == operator,
                operations,
            )
        )
        return output[-limit:]
    elif not operator:
        return operations[:limit]
    else:
        return operations


@app.get("/calculate/history/{history_id}")
def find_history_by_id(history_id: int):
    output = list(
        filter(
            lambda op: op["id"] == history_id,
            operations,
        )
    )
    if output:
        return output[0]
