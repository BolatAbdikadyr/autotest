import unittest
from tests.testofnfc import nfc_check
from tests.First_Test_Case import first_test
from tests.Second_Test_Case import second_test


def run_tests(*test_classes):
    for test_class in test_classes:
        result = unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(test_class))
        if result.wasSuccessful():
            print(f"{test_class.__name__} passed.")
        else:
            print(f"{test_class.__name__} not passed.")


if __name__ == '__main__':
    run_tests(first_test, second_test)
