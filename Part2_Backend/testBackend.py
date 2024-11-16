import requests


def test_get_root():
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a web map application"}


def test_get_cities():
    response = requests.get("http://localhost:8000/cities")
    assert response.status_code == 200
    data = response.json()
    if data:
        assert isinstance(data, list)
        print(data)


if __name__ == "__main__":
    test_get_root()
    test_get_cities()
    print("All tests passed!")
