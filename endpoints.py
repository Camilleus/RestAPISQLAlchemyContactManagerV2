from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()


templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login")
def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
def login_user(request: Request):
    return {"message": "Logowanie udane"}


@app.get("/register")
def read_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
def register_user(request: Request):
    return {"message": "Rejestracja udana"}


@app.get("/contacts")
def read_contacts(request: Request):
    return templates.TemplateResponse("contacts.html", {"request": request})

