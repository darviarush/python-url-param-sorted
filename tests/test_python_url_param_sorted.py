import sys
import unittest

from url_param_sorted import url_param_sorted


class UrlParamSortedTestCase(unittest.TestCase):

    def test_url_param_sorted(self):
        """ тест функций """

        self.assertEqual(url_param_sorted('y=1&z=&x=2&x=3&z&x=1'), 'x=1&x=2&x=3&y=1&z&z=')
        self.assertEqual(url_param_sorted({'y': 1, 'z': ["", None], 'x': [2, 3, 1]}), 'x=1&x=2&x=3&y=1&z&z=')

        with self.assertRaises(TypeError):
            url_param_sorted([])


if __name__ == '__main__':
    unittest.main()
