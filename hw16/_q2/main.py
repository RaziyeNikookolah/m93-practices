from fastapi import FastAPI, HTTPException, Request, status, Form
from fastapi.responses import RedirectResponse

from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


app = FastAPI()

template = Jinja2Templates(directory="templates")


class Person(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str


persons_dict_list = [
    {
        "id": 1,
        "first_name": "ali",
        "last_name": "rezayi",
        "email": "r@gmail.com",
        "phone_number": "123456789",
    },
    {
        "id": 2,
        "first_name": "zahra",
        "last_name": "zahrayi",
        "email": "z@gmail.com",
        "phone_number": "123456789",
    },
    {
        "id": 3,
        "first_name": "akbar",
        "last_name": "akbari",
        "email": "a@gmail.com",
        "phone_number": "123456789",
    },
    {
        "id": 4,
        "first_name": "maryam",
        "last_name": "maryami",
        "email": "m@gmail.com",
        "phone_number": "123456789",
    },
    {
        "id": 5,
        "first_name": "ahmad",
        "last_name": "ahmadi",
        "email": "h@gmail.com",
        "phone_number": "123456789",
    },
    {
        "id": 6,
        "first_name": "sara",
        "last_name": "sarii",
        "email": "s@gmail.com",
        "phone_number": "123456789",
    },
]


person_instance_list = list(
    map(
        lambda x: Person(
            id=x["id"],
            first_name=x["first_name"],
            last_name=x["last_name"],
            email=x["email"],
            phone_number=x["phone_number"],
        ),
        persons_dict_list,
    )
)


@app.get("/home", response_class=HTMLResponse)
def read_persons(request: Request):
    return template.TemplateResponse(
        "index.html",
        {"request": request, "persons": person_instance_list, "person": None},
    )


@app.post("/update/{id}}", response_class=HTMLResponse)
def update(
    request: Request,
    id: int,
    name: str = Form(...),
    lastname: str = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
):
    # Find the person to update
    person = next((p for p in persons_dict_list if p["id"] == id), None)
    if person:
        # Update the person's data
        person["first_name"] = name
        person["last_name"] = lastname
        person["email"] = email
        person["phone_number"] = phone_number
        return RedirectResponse("/home")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Person not found"
        )


@app.get("/edit/{id}", response_class=HTMLResponse)
async def edit(request: Request, id: int):
    person = list((p for p in persons_dict_list if p["id"] == id))
    if person[0]:
        return template.TemplateResponse(
            "index.html",
            {"request": request, "persons": person_instance_list, "person": person[0]},
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Person not found"
        )


@app.post("/add")
async def add(
    request: Request,
    id: int = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    phone_number: str = Form(...),
    email: str = Form(...),
):
    print(first_name)
    print(last_name)
    print(phone_number)
    print(email)
    person = Person(
        id=id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
    )
    person_instance_list.append(person)
    persons_dict_list.append(
        {
            "id": id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
        }
    )

    return RedirectResponse("/home")


# The Form(...) annotation indicates that these parameters should be extracted from the form data.
# The ... within Form(...) is a placeholder that indicates that the parameter is
# required and must be provided in the form data. It acts as a form of validation
# to ensure that the required data is present. If the required parameter is not provided
# in the form data, FastAPI will return a validation error.
