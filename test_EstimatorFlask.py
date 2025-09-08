from EstimatorFlask import app
import json
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    # sample input
    payload = {
        "Age": 35,
        "BMI": 26.5,
        "NumberOfMajorSurgeries": 1,
        "Diabetes": 0,
        "BloodPressureProblems": 1,
        "AnyTransplants": 0,
        "AnyChronicDiseases": 1,
        "KnownAllergies": 0,
        "HistoryOfCancerInFamily": 0
    }

    response = client.post(
        "/predict",
        data=json.dumps(payload),
        content_type="application/json"
    )

    # Check HTTP response
    assert response.status_code == 200

    # Convert response to dict
    data = response.get_json()

    # Ensure the response contains estimated_premium
    assert "estimated_premium" in data
    assert isinstance(data["estimated_premium"], float)