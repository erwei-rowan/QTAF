# -*- coding: utf-8 -*-
"""test case for runner test
"""

from testbase import TestCase
from testbase import testresult

class SuccTest(TestCase):
    """测试示例"""

    timeout = 1
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    expect_passed = True

    def run_test(self):
        pass


class ErrLogTest(TestCase):
    """测试示例"""

    timeout = 1
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    expect_passed = False

    def run_test(self):
        self.test_result.error("error")


class FailedTest(TestCase):
    """测试示例"""

    timeout = 1
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    expect_passed = False

    def run_test(self):
        self.fail("error")


class ExceptTest(TestCase):
    """测试示例"""

    timeout = 1
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    expect_passed = False

    def run_test(self):
        raise RuntimeError("fault")

class FilterCustomTest(TestCase):
    """测试示例"""

    timeout = 1
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    expect_passed = True

    def pre_test(self):
        return testresult.TestResultType.FILTERED, "xxx"

    def run_test(self):
        raise RuntimeError

if __name__ == "__main__":
    SuccTest().debug_run()
