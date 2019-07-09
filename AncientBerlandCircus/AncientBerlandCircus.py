import math


class ShapeMatcher:
    def __init__(self, point1, point2, point3):
        self.point1_expected = point1
        self.point2_expected = point2
        self.point3_expected = point3
        self.angles = 3

    def match(self):
        reg_shape = None
        for angle in range(3, 100):
            self.angles = angle
            reg_shape = RegularShape((1, self.point1_expected), (2, self.point2_expected),
                                     (3, self.point3_expected), self.angles)
            reg_shape.match_points_id()
            found_matching = reg_shape.is_valid_shape()
            if found_matching:
                return reg_shape
        return reg_shape


class RegularShape:
    def __init__(self, point1, point2, point3, angles):
        self.points = [(x + 1, (0.0, 0.0)) for x in range(angles)]
        self.points[point1[0]-1] = point1
        self.points[point2[0]-1] = point2
        self.points[point3[0]-1] = point3
        self.point1_expected = point1
        self.point2_expected = point2
        self.point3_expected = point3
        self.angles = angles
        self.angle_ratio = ((angles - 2) * math.pi) / angles
        self.middle_function = MiddleFunction(point1[1], point2[1], point3[1])
        self.generate_points()

    def generate_points(self):
        for x in range(self.angles):
            if not x + 1 == self.point1_expected[0]:
                self.points[x] = x+1, self.generate_point(x + 1)

    def generate_point(self, n):
        return get_point_angle_related(self.middle_function.center, self.middle_function.point1, (n-1)*self.angle_ratio)

    def get_nth_point(self, n):
        return self.points[n-1]

    def is_valid_shape(self):
        return self.point_in_shape(self.point1_expected) and \
               self.point_in_shape(self.point2_expected) and \
               self.point_in_shape(self.point3_expected)

    def point_in_shape(self, point):
        return points_almost_equal(self.points[point[0]-1][1], point[1])

    def get_area(self):
        return round((distance(self.middle_function.center, self.point1_expected[1])**2)*math.sin(self.angle_ratio)/2*self.angles, 6)

    def match_points_id(self):
        for point in self.points:
            if points_almost_equal(point[1], self.point2_expected[1]):
                self.point2_expected = point
            if points_almost_equal(point[1], self.point3_expected[1]):
                self.point3_expected = point


class MiddleFunction:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.middle_point = get_middle_point(point1, point2)
        self.slope = get_slope(point1, point2)
        if self.slope:
            self.rest = self.middle_point[1] + 1 / self.slope * self.middle_point[0]
        else:
            self.rest = 0.0
        self.center = (0.0, 0.0)
        self.radius = 1.0
        self.find_center()

    def __call__(self, x):
        if self.slope:
            try:
                return -(1/self.slope) * x + self.rest
            except ZeroDivisionError:
                return self.point1[0]
        else:
            return min(self.point1[1], self.point2[1]) + abs(self.point1[1] - self.point2[1])/2

    def find_center(self):
        x = self.middle_point[0]
        step = 0.1
        tolerance = 0.0000000001
        difference = 0
        last_error = 0.1
        expected = distance((x, self(x)), self.point1)
        while(distance((x, self(x)), self.point3)-expected > tolerance):
            difference = last_error - distance((x, self(x)), self.point3)-expected
            last_error = distance((x, self(x)), self.point3)-expected
            if difference > 0:
                step = -difference/10
            x += step
            expected = distance((x, self(x)), self.point1)
        self.center = (x, self(x))
        self.radius = expected
        return self.center


def distance(point1, point2):
    return math.sqrt(abs(point1[0]-point2[0])**2 + abs(point1[1]-point2[1])**2)


def get_middle_point(point1, point2):
    x = min(point1[0], point2[0]) + abs(point1[0]-point2[0])/2
    y = min(point1[1], point2[1]) + abs(point1[1]-point2[1])/2
    return x, y


def get_slope(point1, point2):
    try:
        return (point1[1] - point2[1])/(point1[0]-point2[0])
    except ZeroDivisionError:
        return None


def get_point_on_circle(center, radius, angle):
    return center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle)


def get_point_angle(center, point):
    result = math.atan2(point[1] - center[1], point[0] - center[0])
    if result < 0:
        result = math.pi*2 + result
    return result


def get_point_angle_related(center, point, angle):

    real_angle = get_point_angle(center, point) - angle
    if real_angle < 0:
        real_angle = math.pi*2 + real_angle
    return get_point_on_circle(center, distance(center, point), real_angle)


def points_almost_equal(point1, point2):
    return round(point1[0], 7) == round(point2[0], 7) and round(point1[1], 7) == round(point2[1], 7)


if __name__ == "__main__":
    data = [input(), input(), input()]
    matcher = ShapeMatcher((float(data[0].split(" ")[0]), float(data[0].split(" ")[1])),
                           (float(data[1].split(" ")[0]), float(data[1].split(" ")[1])),
                           (float(data[2].split(" ")[0]), float(data[2].split(" ")[1])))
    shape = matcher.match()
    print(shape.get_area())
