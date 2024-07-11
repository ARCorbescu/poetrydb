import requests
import pytest

BASE_URL = "https://poetrydb.org"

@pytest.mark.parametrize("author, title", [
    ("Emily Dickinson", "Nature can do no more"),
    ("Thomas Campbell", "Lord Ullin's Daughter"),
    ("Thomas Campbell", "The River of Life"),
])
def test_get_poems_by_author_and_title(author, title):
    """
    Test the /author,title endpoint of the PoetryDB API.

    Steps:
    1. Send a GET request to the /author,title endpoint to retrieve poems by a specific author and title.
    2. Verify the response status code is 200 (OK).
    3. Verify the response is a list.
    4. Verify the author and title of each poem in the response match the requested author and title.

    Expected Result:
    The API should return a list of poems where each poem's author and title match the specified author and title.
    """
    # Step 1: Send a GET request to the /author,title endpoint
    response = requests.get(f"{BASE_URL}/author,title/{author};{title}")
    
    # Step 2: Verify the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Step 3: Verify the response is a list
    poems = response.json()
    assert isinstance(poems, list), "Expected response to be a list"

    # Step 4: Verify the author and title of each poem match the requested author and title
    for poem in poems:
        assert 'author' in poem, "Expected poem to contain 'author'"
        assert 'title' in poem, "Expected poem to contain 'title'"
        assert poem['author'] == author, f"Expected author to be '{author}'"
        assert poem['title'] == title, f"Expected title to be '{title}'"

if __name__ == "__main__":
    pytest.main()
