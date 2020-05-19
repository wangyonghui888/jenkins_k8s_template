#!/usr/bin/env python
# coding=utf-8

"""
:author: liliu
:Description: test case example
"""
import allure


class TestCase(object):
    def test_case_example(self, env):
        with allure.step('Test pass'):
            print(env)
            assert 1 == True
