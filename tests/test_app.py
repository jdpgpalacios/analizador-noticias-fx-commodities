from src.app import app


def test_pagina_principal():
    cliente = app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200


def test_eco_repite_el_texto():
    cliente = app.test_client()
    respuesta = cliente.post("/echo_user_input", data={"user_input": "hola"})
    assert b"hola" in respuesta.data