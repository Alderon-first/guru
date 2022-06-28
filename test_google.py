from fixture import *


def test_search_positive(config):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('oriented Web UI browser tests in Python'))


def test_search_negative(config):
    browser.element('[name="q"]').should(be.blank).type('1').press_enter()
    browser.element('[id="search"]').should(have.text('Selen1'))

