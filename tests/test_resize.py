import unittest

from img_ai_prep.resize import resize_math


class TestResizeMethods(unittest.TestCase):

    def test_resize_square(self):
        """Resize a square"""
        img_size = (1024, 1024)
        new_long_side = 512

        expected_output = (512, 512)
        actual_output = resize_math(img_size, new_long_side)
        self.assertTupleEqual(expected_output, actual_output)

    def test_resize_square_2(self):
        """Resize a square with non-even size"""
        img_size = (1025, 1025)
        new_long_side = 512

        expected_output = (512, 512)
        actual_output = resize_math(img_size, new_long_side)
        self.assertTupleEqual(expected_output, actual_output)

    def test_resize_long(self):
        """Resize a long rectangle"""
        img_size = (1024, 2048)
        new_long_side = 512

        expected_output = (512, 1024)
        actual_output = resize_math(img_size, new_long_side)
        self.assertTupleEqual(expected_output, actual_output)

    def test_resize_wide(self):
        """Resize a wide square"""
        img_size = (2048, 1024)
        new_long_side = 512

        expected_output = (1024, 512)
        actual_output = resize_math(img_size, new_long_side)
        self.assertTupleEqual(expected_output, actual_output)
