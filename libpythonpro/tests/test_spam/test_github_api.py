from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/22728?v=4'
    resp_mock.json.return_value = {
        "login": "flavio", "id": 22728, "node_id": "MDQ6VXNlcjIyNzI4",
        "avatar_url": url,
    }
    mocker.patch('libpythonpro.github_api.requests.get')
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('flavio')
    assert avatar_url == url


def test_buscar_avatar_integraçao():
    url = github_api.buscar_avatar('flavio')
    assert 'https://avatars.githubusercontent.com/u/22728?v=4' == url
