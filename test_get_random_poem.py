import requests
import pytest

BASE_URL = "https://poetrydb.org"

def test_get_random_poem():
    """
    Test the /random endpoint of the PoetryDB API.

    Steps:
    1. Send a GET request to the /random endpoint to retrieve a random poem.
    2. Verify the response status code is 200 (OK).
    3. Verify the response is a list containing one poem.
    4. Verify the poem contains the required fields: 'title', 'author', and 'lines'.
    5. Retry up to 3 times to get a different random poem and ensure it differs from the first one.

    Expected Result:
    The API should return a single poem in a list format, containing the fields 'title', 'author', and 'lines'.
    On retries, the API should return a different poem.
    """
    # Step 1: Send a GET request to the /random endpoint
    response = requests.get(f"{BASE_URL}/random")
    
    # Step 2: Verify the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Step 3: Verify the response is a list containing one poem
    poem = response.json()
    assert isinstance(poem, list), "Expected response to be a list"
    assert len(poem) == 1, "Expected list to contain one poem"

    # Step 4: Verify the poem contains the required fields
    required_fields = {'title', 'author', 'lines'}
    for field in required_fields:
        assert field in poem[0], f"Expected poem to contain '{field}'"

    # Step 5: Retry up to 3 times to get a different random poem
    original_poem = poem[0]
    for _ in range(3):
        response = requests.get(f"{BASE_URL}/random")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        new_poem = response.json()[0]
        if new_poem != original_poem:
            break
    else:
        assert new_poem != original_poem, "Expected different random poems on retries"

if __name__ == "__main__":
    pytest.main()
