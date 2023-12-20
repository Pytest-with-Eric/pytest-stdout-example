import sys
import os
import pytest


def test_pass():
    print("Passing test: Message to stdout")
    print("Passing test: Message to stderr", file=sys.stderr)
    os.system(
        "echo 'Passing test: Message to stdout - Running as subprocess'"
    )  # stdin = 0, stdout = 1, stderr = 2
    os.system("echo 'Passing test: Message to stderr - Running as subprocess' >&2")
    assert True


# @pytest.mark.skip(reason="don't want to test it")
def test_fail():
    print("Failing test: Message to stdout")
    print("Failing test: Message to stderr", file=sys.stderr)
    os.system(
        "echo 'Failing test: Message to stdout - Running as subprocess'"
    )  # stdin = 0, stdout = 1, stderr = 2
    os.system("echo 'Failing test: Message to stderr - Running as subprocess' >&2")
    assert False
