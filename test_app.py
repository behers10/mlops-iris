from fastapi.testclient import TestClient
from main import app
print('i ma here')
# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3,
        "sepal_width": 5,
        "petal_length": 3.2,
        "petal_width": 4.4,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Virginica","timestamp":"2021-07-10 23:33:16"}

# New Test Cases  1       
def test_pred_versicolor():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 5.84 ,
        "sepal_width": 3.05 ,
        "petal_length": 3.76 ,
        "petal_width": 1.20 ,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Versicolor","timestamp":"2021-07-10 23:33:16"}


# New Test Cases  2       
def test_pred_versicolor():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 5.84 ,
        "sepal_width": 3.05 ,
        "petal_length": 3.76 ,
        "petal_width": 1.20 ,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert 'timestamp' in str(response.json())