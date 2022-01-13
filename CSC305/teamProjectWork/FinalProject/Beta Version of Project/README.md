# URI eCampus Schedule Maker
# CSC305 - Team 1
# Sean Creamer, Baheem Ferrell, Brian Hopkins, Paul Perry

Necessary Steps to Run the Program
---

1) Tkinter

To operate the software, you must have the python framework, Tkinter, installed. Tkinter runs the GUI, so without it, the GUI will not work.

Instructions to install Tkinter can be found here: 
https://tkdocs.com/tutorial/install.html

2) Selenium

To use the webscraping file, you will need to install Selenium. Selenium is the python library that scrapes data off of web pages.

Instructions to install Selenium can be found here:
https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/#:~:text=Kotlin-,Installing%20Selenium%20libraries,language%20you%20choose%20to%20use.

You will also have to update the __init__ method of the CourseSearch class in the webscrape.py file. The line in question is line 34 and reads: PATH = r"D:\Selenium_webDriver\chromedriver.exe". This assumes you have the Google Chrome browser installed. It also assumes you have a D:\ drive, so you will have to update that information to whatever location you use on your local environment.

Instructions to download and install Google Chrome can be found here:
https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en

To get information scrapped from other classes, you must change lines 84, 85, and 88.  Currently, they read "CSC 305" and "CSC 301". In order to pull whatever course you want, you must change each instance to whatever course you want. You must keep the same format (space in the middle).

If you're interested in add more than two classes, you must copy/paste the for loop on lines 85-86 or 88-89 and add it to the bottom of the file. Then replace the course to whatever course you want. Then the last step is to also add that new course to the set on line 84.