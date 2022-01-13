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

    def getCourse(self, deptCode, courseNum):
        response = requests.get('https://api.uri.edu/v1/catalog/courses/' + deptCode + '/' + courseNum, headers=self._headers)
        if response.status_code != 200:
            raise ConnectionError("Connecting to the API returned response code: " + response.status_code.__str__())
        return response.content

class CourseInterpreter:
    def interpretCourse(self, content):
        course = CourseData()
        response = json.loads(content)[0]
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
        return course

class CourseFormatter:
    def formatCourse(self, data):
        print("\t id: " + data.id)
        print("\t Eff_Date: " + data.Eff_Date)
        print("\t Acad_Group: " + data.Acad_Group)
        print("\t College_Name: " + data.College_Name)
        print("\t Acad_Org: " + data.Acad_Org)
        print("\t FormalDesc: " + data.FormalDesc)
        print("\t Subject: " + data.Subject)
        print("\t Catalog: " + data.Catalog)
        print("\t Course_id: " + data.Course_id)
        print("\t Long_Title: " + data.Long_Title)
        print("\t Min_Units: " + data.Min_Units)
        print("\t Max_Units: " + data.Max_Units)
        print("\t Component: " + data.Component)
        print("\t Designation: " + data.Designation)
        print("\t Descr: " + data.Descr)
        print("\t Status: " + data.Status)
        print("\t Sch_Print: " + data.Sch_Print)
        print("\t Cat_Print: " + data.Cat_Print)
        print("\t Rq_Group: " + data.Rq_Group)

if __name__ == "__main__":
    courseRequester = CourseRequester()
    courseInterpreter = CourseInterpreter()
    courseFormatter = CourseFormatter()
    try:
        subject = 'CSC'
        courseNumber = '305'
        print("Requesting " + subject + " " + courseNumber + ".")
        response = courseRequester.getCourse('CSC','305')
        try:
            print("Interpreting response.")
            data = courseInterpreter.interpretCourse(response)
            try:
                print("Formatting data.")
                courseFormatter.formatCourse(data)
            except Exception as err3:
                print("Could not format data.", err3)
        except Exception as err2:
            print("Could not interpret response.", err2)
    except ConnectionError as err1:
        print("Could not retrieve response.", err1)