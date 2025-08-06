import requests
import pytest
@pytest.mark.duckduckgo
@pytest.mark.api


def test_duckduckgo_istant_answer_api():
    #arrange
    url = "https://api.duckduckgo.com/?q=python+programming&format=json"
    #Act
    response = requests.get(url)
    body = response.json()
    #Assert
    assert response.status_code == 200
    assert "Python" in body["AbstractText"]
