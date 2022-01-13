import unittest
import json

from courseReader import CourseRequester, CourseInterpreter, CourseFormatter, CourseData, CourseFacade


class CourseRequesterTestCase(unittest.TestCase):
    _courseRequester: CourseRequester

    def setUp(self) -> None:
        """
        The private _courseRequester object is created fresh for every test_* method by the setUp method.
        :return: None
        """
        self._courseRequester = CourseRequester()

    def test_CSC_305_course(self):
        content = self._courseRequester.getCourse('CSC', '305')
        json_res = json.loads(content)
        self.assertEqual('1023', json_res[0]['id'])
        self.assertEqual('4/19/2018', json_res[0]['Eff_Date'])
        self.assertEqual('A_SCI', json_res[0]['Acad_Group'])
        self.assertEqual('College of Arts and Sciences ', json_res[0]['College_Name'])
        self.assertEqual('COMP_SCIEN', json_res[0]['Acad_Org'])
        self.assertEqual('Computer Science', json_res[0]['FormalDesc'])
        self.assertEqual('CSC', json_res[0]['Subject'])
        self.assertEqual(' 305', json_res[0]['Catalog'])
        self.assertEqual('200754', json_res[0]['Course_id'])
        self.assertEqual('Software Engineering', json_res[0]['Long_Title'])
        self.assertEqual('4', json_res[0]['Min_Units'])
        self.assertEqual('4', json_res[0]['Max_Units'])
        self.assertEqual('LEC', json_res[0]['Component'])
        self.assertEqual('GE', json_res[0]['Designation'])
        self.assertEqual(
            '(4 crs.) Programming environments and methodologies for the design, development, testing, and maintenance of large software systems. Student teams will develop a substantial software product from requirements to delivery using disciplined techniques. (Lec. 3, Project 3) Pre: CSC 212. (D1)',
            json_res[0]['Descr'])
        self.assertEqual('A', json_res[0]['Status'])
        self.assertEqual('Y', json_res[0]['Sch_Print'])
        self.assertEqual('Y', json_res[0]['Cat_Print'])
        self.assertEqual('3420', json_res[0]['Rq_Group'])

    def test_empty_deptCode_raises_TypeError(self):
        self.assertRaises(TypeError, self._courseRequester.getCourse(''))


class CourseInterpreterTestCase(unittest.TestCase):
    _courseInterpreter: CourseInterpreter

    def setUp(self):
        self._courseInterpreter = CourseInterpreter()

    def test_get_all_values_from_content(self):
        sample_content = """
        [{
            "id": "id",
            "Eff_Date": "Eff_Date",
            "Acad_Group": "Acad_Group",
            "College_Name": "College_Name",
            "Acad_Org": "Acad_Org",
            "FormalDesc": "FormalDesc",
            "Subject": "Subject",
            "Catalog": "Catalog",
            "Course_id": "Course_id",
            "Long_Title": "Long_Title",
            "Min_Units": "Min_Units",
            "Max_Units": "Max_Units",
            "Component": "Component",
            "Designation": "Designation",
            "Descr": "Descr",
            "Status": "Status",
            "Sch_Print": "Sch_Print",
            "Cat_Print": "Cat_Print",
            "Rq_Group": "Rq_Group"
        }]
        """
        # print(sample_content)

        ret_course = self._courseInterpreter.interpretCourse(sample_content)[0]

        self.assertEqual(ret_course.id, 'id')
        self.assertEqual(ret_course.Eff_Date, 'Eff_Date')
        self.assertEqual(ret_course.Acad_Group, 'Acad_Group')
        self.assertEqual(ret_course.College_Name, 'College_Name')
        self.assertEqual(ret_course.Acad_Org, 'Acad_Org')
        self.assertEqual(ret_course.FormalDesc, 'FormalDesc')
        self.assertEqual(ret_course.Subject, 'Subject')
        self.assertEqual(ret_course.Catalog, 'Catalog')
        self.assertEqual(ret_course.Course_id, 'Course_id')
        self.assertEqual(ret_course.Long_Title, 'Long_Title')
        self.assertEqual(ret_course.Min_Units, 'Min_Units')
        self.assertEqual(ret_course.Max_Units, 'Max_Units')
        self.assertEqual(ret_course.Component, 'Component')
        self.assertEqual(ret_course.Designation, 'Designation')
        self.assertEqual(ret_course.Descr, 'Descr')
        self.assertEqual(ret_course.Status, 'Status')
        self.assertEqual(ret_course.Sch_Print, 'Sch_Print')
        self.assertEqual(ret_course.Cat_Print, 'Cat_Print')
        self.assertEqual(ret_course.Rq_Group, 'Rq_Group')


class CourseFormatterTestCase(unittest.TestCase):
    _courseFormatter: CourseFormatter

    def setUp(self):
        self._courseFormatter = CourseFormatter()

    def test_try_formatCourse(self):
        sample_courses = []

        sample_course = CourseData()
        sample_course.id = 'id'
        sample_course.Eff_Date = 'Eff_Date'
        sample_course.Acad_Group = 'Acad_Group'
        sample_course.College_Name = 'College_Name'
        sample_course.Acad_Org = 'Acad_Org'
        sample_course.FormalDesc = 'FormalDesc'
        sample_course.Subject = 'Subject'
        sample_course.Catalog = 'Catalog'
        sample_course.Course_id = 'Course_id'
        sample_course.Long_Title = 'Long_Title'
        sample_course.Min_Units = 'Min_Units'
        sample_course.Max_Units = 'Max_Units'
        sample_course.Component = 'Component'
        sample_course.Designation = 'Designation'
        sample_course.Descr = 'Descr'
        sample_course.Status = 'Status'
        sample_course.Sch_Print = 'Sch_Print'
        sample_course.Cat_Print = 'Cat_Print'
        sample_course.Rq_Group = 'Rq_Group'

        sample_courses.append(sample_course)
        self._courseFormatter.formatCourse(sample_courses)


if __name__ == '__main__':
    unittest.main()
