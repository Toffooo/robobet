import pytest
import ast


class Helpers:
    def get_integration_response(self):
        with open("samples/integration_response.txt", "r") as f:
            data = ast.literal_eval(f.read())
            data.sort()
        return data


@pytest.fixture
def helpers():
    return Helpers()
