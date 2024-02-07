# RestAPISQLalchemyContactsManager

tutaj działa, używam tutaj MySQL i XAMPP'a

## Instalacja

1. Sklonuj repozytorium: `git clone https://github.com/Camilleus/RestAPISQLalchemyContactsManagerV2.git`
2. Przejdź do folderu projektu: `cd RestAPISQLalchemyContactsManagerV2`
3. Zainstaluj zależności: `poetry install`
4. Uruchom serwer: `uvicorn main:app --host localhost --port 8000 --reload`

## Requirements

Wszystko ( a przynajmniej większość) w pliku requirements.txt

## Przyszłe Rozszerzenia

Powstanie jeszcze wersja V3 i V4 na potrzeby ukończenia kursu

## Kontrybucje

Nie potrzebuję ale spoko jeśli takie sie ukażą

## Struktura Projektu

```
RestAPISQLAlchemyContactManagerV2
├─ .gitattributes
├─ api
│  ├─ apis.py
│  ├─ config.py
│  ├─ routes.py
│  └─ __init__.py
├─ auth
│  ├─ auths.py
│  ├─ jwts.py
│  └─ __init__.py
├─ db
│  ├─ contacts.db
│  ├─ data_faker.py
│  ├─ data_for_db.sql
│  ├─ data_sender.py
│  ├─ dbs.py
│  └─ __init__.py
├─ main.py
├─ models.py
├─ poetry.lock
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ static
│  └─ styles.css
├─ templates
│  ├─ base.html
│  ├─ contacts.html
│  ├─ index.html
│  ├─ login,html
│  ├─ register.html
│  └─ verify.html
└─ __init__.py
```
