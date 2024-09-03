def test_create_carrera(client):
    response = client.post("/carreras/register", json={
        "nombre_carrera": "Medicina",
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nombre_carrera"] == "Medicina"

def test_get_carrera(client):
    response = client.get("/carreras/1")
    assert response.status_code == 200
    data = response.json()
    assert data["nombre_carrera"] == "Ingeniería en Sistemas"