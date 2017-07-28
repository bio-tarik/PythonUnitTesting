"""
    Learning unit testing on Django web application using selenium
    Tutorial: https://www.obeythetestinggoat.com/book/praise.harry.html
"""

from selenium import webdriver

WEB_BROWSER = webdriver.Firefox()
WEB_BROWSER.get('http://localhost:8000')

assert 'Django' in WEB_BROWSER.title
