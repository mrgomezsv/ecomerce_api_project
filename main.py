# main.py

import os
from fastapi import FastAPI
from productos import productos  # Importa la lista de productos
from contacts import contacts

app = FastAPI()

# Ruta que devuelve la lista de productos
@app.get("/productos")
def read_productos():
    return {"productos": productos}

# Ruta que devuelve la lista de contactos
@app.get("/contacts")
def read_contacts():
    return {"contacts": contacts}

# Ruta que devuelve un JSON con el saludo "Hola Mario"
@app.get("/")
def read_root():
    return {"message": "Hola Mario"}
