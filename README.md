# RestAPISQLalchemyContactsManager

tutaj działa, używam tutaj MySQL i XAMPP'a

## Instalacja

1. Sklonuj repozytorium: `git clone https://github.com/Camilleus/RestAPISQLalchemyContactsManagerV2.git`
2. Przejdź do folderu projektu: `cd RestAPISQLalchemyContactsManagerV2`
3. Zainstaluj zależności: `poetry install`
4. Uruchom serwer: `poetry run python main.py`

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
│  ├─ api.py
│  ├─ config.py
│  ├─ models.py
│  └─ routes.py
├─ auth
│  ├─ auth.py
│  └─ jwt_utils.py
├─ db
│  ├─ contacts.db
│  ├─ data_faker.py
│  ├─ data_for_db.sql
│  ├─ data_sender.py
│  └─ db.py
├─ main.py
├─ poetry.lock
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ static
│  └─ styles.css
├─ templates
│  ├─ base.html
│  └─ index.html
└─ __init__.py
```
