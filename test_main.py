#! /usr/bin/env python3

import unittest
# https://docs.python.org/ja/3/library/unittest.html#assert-methods

from tests import alive
from tests import post


class TestSample(unittest.TestCase):
    def test_alive(self):
        res = alive.check_alive()
        self.assertEqual(res, 200)

    def test_post_params(self):
        cases = [
            {
                'params': {'id': '10', 'name': 'john'},
                'expected': {'id': '10', 'name': 'john'}
            },
            {
                'params': {'id': '11', 'name': 'paul'},
                'expected': {'id': '11', 'name': 'paul'}
            }
        ]

        for case in cases:
            expected = case['expected']
            params = case['params']
            result = post.test_post(case['params'])

            # httpbin.orgは投げたPOSTをそのままこの形で返してくれるので
            # {
            #  'form': {
            #   'id': '11',
            #   'name': 'paul'
            #  },,,
            # }

            # https://docs.python.org/ja/3/library/unittest.html?highlight=assert#distinguishing-test-iterations-using-subtests
            # サブテストを利用して繰り返しテストの区別を付ける
            with self.subTest(params=params, expected=expected, result=result):
                for key in expected:
                    self.assertEqual(result['form'][key], expected[key])


if __name__ == '__main__':
    unittest.main()
