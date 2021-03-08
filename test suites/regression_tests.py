import unittest
from unittest.loader import makeSuite

from features.basic_auth import BasicAuth
from features.java_script_alerts import JavaScriptAlerts
from features.horizontal_slider import Slider
from features.log_in import HerokuappLoginPageTests
from features.dynamic_content import DynamicContent

def full_suite():
    test_suite = unittest.TestSuite()
    # adding couple test classes for "regression":
    test_suite.addTest(makeSuite(BasicAuth))
    test_suite.addTest(makeSuite(HerokuappLoginPageTests))
    test_suite.addTest(makeSuite(JavaScriptAlerts))
    test_suite.addTest(makeSuite(Slider))
    test_suite.addTest(makeSuite(DynamicContent))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(full_suite())