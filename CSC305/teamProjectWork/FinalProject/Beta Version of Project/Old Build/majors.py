'''
NOTES
---------------------------------
testTestTest #camelCase
Test_test_test # snake_case

Hard coded list of majors for proof of concept

Majors:
- Computer Science B.A
- Computer Science B.S
- Data Science B.S
- Computer Engineering
'''

import re

class Major:
    def CSC_BA(self):
        return {
            "CSC 106", "CSC 110", "CSC 211", "CSC 212", "CSC 301", "CSC 305", "CSC 411", "CSC 402", "MTH 180",
            "MTH 131", " WRT 104", "WRT 201"
        }

    def CSC_BS(self):
        return {
            "CSC 106", "CSC110", "CSC 211", "CSC 212", "CSC 301", "CSC 305", "CSC 340", "CSC 411", "CSC 412",
            "CSC 440", "CSC 440", "CSC 449", "MTH 180", "MTH 141", "MTH 142", "WRT 201"
        }

    def DS_BS(self):
        return {
            "MTH 141", "MTH 215", "STA 409", "CSC 201", "CSC 320", "STA 409", "MTH 142", "MTH 215", "CSC 310",
            "STA 305", "STA 441", "CSC 461", "BUS 456", "CSC 499"
        }

    def CPE_BS(self):
        return {
            "CHM 101", "CHM 102", "ECN 201", "EGR 105", "MTH 141", "EGR 106", "MTH 142", "PHY 203", "PHY 273",
            "ELE 201", "ELE 202", "ELE 208", "ELE 209", "MTH 244", "PHY 204", "PHY 274",
            "CSC 211", "ELE 212", "ELE 215", "MTH 243",
            "CSC 212", "ELE 313", "ELE 338", "ELE 339", "MTH 215", "MTH 447", "CSC 447",
            "ELE 301", "ELE 302", "ELE 305", "MTH 451",
            "ELE 400", "ELE 405", "ELE 406", "ELE 437", "ELE 480",
            "ELE 408", "ELE 409", "ELE 481"
        }

    def __init__(self, major_title: str):
        self.required_courses = []

        if major_title == "CSC BA":
            self.required_courses = self.CSC_BA()
        elif major_title == "CSC BS":
            self.required_courses = self.CSC_BS()
        elif major_title == "DS BS":
            self.required_courses = self.DS_BS()
        elif major_title == "CPE BS":
            self.required_courses = self.CPE_BS()
        else:
            raise Exception("Not a valid Major")

def listCourses(pre_text):
    pieces = re.findall(r"\b([A-Z]{3}|[0-9]{3})\b", pre_text)
    currentDepartment = None
    prerequisites = []

    for item in pieces:
        if item.isdigit():
            if currentDepartment is None:
                raise ValueError
            # you should have a more useful data type to instantiate here:
            prerequisites.append(currentDepartment + " " + item)
        else:
            currentDepartment = item
    return prerequisites
