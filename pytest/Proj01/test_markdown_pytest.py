"""
Learning unit testing on Python using py.test.
Tutorial: http://pythontesting.net/framework/pytest/pytest-introduction/
"""

from markdown_adapter import run_markdown


def test_non_marked_lines():
    '''
    Non-marked lines should only get 'p' tags around all input
    '''
    assert run_markdown('this line has no special handling') == \
        'this line has no special handling</p>'


def test_em():
    '''
    Lines surrounded by asterisks should be wrapped in 'em' tags
    '''
    assert run_markdown('*this should be wrapped in em tags*') == \
        '<p><em>this should be wrapped in em tags</em></p>'


def test_strong():
    '''
    Lines surrounded by double asterisks should be wrapped in 'strong' tags
    '''
    assert run_markdown('**this should be wrapped in strong tags**') == \
        '<p><strong>this should be wrapped in strong tags</strong></p>'
