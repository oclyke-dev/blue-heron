#!/usr/bin/env python3

"""
run with py.test
"""

import pytest

@pytest.fixture(scope='module')
def fixture():
    """fixture to demonstrate how fixtures work in pytest"""
    meaning = 42                # create a value
    yield meaning               # the value yielded from a fixture will be sent to the test
    print('fixture teardown')   # this function will be resumed at teardown of the test

# def test_failure():
#     # this test shows that failed tests are caught
#     assert False

def test_success():
    # this test shows that successful tests are identified
    assert True

def test_fixture(fixture):
    print('value of fixture: ')
    print(fixture)

def test_import():
    import blue_heron
