from django.shortcuts import resolve_url
import pytest
from rest_framework.status import HTTP_200_OK


URL = resolve_url("whoiam")

@pytest.mark.integration
def test_positive(client_api, user_with_token):

    client_api.credentials(HTTP_AUTHORIZATION='Token ' + user_with_token.auth_token.key)

    response = client_api.get(URL)

    assert response.status_code == HTTP_200_OK

    body = response.json()

    assert body["id"] == user_with_token.pk
    assert body["user"] == user_with_token.email
    assert body["created_at"] == str(user_with_token.created_at)
    assert body["modified_at"] == str(user_with_token.modified_at)
    assert body["permission"] == {
        "ADMIN": user_with_token.is_superuser,
        "STAFF": user_with_token.is_staff,
    }
