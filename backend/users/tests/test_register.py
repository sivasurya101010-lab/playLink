import pytest
from rest_framework.test import APIClient
from users.models import User

@pytest.mark.django_db
def test_register_user():
    client=APIClient()

    data = {
        "username": "surya",
        "identifier": "surya@gmail.com",
        "password": "Surya@123"
    }

    response=client.post("/api/auth/register/",data)

    assert response.status_code==201
    assert User.objects.filter(username="surya").exists()
