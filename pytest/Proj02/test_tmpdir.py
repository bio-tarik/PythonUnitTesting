"""
Learning unit testing on Python using py.test.
Tutorial: docs.pytest.org/en/latest/getting-started.html#our-first-test-run
"""


def test_needsfiles(tmpdir):
    """
        Having a look at the pytest's tmpdir argument
    """
    print(tmpdir)
    assert 0
