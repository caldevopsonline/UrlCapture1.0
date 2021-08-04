import pytest
from app import url_capture


@pytest.fixture
def app():
    app = url_capture()
    return app
