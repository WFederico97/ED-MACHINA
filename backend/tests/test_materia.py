def test_create_materia(client):
    response = client.post("/materias/register", json={
        "nombre_materia": "Semiologia",
        "cod_carrera": 1,
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nombre_materia"] == "Semiologia"
    assert data["cod_carrera"] == 1

def test_get_materia(client):
    response = client.get("/materias/1")
    assert response.status_code == 200
    data = response.json()
    assert data["nombre_materia"] == "DSI"
    assert data["cod_materia"] == 1