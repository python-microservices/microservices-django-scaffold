import pytest
from django.test import Client

from template.models import Color


# Create your tests here.


@pytest.mark.django_db
def test_model():
    color_red, created = Color.objects.get_or_create(name='red')
    assert color_red.name == "red"


@pytest.mark.django_db
def test_view_empty():
    c = Client()
    response = c.get('/template/')
    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_view_with_data():
    c = Client()
    Color.objects.get_or_create(name='red')
    response = c.get('/template/')
    assert response.status_code == 200
    assert response.data[0]["id"] == 1
    assert response.data[0]["name"] == "red"
