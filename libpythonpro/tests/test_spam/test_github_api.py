from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        "login": "flavio", "id": 22728, "node_id": "MDQ6VXNlcjIyNzI4",
        "avatar_url": "https://avatars.githubusercontent.com/u/22728?v=4",
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('flavio')
    assert 'https://avatars.githubusercontent.com/u/22728?v=4' == url
