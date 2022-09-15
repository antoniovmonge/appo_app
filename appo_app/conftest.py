import pytest

from appo_app.users.models import CustomUser
from appo_app.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> CustomUser:
    return UserFactory()
