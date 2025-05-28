from playwright.sync_api import Page
from pages.like_page import LikePage


def test_like_exists(page: Page):
    like_page = LikePage(page)
    like_page.open()
    like_page.check_button_exists()


def test_like_click(page: Page):
    like_page = LikePage(page)
    like_page.open()
    like_page.click_button()
    like_page.check_result_text_is_('Submitted')
