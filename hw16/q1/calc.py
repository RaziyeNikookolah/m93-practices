from fastapi import FastAPI

app = FastAPI()


@app.post("/calculate/add")
def add(numbers: dict):
    return sum(numbers["numbers"])


@app.post("/calculate/subtract")
def subtract(numbers: dict):
    return numbers["minuend"] - numbers["subtrahend"]
