import pytest


@pytest.mark.parametrize("api_fixture",
                         [("get", "https://reqres.in/api/users?page=2"),
                          ("post", "https://reqres.in/api/login", {"email": "eve.holt@reqres.in", "password": "cityslicka"})],
                         indirect=True)
def test_200(api_fixture):
    assert api_fixture == 200


@pytest.mark.parametrize("api_fixture",
                         [("post", "https://reqres.in/api/users", {"name": "morpheus","job": "leader"})],
                         indirect=True)
def test_201(api_fixture):
    assert api_fixture == 201


@pytest.mark.parametrize("api_fixture",
                         [("post", "https://reqres.in/api/register", {"email": "sydney@fife"}), 
                          ("post", "https://reqres.in/api/login", {"email": "peter@klaven"})],
                         indirect=True)
def test_400(api_fixture):
    assert api_fixture == 400
