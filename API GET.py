import requests

# URL for testing (example with JSONPlaceholder)
api_url = "https://jsonplaceholder.typicode.com/posts/1"


# Test scenario for a GET request to the API
def test_api_get_request():
    response = requests.get(api_url)

    # Check for a successful status code (200 OK)
    assert response.status_code == 200

    # Check the content type (JSON in this case)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # Check the presence of a specific field in the JSON response
    json_data = response.json()
    assert "userId" in json_data

    # Check the value of a specific field
    assert json_data["userId"] == 1


# Run the test
test_api_get_request()
print("API GET request test has passed successfully.")