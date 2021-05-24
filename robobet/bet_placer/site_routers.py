import time
from abc import ABC, abstractmethod
from contextlib import contextmanager

from selenium import webdriver

from settings import Bet1X

from .schemas import RouterResponse, create_router_response


class AbstractRouter(ABC):
    def __init__(self, username: int, password: str) -> None:
        self.username = username
        self.password = password

    @abstractmethod
    def get_balance(self) -> RouterResponse:
        pass


class Bet1XRouter(AbstractRouter):
    def __init__(self, username: int, password: str) -> None:
        super().__init__(username, password)

    @contextmanager
    def login(self):
        driver = webdriver.Firefox()

        try:
            driver.get(Bet1X.base_url)

            drop_login_btn = driver.find_element_by_id("curLoginForm")
            drop_login_btn.click()

            auth_id_email = driver.find_element_by_id("auth_id_email")
            auth_id_email.send_keys(self.username)

            auth_form_password = driver.find_element_by_id("auth-form-password")
            auth_form_password.send_keys(self.password)

            login_btn = driver.find_element_by_class_name("auth-button")
            login_btn.click()

            time.sleep(3)  # TODO: replace this block to `.wait_until`

            yield driver
        finally:
            exit_btn = driver.find_element_by_class_name("exitLink")
            exit_btn.click()

            driver.close()

    def get_balance(self) -> RouterResponse:
        response = create_router_response(
            path=Bet1X.get_balance,
            linter={
                "type": "ELEMENT",
                "tag": "p",
                "attrs": {"class": "top-b-acc__amount"},
            },
        )
        return response

    def get_live_matches(self) -> RouterResponse:
        response = create_router_response(
            path=Bet1X.base_url,
            linter={
                "type": "LIST",
                "tag": "div",
                "attrs": {"data-name": "dashboard-champ-content"},
                "children": {
                    "type": "LIST",
                    "tag": "div",
                    "attrs": {"class": "c-events__item"},
                },
            },
        )
        return response
