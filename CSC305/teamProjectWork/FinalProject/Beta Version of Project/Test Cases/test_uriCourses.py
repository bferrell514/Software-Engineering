import unittest

from uri_majors import Course

class Course_Test_Case(unittest.TestCase):
    _course: Course

    def test_class_available(self):
        self._course = Course("CSC106")
        self.assertTrue(self._course.is_course_available("CSC106"))

    def test_class_not_available(self):
        self._course = Course("CSC301")
        self.assertFalse(self._course.is_course_available("CSC301"))

    def test_course_requires_lab(self):
        self._course = Course("CSC106")
        self.assertFalse(self._course.does_course_require_lab("CSC106"))

    def test_course_does_not_require_lab(self):
        self._course = Course("CSC211")
        self.assertTrue(self._course.does_course_require_lab("CSC211"))

    def test_yes_online_option(self):
        self._course = Course("CSC106")
        self.assertTrue(self._course.any_online_option("CSC106"))

    def test_no_online_option(self):
        self._course = Course("CSC211")
        self.assertFalse(self._course.any_online_option("CSC211"))

    def test_correct_location(self):
        self._course = Course("CSC106")
        self.assertEqual(self._course.location_of_class("TR_2:30-3:45",\
                         self._course.course_location, self._course.available_course_timeslots),\
                         "White Hall 205")

if __name__ == '__main__':
    unittest.main()
