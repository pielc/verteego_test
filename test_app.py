from app import app
from flask import Flask

def test_api_should_work():
  response = app.test_client().post(
    "/usecase",
    json={'usecase': "id"}
  )
  assert response.status_code == 200
  assert response.json['usecase'] == "id"
  assert response.json['param1'] == "value1"
  
def test_no_parameters_api_should_return_405():
  response = app.test_client().post()
  assert response.status_code == 405
  
def test_should_parameters_api_should_return_400():
  response = app.test_client().post(
    "/usecase",
    json={'wrongParam': "id"}
  )
  assert response.status_code == 400

def test_get_api_should_return_405():
  response = app.test_client().get(
    "/usecase",
    json={'usecase': "id"}
  )
  assert response.status_code == 405