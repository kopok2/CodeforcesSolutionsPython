import unittest
import math
from AncientBerlandCircus.AncientBerlandCircus import RegularShape, distance, get_middle_point, MiddleFunction, \
    get_slope, get_point_on_circle, get_point_angle, get_point_angle_related, ShapeMatcher, \
    points_almost_equal


class AncientBerlandCircus(unittest.TestCase):
    def test_regular_shape_init(self):
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 3)
        self.assertEqual(reg_shape.point1_expected, (1, (0.0, 0.0)))
        self.assertAlmostEqual(reg_shape.angle_ratio, math.pi/3)

    def test_get_nth_point(self):
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 4)
        self.assertEqual(reg_shape.get_nth_point(3), (3, (1.0, 1.0)))

    def test_generate_points(self):
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 4)
        self.assertAlmostEqual(reg_shape.get_nth_point(2)[1][0], 0.0)
        self.assertAlmostEqual(reg_shape.get_nth_point(2)[1][1], 1.0)
        self.assertAlmostEqual(reg_shape.get_nth_point(3)[1][0], 1.0)
        self.assertAlmostEqual(reg_shape.get_nth_point(3)[1][1], 1.0)
        self.assertAlmostEqual(reg_shape.get_nth_point(4)[1][0], 1.0)
        self.assertAlmostEqual(reg_shape.get_nth_point(4)[1][1], 0.0)

    def test_distance(self):
        self.assertAlmostEqual(distance((0.0, 0.0), (1.0, 0.0)), 1.0)
        self.assertAlmostEqual(distance((0.0, 0.0), (0.0, 1.0)), 1.0)
        self.assertAlmostEqual(distance((0.0, 0.0), (1.0, 1.0)), 1.4142135623730950)

    def test_get_middle_point(self):
        self.assertEqual(get_middle_point((0.0, 0.0), (1.0, 1.0)), (0.5, 0.5))
        self.assertEqual(get_middle_point((-1.0, -1.0), (1.0, 1.0)), (0.0, 0.0))
        self.assertEqual(get_middle_point((0.0, 0.0), (0.0, 1.0)), (0.0, 0.5))

    def test_middle_function_init(self):
        mid_func = MiddleFunction((0.0, 0.0), (1.0, 1.0), (2.0, 0.0))
        self.assertEqual(mid_func.middle_point, (0.5, 0.5))
        self.assertEqual(mid_func.slope, 1.0)
        self.assertEqual(mid_func.rest, 1.0)

    def test_get_slope(self):
        self.assertAlmostEqual(get_slope((0.0, 0.0), (1.0, 1.0)), 1.0)
        self.assertAlmostEqual(get_slope((0.0, 0.0), (1.0, 2.0)), 2.0)
        self.assertAlmostEqual(get_slope((0.0, 0.0), (0.0, 2.0)), None)

    def test_middle_function_find_center(self):
        mid_func = MiddleFunction((0.0, 0.0), (1.0, 1.0), (2.0, 0.0))
        self.assertAlmostEqual(mid_func.find_center()[0], 1.0)
        self.assertAlmostEqual(mid_func.find_center()[1], 0.0)
        self.assertAlmostEqual(mid_func.radius, 1.0)
        mid_func = MiddleFunction((0.0, 0.0), (0.0, 1.0), (1.0, 1.0))
        self.assertAlmostEqual(mid_func.find_center()[0], 0.5)
        self.assertAlmostEqual(mid_func.find_center()[1], 0.5)

    def test_middle_function_call(self):
        mid_func = MiddleFunction((0.0, 0.0), (1.0, 1.0), (2.0, 0.0))
        self.assertEqual(mid_func(0.0), 1.0)

    def test_generate_point(self):
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 4)
        self.assertAlmostEqual(reg_shape.generate_point(4)[0], 1.0)
        self.assertAlmostEqual(reg_shape.generate_point(4)[1], 0.0)

    def test_get_point_on_circle(self):
        self.assertAlmostEqual(get_point_on_circle((0.0, 0.0), 1, 0)[0], 1.0)
        self.assertAlmostEqual(get_point_on_circle((0.0, 0.0), 1, 0)[1], 0.0)

    def test_get_point_angle(self):
        self.assertAlmostEqual(get_point_angle((0.0, 0.0), (1.0, 0.0)), 0.0)
        self.assertAlmostEqual(get_point_angle((0.0, 0.0), (0.0, 1.0)), math.pi/2)
        self.assertAlmostEqual(get_point_angle((0.0, 0.0), (-1.0, 0.0)), math.pi)
        self.assertAlmostEqual(get_point_angle((0.0, 0.0), (0.0, -1.0)), math.pi*3/2)

    def test_get_point_angle_related(self):
        self.assertAlmostEqual(get_point_angle_related((0.0, 0.0), (-1.0, 0.0), math.pi/2)[0], 0.0)
        self.assertAlmostEqual(get_point_angle_related((0.0, 0.0), (-1.0, 0.0), math.pi/2)[1], 1.0)
        self.assertAlmostEqual(get_point_angle_related((0.0, 0.0), (-1.0, 0.0), math.pi)[0], 1.0)
        self.assertAlmostEqual(get_point_angle_related((0.0, 0.0), (-1.0, 0.0), math.pi)[1], 0.0)

    def test_is_valid_shape(self):
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 4)
        self.assertTrue(reg_shape.is_valid_shape())
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (2.0, 2.0)), (3, (4.0, 0.0)), 4)
        self.assertTrue(reg_shape.is_valid_shape())
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 5)
        self.assertFalse(reg_shape.is_valid_shape())

    def test_point_in_shape(self):
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 4)
        self.assertTrue(reg_shape.point_in_shape((2, (0.0, 1.0))))
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 4)
        self.assertTrue(reg_shape.point_in_shape((3, (1.0, 1.0))))
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 5)
        self.assertFalse(reg_shape.point_in_shape((3, (6.0, 6.0))))

    def test_find_first_matching_shape(self):
        shape_matcher = ShapeMatcher((0.0, 0.0), (0.0, 1.0), (1.0, 1.0))
        shape_matcher.match()
        self.assertEqual(shape_matcher.angles, 4)
        shape_matcher = ShapeMatcher((0.0, 0.0), (1.0, 1.0), (2.0, 0.0))
        shape_matcher.match()
        self.assertEqual(shape_matcher.angles, 4)

    def test_shape_matcher_init(self):
        shape_matcher = ShapeMatcher((0.0, 0.0), (0.0, 1.0), (1.0, 1.0))
        self.assertEqual(shape_matcher.point1_expected, (0.0, 0.0))
        self.assertEqual(shape_matcher.point2_expected, (0.0, 1.0))
        self.assertEqual(shape_matcher.point3_expected, (1.0, 1.0))
        self.assertEqual(shape_matcher.angles, 3)

    def test_get_shape_area(self):
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (3, (1.0, 1.0)), 4)
        self.assertEqual(reg_shape.get_area(), 1)
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (1.0, 1.0)), (3, (2.0, 0.0)), 4)
        self.assertEqual(reg_shape.get_area(), 2)
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (1.0, 1.0)), (3, (1.0, -1.0)), 4)
        self.assertEqual(reg_shape.get_area(), 2)

    def test_match_points_id(self):
        reg_shape = RegularShape((1, (0.0, 0.0)), (2, (0.0, 1.0)), (4, (1.0, 1.0)), 4)
        self.assertFalse(reg_shape.is_valid_shape())
        reg_shape.match_points_id()
        self.assertTrue(reg_shape.is_valid_shape())

    def test_matcher_matching(self):
        shape_matcher = ShapeMatcher((0.0, 0.0), (1.0, 1.0), (1.0, -1.0))
        shape = shape_matcher.match()
        self.assertEqual(shape.get_area(), 2)

    def test_points_almost_equal(self):
        self.assertTrue(points_almost_equal((1.0, 1.0), (0.999999999, 1.0000000006)))
        self.assertFalse(points_almost_equal((1.0, 1.0), (0.0, 0.0)))
