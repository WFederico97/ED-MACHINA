def test_create_persona(client):
    response = client.post("/personas/register", json={
        "nombre_persona": "Nicolas",
        "apellido_persona": "Tzar",
        "email_persona": "anti.bolcheviks@example.com",
        "active": True,
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nombre_persona"] == "Nicolas"
    assert data["apellido_persona"] == "Tzar"

def test_get_persona(client):
    response = client.get("/personas/1")
    assert response.status_code == 200
    data = response.json()
    assert data["nombre_persona"] == "Nicolas"
    assert data["apellido_persona"] == "Tzar"

def test_update_persona(client):
    response = client.put("/personas/update/1", json={
        "nombre_persona": None,
        "apellido_persona": None,
        "email_persona": "anti.bolcheviks@russi.com",
        "active": True,
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email_persona"] == "anti.bolcheviks@russi.com"

def test_delete_persona(client):
    response = client.put("/personas/update/2", json={
        "active": True,
    })
    assert response.status_code == 200
    data = response.json()
    assert data["active"] == True