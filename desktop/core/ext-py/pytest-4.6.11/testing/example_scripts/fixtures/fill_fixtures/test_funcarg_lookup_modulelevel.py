# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def something(request):
    return request.function.__name__


class TestClass(object):
    def test_method(self, something):
        assert something == "test_method"


def test_func(something):
    assert something == "test_func"
