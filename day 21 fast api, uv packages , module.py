from calculate.calculator import Calculator
calc = Calculator()
a = float(input("enter first number: "))
b = float(input("enter second number: "))
result = calc.add(a, b)
print("The result of addition is:", result)


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    return {"item_id": item_id, "updated_name": name}

@app.patch("/items/{item_id}")
def partial_update_item(item_id: int, description: str = None):
    return {"item_id": item_id, "updated_description": description}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a request body model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# GET endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax,
    }
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a request body model for POST
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# GET endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax,
    }

# PUT endpoint
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_item": item}

# PATCH endpoint
@app.patch("/items/{item_id}")
def partial_update_item(item_id: int, description: str | None = None):
    return {"item_id": item_id, "updated_description": description}

@app.post("/calculate/")
def calculate(a: float, b: float):
    result = calc.add(a, b)
    return {"result": result}       
