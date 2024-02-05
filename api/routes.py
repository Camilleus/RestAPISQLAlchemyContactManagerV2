from fastapi import APIRouter, Depends, Request
from auth.auths import refresh_access_token
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.dbs import init_db
from models import Token
from api.apis import ContactCreateUpdate, ContactResponse, Contact, create_contact, get_all_contacts, get_contact, update_contact, delete_contact, get_birthdays_within_7_days


router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, world!"})


@router.post("/refresh-token/", response_model=Token)
async def refresh_token(current_token: str = Depends(refresh_access_token)):
    return current_token