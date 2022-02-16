import pytest
import requests


@pytest.fixture()
def api_fixture(request):
    request_type = request.param[0]
    url = request.param[1]
    if len(request.param) == 3:
        data = request.param[2]
        response = getattr(requests, request_type)(url, data)
    else:
        response = getattr(requests, request_type)(url)
    return response.status_code



