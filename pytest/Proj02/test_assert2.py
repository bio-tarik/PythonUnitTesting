"""
    Learning unit testing on Python using py.test.
    Tutorial: https://docs.pytest.org/en/latest/assert.html
"""


def test_set_comparison():
    """
        Compares two set objects
    """
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2
