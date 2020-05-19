#!/usr/bin/env python
# coding=utf-8
import pytest


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test", help="environment: dev ,test or stg")


@pytest.fixture(scope="session", autouse=False)
def cmdopt(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session", autouse=False)
def env(request, cmdopt):
    """
    Parse env config info
    :param request:
    :param cmdopt:
    :return: 返回环境
    """
    env_config = {'env':cmdopt, 'mysql':'XXX'}
    return env_config