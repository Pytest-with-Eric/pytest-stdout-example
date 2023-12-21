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


def test_capsys(capsys):
    print("Hello, Pytest!")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Pytest!\n"


def test_capfd(capfd):
    # Capture output to `stdout` using basic and subprocess
    print("Hello, Pytest!")
    captured = capfd.readouterr()
    assert captured.out == "Hello, Pytest!\n"
    os.system("echo 'Passing test: Message to stdout - Running as subprocess'")
    captured = capfd.readouterr()
    assert captured.out == "Passing test: Message to stdout - Running as subprocess\n"

    # Capture output to `stderr` using basic and subprocess
    print("Oh we have an Error!", file=sys.stderr)
    captured = capfd.readouterr()
    assert captured.err == "Oh we have an Error!\n"


def test_capfdbinary(capfdbinary):
    # Directly write bytes to stdout
    os.write(1, b"Hello, Pytest!\n")
    captured = capfdbinary.readouterr()
    assert captured.out == b"Hello, Pytest!\n"


@pytest.mark.parametrize(
    "input, expected", ([("test1", "Result: test1"), ("test2", "Result: test2")])
)
def test_capsys_parametrization(capsys, input, expected):
    print(f"Result: {input}")
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
