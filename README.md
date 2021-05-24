# robobet


## How use the routers and parser
```python
from robobet.bet_placer.parser import RouterParser
from robobet.bet_placer.site_routers import Bet1XRouter


parser = RouterParser()
router = Bet1XRouter("username", "password")


with router.login() as logged_driver:
    html = logged_driver.page_source
    data = parser.load(html, router.get_balance())

>>> data = your account ballance
```

## How parser and routers work
* **Routers**

In the router class you can create pipeline of work of your scraper.

Router can:
1. Set behaviour of your scraper
2. Manipulate on matched element

Example: 
```python
class Bet1XRouter(AbstractRouter):
    def __init__(self, username: int, password: str) -> None:
        super().__init__(username, password)

    @contextmanager
    def login(self):
        ...

    def get_live_matches(self) -> RouterResponse:
        response = create_router_response(
            path=Bet1X.base_url,  # URL to web page
            linter={
                "type": "ELEMENT",  # Is it single element or list?
                "tag": "div",  # Tag 
                "attrs": {"data-name": "dashboard-champ-content"},  # Attrs of tag
                "children": {  # If you need to extract child element
                    "type": "LIST",
                    "tag": "div",
                    "attrs": {"class": "c-events__item"},
                },
            },
        )
        return response
```