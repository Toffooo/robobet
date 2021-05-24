from bs4 import ResultSet
import pytest

from robobet import RouterParser, Bet1XRouter


@pytest.fixture
def router() -> Bet1XRouter:
    router = Bet1XRouter(123, "password")
    return router


@pytest.fixture
def parser() -> RouterParser:
    parser = RouterParser()
    return parser


@pytest.fixture
def html_from_web_page():
    with open("samples/source.txt") as f:
        html = f.read()
    return html


def test_parser_router(html_from_web_page, router, parser, helpers):
    data = parser.load(html_from_web_page, router.get_live_matches())
    assert isinstance(data, ResultSet)
