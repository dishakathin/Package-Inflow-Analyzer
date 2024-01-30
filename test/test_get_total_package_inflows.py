from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# to check rest api get call
def test_get_total_package_inflows():
    response = client.get("/?acme=aa")
    assert response.status_code == 200
    assert response.json() == {"total_package_inflows": [1]}

# to check 400 error status code
def test_get_total_package_inflows():
    response = client.get("/?acme=a2")
    assert response.status_code == 400
    assert response.json() == {"detail": "contains an invalid character"}

# to check 400 error status code
def test_get_total_package_inflows():
    response = client.get("/?acme=aaba")
    assert response.status_code == 400
    assert response.json() == {"detail": "contains a package with fewer characters than specified by package-size"}