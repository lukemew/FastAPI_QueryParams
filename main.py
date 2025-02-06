from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import Response

app = FastAPI()

class Country(BaseModel):
    country_name: str
    capital: str
    population: int
    continent: str

countries_db = [
    {"country_name": "Brazil", "capital": "Brasília", "population": 213000000, "continent": "South America"},
    {"country_name": "Argentina", "capital": "Buenos Aires", "population": 45195777, "continent": "South America"},
    {"country_name": "Japan", "capital": "Tokyo", "population": 125800000, "continent": "Asia"},
    {"country_name": "Germany", "capital": "Berlin", "population": 83200000, "continent": "Europe"},
]

@app.get("/country/{country_name}", response_model=Country)
def get_country(country_name: str):
    country = next((c for c in countries_db if c["country_name"].lower() == country_name.lower()), None)
    if country:
        return country
    raise HTTPException(status_code=404, detail="País não encontrado")

@app.get("/countries/", response_model=List[Country])
def get_countries(continent: Optional[str] = Query(None, description="Filtrar países por continente")):
    if continent:
        filtered_countries = [c for c in countries_db if c["continent"].lower() == continent.lower()]
        return filtered_countries
    return countries_db

@app.post("/country/{country_name}", response_model=dict)
def add_country(country_name: str, country: Country):
    if any(c["country_name"].lower() == country_name.lower() for c in countries_db):
        raise HTTPException(status_code=400, detail="País já existe")
    
    new_country = country.dict()
    new_country["country_name"] = country_name
    countries_db.append(new_country)
    
    return {"message": "País adicionado com sucesso!", "country_name": country_name}

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de países! Use /country/{nome_do_país} ou /countries/ para começar."}

@app.get("/favicon.ico", include_in_schema=False)
def get_favicon():
    return Response(status_code=204)