"""
Learning unit testing on Python using unittest.
Tutorial: http://pythontesting.net/framework/nose/nose-introduction/
"""

from nose.tools import assert_equals
from markdown_adapter import run_markdown


def test_non_marked_lines():
    """
        Non-marked lines should only get 'p' tags around all input
    """
    assert_equals(run_markdown('this line has no special handling'),
                  'this line has no special handling</p>')


def test_em():
    """
        Lines surrounded by asterisks should be wrapped in 'em' tags
    """
    assert_equals(run_markdown('*this should be wrapped in em tags*'),
                  '<p><em>this should be wrapped in em tags</em></p>')


def test_strong():
    """
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
    """
    assert_equals(run_markdown('**this should be wrapped in strong tags**'),
                  '<p><strong>this should be wrapped in strong \
                  tags</strong></p>')
