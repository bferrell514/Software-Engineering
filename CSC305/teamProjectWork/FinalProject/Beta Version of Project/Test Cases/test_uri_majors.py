import unittest
from uri_majors import Major


class TestMajorList(unittest.TestCase):
    
    def test_CSC_BA_has_reqs(self):
        new_major = Major("CSC_BA")
        self.assertTrue(new_major.major_req, ["CSC 106", "CSC 110", "CSC 211", "CSC 212", "CSC 301", "CSC 305", "CSC 411", "CSC 402", "MTH 180", "MTH 131", " WRT 104", "WRT 201"])

    def test_CSC_BS_has_reqs(self):
        new_major = Major("CSC_BS")
        self.assertEqual(new_major.major_req,["CSC 106", "CSC110", "CSC 211", "CSC 212", "CSC 301", "CSC 305", "CSC 340", "CSC 411", "CSC 412", "CSC 440", "CSC 440", "CSC 449", "MTH 180", "MTH 141", "MTH 142", "WRT 201"])
    
    def test_DS_BS_has_reqs(self):
        new_major = Major("DS_BS")
        self.assertEqual(new_major.major_req,["MTH 141", "MTH 215", "STA 409", "CSC 201", "CSC 320", "STA 409", "MTH 142", "MTH 215", "CSC 310", "STA 305", "STA 441", "CSC 461", "BUS 456", "CSC 499"])

    def test_CPE_BS_has_reqs(self):
        new_major = Major("CPE_BS")
        self.assertEqual(new_major.major_req,["CHM 101","CHM 102", "ECN 201", "EGR 105", "MTH 141", "EGR 106", "MTH 142", "PHY 203", "PHY 273", 
        "ELE 201", "ELE 202", "ELE 208", "ELE 209", "MTH 244", "PHY 204", "PHY 274", 
        "CSC 211", "ELE 212", "ELE 215", "MTH 243",
        "CSC 212", "ELE 313", "ELE 338", "ELE 339", "MTH 215" "MTH 447", "CSC 447",
        "ELE 301", "ELE 302", "ELE 305", "MTH 451", 
        "ELE 400", "ELE 405", "ELE 406", "ELE 437", "ELE 480",
        "ELE 408", "ELE 409", "ELE 481"])
    
    def test_valid_major(self):
        new_major = Major("BIO")
        self.assertRaises(ValueError,new_major.major_req)

if __name__ == '__main__':
    unittest.main()

