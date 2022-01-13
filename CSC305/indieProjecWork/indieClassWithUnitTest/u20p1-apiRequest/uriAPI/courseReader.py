import requests
import json
import configparser
import os


class CourseData:
    id = ''
    Eff_Date = ''
    Acad_Group = ''
    College_Name = ''
    Acad_Org = ''
    FormalDesc = ''
    Subject = ''
    Catalog = ''
    Course_id = ''
    Long_Title = ''
    Min_Units = ''
    Max_Units = ''
    Component = ''
    Designation = ''
    Descr = ''
    Status = ''
    Sch_Print = ''
    Cat_Print = ''
    Rq_Group = ''


class CourseRequester:
    def __init__(self):
        config = configparser.ConfigParser()
        ## look for the uri.ini file in this class's folder
        config.read(os.path.dirname(os.path.abspath(__file__)) + '/uri.ini')

        self._headers = {
            'id': config['uri.edu']['id']
        }

    def getCourse(self, deptCode, courseNum=None):
        if courseNum is not None:
            response = requests.get('https://api.uri.edu/v1/catalog/courses/' + deptCode + '/' + courseNum, headers=self._headers)
        else:
            response = requests.get('https://api.uri.edu/v1/catalog/courses/' + deptCode, headers=self._headers)
            
        if response.status_code != 200:
            raise ConnectionError("Connecting to the API returned response code: " + response.status_code.__str__())
        return response.content


class CourseInterpreter:
    def interpretCourse(self, content):
        responses = json.loads(content);
        courses = []
        for response in responses:
            course = CourseData()
            course.id = response['id']
            course.Eff_Date = response['Eff_Date']
            course.Acad_Group = response['Acad_Group']
            course.College_Name = response['College_Name']
            course.Acad_Org = response['Acad_Org']
            course.FormalDesc = response['FormalDesc']
            course.Subject = response['Subject']
            course.Catalog = response['Catalog']
            course.Course_id = response['Course_id']
            course.Long_Title = response['Long_Title']
            course.Min_Units = response['Min_Units']
            course.Max_Units = response['Max_Units']
            course.Component = response['Component']
            course.Designation = response['Designation']
            course.Descr = response['Descr']
            course.Status = response['Status']
            course.Sch_Print = response['Sch_Print']
            course.Cat_Print = response['Cat_Print']
            course.Rq_Group = response['Rq_Group']
            courses.append(course)
        return courses


class CourseFormatter:
    def formatCourse(self, courses):
        for course in courses:
            print("\t id: " + course.id)
            print("\t Eff_Date: " + course.Eff_Date)
            print("\t Acad_Group: " + course.Acad_Group)
            print("\t College_Name: " + course.College_Name)
            print("\t Acad_Org: " + course.Acad_Org)
            print("\t FormalDesc: " + course.FormalDesc)
            print("\t Subject: " + course.Subject)
            print("\t Catalog: " + course.Catalog)
            print("\t Course_id: " + course.Course_id)
            print("\t Long_Title: " + course.Long_Title)
            print("\t Min_Units: " + course.Min_Units)
            print("\t Max_Units: " + course.Max_Units)
            print("\t Component: " + course.Component)
            print("\t Designation: " + course.Designation)
            print("\t Descr: " + course.Descr)
            print("\t Status: " + course.Status)
            print("\t Sch_Print: " + course.Sch_Print)
            print("\t Cat_Print: " + course.Cat_Print)
            print("\t Rq_Group: " + course.Rq_Group)
            print("----------------------------------------")


class CourseFacade(object):
    def __init__(self) -> None:
        self.courseRequester = CourseRequester()
        self.courseInterpreter = CourseInterpreter()
        self.courseFormatter = CourseFormatter()

    def start(self, subject, courseNumber=None) -> None:
        try:
            if courseNumber is None:
                print("Requesting all courses in " + subject + ".")
            else:
                print("Requesting " + subject + " " + courseNumber + ".")
            response = self.courseRequester.getCourse(subject, courseNumber)
            try:
                print("Interpreting response.")
                data = self.courseInterpreter.interpretCourse(response)
                try:
                    print("Formatting data.")
                    self.courseFormatter.formatCourse(data)
                except Exception as err3:
                    print("Could not format data.", err3)
            except Exception as err2:
                print("Could not interpret response.", err2)
        except ConnectionError as err1:
            print("Could not retrieve response.", err1)
        print("----------------------------------------")
        print("----------------------------------------")


if __name__ == "__main__":
   courseFacade = CourseFacade()
   courseFacade.start('CSC', '305')
   courseFacade.start('CSC')

