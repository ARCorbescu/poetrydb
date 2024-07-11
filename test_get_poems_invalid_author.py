import requests
import pytest

BASE_URL = "https://poetrydb.org"

@pytest.mark.parametrize("invalid_author", [
    ("Alexandru-Robert Corbescu"),
    ("Tom Burke"),
])
def test_get_poems_by_invalid_author(invalid_author):
    """
    Test the /author endpoint of the PoetryDB API using invalid values for the author.

    Steps:
    1. Send a GET request to the /author endpoint using invalid values for the author.
    2. Verify the response status code is 405.
    3. Verify the response gives a reson for 405

    Expected Result:
    The API should return a 405 with an appropriate error message.
    """
    # Step 1: Send a GET request to the /author,title endpoint
    response = requests.get(f"{BASE_URL}/author{invalid_author}").json()

    # Step 2: Verify the response status code 405
    err_msg = f"Expected status code 405"
    assert response['status'] == '405', err_msg

    # Step 3: Verify the response contains an appropriate error message
    err_msg = "Expected response to be a list"
    assert invalid_author + " list not available" in response['reason'], err_msg

if __name__ == "__main__":
    pytest.main()
