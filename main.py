from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.dbs import init_db
from api.routes import router


app = FastAPI()


app.include_router(router)


app.mount("/static", StaticFiles(directory="static"), name="static")


init_db()


from api.apis import ContactCreateUpdate, ContactResponse, Contact, create_contact, get_all_contacts, get_contact, update_contact, delete_contact, get_birthdays_within_7_days


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


