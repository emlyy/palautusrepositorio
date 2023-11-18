import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if user:
            raise UserInputError("Username taken")
        
        if len(username) < 3:
            raise UserInputError("Username should contain atleast 3 characters")
        
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username should only contain characters from a-z")
        
        if len(password) < 8:
            raise UserInputError("Password too short")

        if re.search(r'\d', password) is None:
            raise UserInputError("Password cannot contain only letters")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
