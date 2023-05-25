from fastapi import FastAPI, HTTPException
from functools import reduce
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()
i = 5
operations = [
    {
        "id": 1,
        "numbers": [1, 2, 3, 4],
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


class AddRequest(BaseModel):
    numbers: List[int]


class SubtractRequest(BaseModel):
    minuend: int
    subtrahend: int


class MultiplyRequest(BaseModel):
    factors: List[int]


class DivideRequest(BaseModel):
    dividend: int
    divisor: int


@app.post("/calculate/add")
def add(request: AddRequest):
    global i
    global operations
    result = sum(request.numbers)
    operations.append(
        {
            "id": i,
            "numbers": request.numbers,
            "operation_type": "add",
            "result": result,
        }
    )
    i += 1

    return result


@app.post("/calculate/subtract")
def subtract(request: SubtractRequest):
    global i
    global operations
    result = request.minuend - request.subtrahend
    operations.append(
        {
            "id": i,
            "numbers": {"minuend": request.minuend, "subtrahend": request.subtrahend},
            "operation_type": "subtract",
            "result": result,
        }
    )
    i += 1
    return result


@app.post("/calculate/multiply")
def multiply(request: MultiplyRequest):
    global i
    global operatins
    result = reduce(lambda x, y: x * y, request.factors)
    operations.append(
        {
            "id": i,
            "numbers": request.factors,
            "operation_type": "multiply",
            "result": result,
        }
    )
    i += 1
    print(operations)
    return result


@app.post("/calculate/divide")
def divide(request: DivideRequest):
    global i
    global operations
    if request.divisor == 0:
        raise HTTPException(status_code=400, detail="Divisor cannot be zero")
    result = request.dividend / request.divisor
    operations.append(
        {
            "id": i,
            "numbers": {"dividend": request.dividend, "divisor": request.divisor},
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
    if limit and limit <= 0:
        raise HTTPException(status_code=400, detail="Invalid limit")
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
        output = list(
            filter(
                lambda op: op["operation_type"] == operator,
                operations,
            )
        )
        return output


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
