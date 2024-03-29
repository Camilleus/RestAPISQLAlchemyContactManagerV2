from fastapi import FastAPI, HTTPException, Query, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import date, timedelta
from models import Contact, User, Token
from db.dbs import get_db, database
from pydantic import BaseModel
from typing import List
from auth.auths import get_current_active_user, login_for_access_token
from auth.jwts import create_jwt_token, decode_jwt_token


app = FastAPI()


router = APIRouter()


class ContactCreateUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str = None
    
    
class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str = None


# CRUD operations
@router.post("/contacts/", response_model=ContactResponse)
async def create_contact(contact: ContactCreateUpdate, current_user: User = Depends(get_current_active_user)):
    query = Contact.__table__.insert().values(**contact.dict())
    contact_id = await database.execute(query)
    return {"id": contact_id, **contact.dict()}


@router.get("/contacts/", response_model=List[ContactResponse])
def get_all_contacts(
    q: str = Query(None, alias="search", description="Search contacts by first name, last name, or email"),
    db: Session = Depends(get_db)
):
    if q:
        contacts = db.query(Contact).filter(
            Contact.first_name.ilike(f"%{q}%")
            | Contact.last_name.ilike(f"%{q}%")
            | Contact.email.ilike(f"%{q}%")
        ).all()
    else:
        contacts = db.query(Contact).all()
    return contacts


@router.get("/contacts/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.put("/contacts/{contact_id}", response_model=ContactResponse)
def update_contact(contact_id: int, contact: ContactCreateUpdate, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    for key, value in contact.dict().items():
        setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.delete("/contacts/{contact_id}", response_model=ContactResponse)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return contact


@router.get("/contacts/birthdays/", response_model=list[ContactResponse])
def get_birthdays_within_7_days(db: Session = Depends(get_db)):
    today = date.today()
    next_week = today + timedelta(days=7)

    contacts = db.query(Contact).filter(
        Contact.birth_date.between(today, next_week)
    ).all()

    return contacts


@router.post("/token/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordBearer = Depends()):
    return login_for_access_token(form_data)


app = FastAPI()
app.include_router(router)