from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db import init_db


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


init_db()


from api import ContactCreateUpdate, ContactResponse, Contact, create_contact, get_all_contacts, get_contact, update_contact, delete_contact, get_birthdays_within_7_days


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
