from users import User
from course import Course
from majors import Major


class Scheduler:
    """
    This class holds schedule information
    """

    def __init__(self, user: User):
        """
        :param user: the owner of this schedule
        """
        if user is None:
            raise Exception('Could not create schedule with non-user')
        else:
            self.user = user

        # major of user
        self.major = None
        # completed course title array
        self.completed_courses = []
        # title array of courses to be taken
        self.remaining_courses = []

        # selected course title array
        self.selected_courses = []
        self.schedule = {}

    def reset(self):
        self.major = None
        self.completed_courses = []
        self.remaining_courses = []
        self.selected_courses = []
        self.schedule = {}

    def set_major(self, major_title: str):
        try:
            self.major = Major(major_title)
            self.remaining_courses = self.major.required_courses
            return True
        except:
            print("Invalid major title")
            return False

    def _check_if_passed_all_prerequisites(self, course_title: str) -> bool:
        if self.major is None:
            raise Exception("Major was not set")

        course = Course(course_title)
        # TODO: Course class should have a function to get all the prerequisites (maybe course array?)
        prerequisites = course.get_prerequisites()
        for prerequisite in prerequisites:
            if prerequisite not in self.completed_courses:
                return False

        return True

    def _check_if_already_taken(self, course_title: str) -> bool:
        if self.major is None:
            raise Exception("Major was not set")

        if course_title in self.completed_courses:
            return True
        else:
            return False

    def _check_if_has_duplicated_time_slots(self, course_title: str) -> bool:
        if self.major is None:
            raise Exception("Major was not set")

        new_course = Course(course_title)
        new_set = set(new_course.available_course_timeslots)
        for selected_course_title in self.selected_courses:
            selected_course = Course(selected_course_title)
            old_set = set(selected_course.available_course_timeslots)
            if old_set & new_set:
                return True

        return False

    def mark_course_as_completed(self, course_title):
        """
        Set a course as completed
        :param course_title:
        :return:
        """
        if self.major is None:
            raise Exception("Major was not set")

        if not self._check_if_already_taken(course_title):
            self.completed_courses.append(course_title)

        if course_title in self.remaining_courses:
            self.remaining_courses.remove(course_title)

    def select_course(self, course_title: str):
        """
        This function is for selecting a subject
            if succeed, return True
                failed, raise Exception
        :param course_title:
        :return:
        """
        if self.major is None:
            raise Exception("Major was not set")

        if self._check_if_already_taken(course_title):
            raise Exception("This subject is already taken")

        if not self._check_if_passed_all_prerequisites(course_title):
            raise Exception("This subject's prerequisites are not passed")

        if self._check_if_has_duplicated_time_slots(course_title):
            return Exception("This subject has duplicated timeslot.")

        self.selected_courses.append(course_title)
        self.build_schedule()

        return True

    def remove_course(self, course_title: str):
        """
        This function is for removing a course from selected courses
        :param course_title:
        :return:
        """
        if self.major is None:
            raise Exception("Major was not set")

        if course_title in self.selected_courses:
            self.selected_courses.remove(course_title)
            self.build_schedule()
            return True

        return False

    def build_schedule(self):
        """
        This function is for building a schedule from selected courses
        :return:
        """
        if self.major is None:
            raise Exception("Major was not set")

        self.schedule = {}
        
        for course_title in self.selected_courses:
            course = Course(course_title)
            for i in range(course.available_course_timeslots):
                self.schedule[course.available_course_timeslots[i]] = {
                    'Subject': course_title,
                    'Type': 'Class',
                    'Professor': course.course_professors[i],
                    'Class': course.available_classes[i],
                }

            for j in range(course.available_lab_timeslots):
                self.schedule[course.available_lab_timeslots[j]] = {
                    'Subject': course_title,
                    'Type': 'Lab',
                    'Professor': course.lab_professors[j],
                    'Lab': course.available_labs[j]
                }
