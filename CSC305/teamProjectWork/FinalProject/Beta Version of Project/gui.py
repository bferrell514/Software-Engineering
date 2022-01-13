from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from database import Database


class Gui:
    class WelcomeScreen:
        def __init__(self, gui):
            """
            Displays the welcome screen to the GUI.

            :param gui: The overall GUI object that controls everything.
            """
            self.gui = gui
            # Destroy the last screen
            self.gui.root.destroy()
            # Create a new screen
            self.gui.root = Tk()
            # Set the screens size
            self.gui.root.geometry(self.gui.window_size)

            self.gui.root.title("URI Automated Class Schedule Generator")
            self.gui.root['bg'] = self.gui.background_color

            # Create the Welcome header
            header = Label(self.gui.root, text="Welcome", font=("Arial Bold", 36), bg=self.gui.background_color)
            header.pack(side="top")
            # Import and display the URI logo.
            logo_file = Image.open("gui/media/uri_logo.png")
            logo_file = logo_file.resize((300, 300), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(logo_file)
            logo = Label(image=render)
            logo.place(x=300, y=300, anchor="center")

            self.gui.root.mainloop()

    class CreateUserScreen:
        def __init__(self, gui):
            """
            Displays the screen to create a new user account to the GUI.

            :param gui: The overall GUI object that controls everything.
            """
            self.gui = gui
            # Destroy the last screen
            self.gui.root.destroy()
            # Create a new screen
            self.gui.root = Tk()
            # Set the screens size
            self.gui.root.geometry(self.gui.window_size)
            # Create the field "username"
            Label(text=' Choose a username ', font='Times 15').grid(row=1, column=1, pady=20)
            self.username = Entry()
            self.username.grid(row=1, column=2, columnspan=10)
            # Create the field "password"
            Label(text=' Choose a password ', font='Times 15').grid(row=2, column=1, pady=20)
            self.password = Entry(show='*')
            self.password.grid(row=2, column=2, columnspan=10)
            # Create the field "major"
            Label(text=' Enter your major ', font='Times 15').grid(row=3, column=1, pady=20)
            self.major = Entry()
            self.major.grid(row=3, column=2, columnspan=10)
            # Create the submit button which will call the create_user function to enter the user in the database
            ttk.Button(
                text='Submit',
                command=self.attempt_to_create_user
            ).grid(row=4, column=2)

        def attempt_to_create_user(self):
            self.gui.database.add_user(self.username.get(), self.password.get(), self.major.get())
            self.gui.WelcomeScreen(self.gui)

    class LoginScreen:
        def __init__(self, gui):
            """
            Displays the screen to login an existing user account to the GUI.

            :param gui: The overall GUI object that controls everything.
            """
            self.gui = gui
            # Destroy the last screen
            self.gui.root.destroy()
            # Create a new screen
            self.gui.root = Tk()
            # Set the screens size
            self.gui.root.geometry(self.gui.window_size)
            # Create the field "username"
            Label(text=' Username ', font='Times 15').grid(row=1, column=1, pady=20)
            self.username = Entry()
            self.username.grid(row=1, column=2, columnspan=10)
            # Create the field "password"
            Label(text=' Password ', font='Times 15').grid(row=2, column=1, pady=20)
            self.password = Entry(show='*')
            self.password.grid(row=2, column=2, columnspan=10)
            # Create the "login" button
            ttk.Button(
                text='Login',
                command=self.attempt_login
            ).grid(row=3, column=2, pady=20)
            # Create the "Create an account" button in case the user does not have an account
            ttk.Button(text='Create an account', command=lambda: self.gui.CreateUserScreen(self.gui)) \
                .grid(row=7, column=2)

        def attempt_login(self):
            user = self.gui.database.login_user(self.username.get(), self.password.get())
            if user is None:
                raise ValueError
            else:
                # Password was valid
                self.gui.WelcomeScreen(self.gui)

    def __init__(self):
        """
        Initializes the GUI for the schedule generator. There are a number of
        sub classes which are the possible screens that the GUI has.
        """
        self.background_color = '#7aa3cc'
        self.window_size = '600x600'
        self.root = Tk()
        self.root.geometry(self.window_size)
        self.database = Database()

        if not self.database.users:
            self.CreateUserScreen(self)
        else:
            self.LoginScreen(self)

        self.root.mainloop()


# Test code
gui = Gui()
