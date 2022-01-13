# class Course:
#     def __init__(self, course_name: str, times_and_places: set[tuple[str, str]]):
#         self.course_name = course_name
#         self.times_and_places = times_and_places

# csc305 = Course("CSC305", "Tyler Hall 205", "TuTh_11AM-12:30PM")

class Course:
    '''
    This class sets information about the individual courses themselves,
    which includes the times they run, how many available courses there
    are, as well as the professors teaching said classes, and how many
    professor options there are.
    '''

    def __init__(self, subject_course: str):
        '''
        Note these are temporary, will update with info from web scraped data
        '''

        if (subject_course == "CSC106"):
            # Sets timeslots available for courses and labs
            self.available_course_timeslots = ["MWF_8:00-8:50", "MWF_10:00-10:50", "TR_2:30-3:45",\
                                              "ONLINE"]
            self.available_lab_timeslots = []

            # Stores professors teaching the courses and labs, stored by the index of the timeslots above
            self.course_professors = ["Victor Fay-Wolfe", "Victor Fay-Wolfe", "Victor Fay-Wolfe",\
                                     "Victor Fay-Wolfe"]
            self.lab_professors = []

            # Stores location of the class, stored by the index of the timeslots above
            self.course_location = ["White Hall 205", "Tyler 300", "White Hall 205", "ONLINE"]
            self.lab_location = []
        elif (subject_course == "CSC110"):
            # Sets timeslots available for courses and labs
            self.available_course_timeslots = ["MWF_9:00-9:50", "MWF_12:00-12:50", "MWF_2:00-2:50",\
                                              "TR_3:30-4:45"]
            self.available_lab_timeslots = ["F_8:00-9:45", "F_10:00-11:45"]

            # Stores professors teaching the courses and labs, stored by the index of the timeslots above
            self.course_professors = ["Lisa DiPippo", "Victor Fay-Wolfe", "Lisa DiPippo", "Lisa DiPippo"]
            self.lab_professors = ["Lisa DiPippo", "Lisa DiPippo"]

            # Stores location of the class, stored by the index of the timeslots above
            self.course_location = ["White Hall 205", "White Hall 207", "White Hall 205", "White Hall 207"]
            self.lab_location = ["Tyler Hall 055", "Tyler Hall 055"]
        elif (subject_course == "CSC211"):
            # Sets timeslots available for courses and labs
            self.available_course_timeslots = ["TR_12:30-1:45"]
            self.available_lab_timeslots = ["F_10:00-11:45", "F_12:00-1:45"]

            # Stores professors teaching the courses and labs, stored by the index of the timeslots above
            self.course_professors = ["Michael Conti"]
            self.lab_professors = ["Michael Conti", "Michael Conti"]

            # Stores location of the class, stored by the index of the timeslots above
            self.course_location = ["Beaupre 105"]
            self.lab_location = ["Library 166", "Tyler Hall 055"]
        elif (subject_course == "CSC212"):
            # Sets timeslots available for courses and labs
            self.available_course_timeslots = ["TR_8:00-9;45", "TR_3:30-4:45"]
            self.available_lab_timeslots = ["M_10:00-11:45", "M_12:00-1:45"]

            # Stores professors teaching the courses and labs, stored by the index of the timeslots above
            self.course_professors = ["Marco Alvarez Vega", "Marco Alvarez Vega"]
            self.lab_professors = ["Marco Alvarez Vega", "Marco Alvarez Vega"]

            # Stores location of the class, stored by the index of the timeslots above
            self.course_location = ["White Hall 205", "White Hall 205"]
            self.lab_location = ["Library 166", "Library 166"]
        elif (subject_course == "CSC301"):
            # Sets timeslots available for courses and labs
            self.available_course_timeslots = []
            self.available_lab_timeslots = []

            # Stores professors teaching the courses and labs
            # Note: Stored by the index of the timeslots above
            self.course_professors = []
            self.lab_professors = []

            # Stores location of the class, stored by the index of the timeslots above
            self.course_location = []
            self.lab_location = []
        else:
            # Course not found
            raise Exception("Not a valid course")

        # Sets amount of available courses and labs
        self.available_classes = len(self.available_course_timeslots)
        self.available_labs = len(self.available_lab_timeslots)

        # Sets count of unique professor options
        self.course_professor_count = len(set(self.course_professors))
        self.lab_professor_count = len(set(self.lab_professors))

    def is_course_available(self, subject_course):
        '''
        This checks if there are any available options for
        a specific course.
        '''
        if (self.available_classes == 0):
            return False

        return True

    def does_course_require_lab(self, subject_course):
        '''
        This checks if a specific class requires any labs.
        '''
        if (self.available_labs == 0):
            return False

        return True

    # Note that this has not yet been implemented for the 7/4/2020 12:00PM deadline
    def count_professors(self, professor_list):
        '''
        This returns a count of how many unique professor
        options are available to the student.
        '''
        unique_professors = set(self.professor_list)
        unique_professor_count = len(unique_professors)

        return unique_professor_count

    def any_online_option(self, subject_course):
        '''
        This checks if a specific course has an online option.
        '''
        for course in self.available_course_timeslots:
            if (course == "ONLINE"):
                return True

        return False

    def location_of_class(self, requested_timeslot, location_list, timeslot_list):
        '''
        This returns the location of the classroom for the requested timeslot
        for a specific course.
        '''
        for i in range(len(timeslot_list)):
            if (timeslot_list[i] == requested_timeslot):
                index = i
                break

        return location_list[index]


# TESTING AREA
# -----------------------------------
if __name__ == "__main__":
    print('\n------------------------------')
    print('Major Testing')
    print('\n------------------------------')
    new_user_major = Major("CPE_BS")
    print(new_user_major.required_courses)

    print('\n')

    print('\n------------------------------')
    print('Course Testing')
    print('\n------------------------------')

    testing_course_1 = Course("CSC106")
    testing_course_2 = Course("CSC211")
    testing_course_3 = Course("CSC301")

    print('\n')

    print("The location of the Tuesday/Thursday 2:30-3:45PM CSC106 course is " +\
            str(testing_course_1.location_of_class("TR_2:30-3:45", testing_course_1.course_location,\
                testing_course_1.available_course_timeslots)))

    print('\n')

    print("CSC106")
    print("-------")
    print("Number of Available Classes for CSC106: " + str(testing_course_1.available_classes))
    print("Available Class Timeslots for CSC106: " + str(testing_course_1.available_course_timeslots))

    print('\n')

    print("CSC211")
    print("-------")
    print("Number of Available Classes for CSC211: " + str(testing_course_2.available_classes))
    print("Available Class Timeslots for CSC211: " + str(testing_course_2.available_course_timeslots))
    print("Number of Available Labs for CSC211: " + str(testing_course_2.available_labs))
    print("Available Lab Timeslots for CSC211: " + str(testing_course_2.available_lab_timeslots))

    print('\n')

    print("CSC301")
    print("-------")
    print("Number of Available Classes for CSC301: " + str(testing_course_3.available_classes))
    print("Available Class Timeslots for CSC301: " + str(testing_course_3.available_course_timeslots))

    print('\n')

    '''
    Note: I really don't like that it's calling CSC106 twice.
    Example: Course("CSC106").is_course_available("CSC106")
    '''
    print("CSC106 is available: " + str(testing_course_1.is_course_available("CSC106")))
    print("CSC301 is available: " + str(testing_course_3.is_course_available("CSC301")))

    print("List of Professors teaching CSC106: " + str(testing_course_1.course_professors))
    print("There are " + str(testing_course_1.course_professor_count) +\
            " different professor options to choose from.")

    print("List of Professors teaching CSC110: " + str(Course("CSC110").course_professors))
    print("There are " + str(Course("CSC110").course_professor_count) +\
            " different professor options to choose from.")

    print("List of Professors teaching CSC301: " + str(Course("CSC301").course_professors))
    print("There are " + str(Course("CSC301").course_professor_count) +\
            " different professor options to choose from.")



    print('\n')

    #Text parser (from prof.)
    # Requires import re

    def listCourses(pre_text):
        pieces = re.findall(r"\b([A-Z]{3}|[0-9]{3})\b", pre_text)
        currentDepartment = None
        prerequisites = []

        for item in pieces:
            if item.isdigit():
                if currentDepartment is None:
                    raise ValueError
                # you should have a more useful data type to instantiate here:
                prerequisites.append(currentDepartment+" "+item)
            else:
                currentDepartment = item
        return prerequisites


    ele212 = "Pre: (ELE 201, PHY 204, (credit or concurrent enrollment in MTH 244 or 362),\
              and (at least a 2.00 (C) average in MTH 141, MTH 142, PHY 203, and PHY 204))\
              or permission of instructor.)"
    print(listCourses(ele212))