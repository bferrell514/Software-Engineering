import hashlib
import os
from typing import Set, Tuple

from majors import Major


class User:
    """
    This class holds user information and is the type that the Database class expects to store.
    """
    def __init__(self, username: str, password: str, major: str, courses_taken=None):
        """
        :param username: the username of the user
        :param password: the plaintext password of the user to be hashed before storing
        :param major: the user's major.
        """
        if courses_taken is None:
            courses_taken = set()
        self.username = username
        # The plaintext password needs to be hashed before storing
        self.salt, self.key = self.encode_password(password)
        self.major: Major = Major(major)
        self.courses_taken = courses_taken

    def has_taken(self, completed_courses: Set[str]):
        """
        Called to add courses that the user has taken to the user's courses_taken field
        :param completed_courses: the set of courses the user has just completed that are
                                  not in their courses_taken currently
        """
        if self.courses_taken is None:
            # If the user has NOT taken courses prior to this, simply set it to the
            # the set of courses passed in
            self.courses_taken = completed_courses
        else:
            # If the user HAS taken courses prior to this, merge the two sets and store them
            self.courses_taken = self.courses_taken.union(completed_courses)

    def needs_to_take(self) -> Set[str]:
        """
        :return: The set of courses the user still needs to take.
        """
        if self.courses_taken is None:
            # The user has not finished any courses, so simply return the full list of requirements.
            return self.major.required_courses
        else:
            # Find the difference between the set of courses the user needs to take, and the set of courses
            # the user has taken and return it.
            return self.major.required_courses.difference(self.courses_taken)

    @staticmethod
    def encode_password(password: str) -> Tuple[bytes, bytes]:
        """
        Hashes the user's plaintext password.
        :param password: a plaintext password the user would like to use
        :return: a key and salt needed to check for a password's validity
        """
        salt = os.urandom(32)

        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000,
            dklen=128
        )

        return salt, key

    def authenticate(self, entered_password) -> bool:
        """
        Validates a given password and returns if the password was valid or not
        :param entered_password: the password the user is trying to log on with
        """
        verification_key = hashlib.pbkdf2_hmac(
            'sha256',
            entered_password.encode('utf-8'),
            self.salt,
            100000,
            dklen=128
        )

        if verification_key == self.key:
            return True
        else:
            return False
