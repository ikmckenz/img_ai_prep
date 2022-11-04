import unittest

from img_ai_prep.crop import crop_math


class TestCropMethods(unittest.TestCase):

    def test_center_large(self):
        """Center of a large image where no adjustments made"""
        img_size = (1024, 1024)
        center = [512, 512]
        crop_size = 512

        expected_output = (256, 256, 768, 768)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_center_large_2(self):
        """Off center of a large image where no adjustments made"""
        img_size = (1024, 2024)
        center = [512, 512]
        crop_size = 512

        expected_output = (256, 256, 768, 768)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_center_large_3(self):
        """Off center of a large image (odd size) where no adjustments made"""
        img_size = (1023, 2023)
        center = [512, 512]
        crop_size = 512

        expected_output = (256, 256, 768, 768)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_left_adjustment(self):
        """Adjustment on the left side"""
        img_size = (1024, 1024)
        center = [0, 512]
        crop_size = 512

        expected_output = (0, 256, 512, 768)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_right_adjustment(self):
        """Adjustment on the right side"""
        img_size = (1024, 1024)
        center = [1024, 512]
        crop_size = 512

        expected_output = (512, 256, 1024, 768)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_upper_adjustment(self):
        """Adjustment on the upper side"""
        img_size = (1024, 1024)
        center = [512, 0]
        crop_size = 512

        expected_output = (256, 0, 768, 512)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_lower_adjustment(self):
        """Adjustment on the lower side"""
        img_size = (1024, 1024)
        center = [512, 1024]
        crop_size = 512

        expected_output = (256, 512, 768, 1024)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_left_and_upper_adjustment(self):
        """Adjustment on the left and upper sides"""
        img_size = (1024, 1024)
        center = [0, 0]
        crop_size = 512

        expected_output = (0, 0, 512, 512)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_left_and_upper_adjustment_2(self):
        """Adjustment on the left and upper sides"""
        img_size = (1024, 1024)
        center = [1, 2]
        crop_size = 512

        expected_output = (0, 0, 512, 512)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_right_and_lower_adjustment(self):
        """Adjustment on the right and lower sides"""
        img_size = (1024, 1024)
        center = [1024, 1024]
        crop_size = 512

        expected_output = (512, 512, 1024, 1024)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_right_and_lower_adjustment_2(self):
        """Adjustment on the right and lower sides"""
        img_size = (1024, 1024)
        center = [1023, 1022]
        crop_size = 512

        expected_output = (512, 512, 1024, 1024)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_positive_out_of_bounds(self):
        """Adjustment proper even with positive out of bounds"""
        img_size = (1024, 1024)
        center = [5000, 5000]
        crop_size = 512

        expected_output = (512, 512, 1024, 1024)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)

    def test_negative_out_of_bounds(self):
        """Adjustment proper even with negative out of bounds"""
        img_size = (1024, 1024)
        center = [-1, -1]
        crop_size = 512

        expected_output = (0, 0, 512, 512)
        actual_output = crop_math(img_size, center, crop_size)
        self.assertTupleEqual(expected_output, actual_output)
