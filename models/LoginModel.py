from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, validators
from flaskTest.services.Services import UserService


class LoginModel(Form):
    Username = StringField('Username',
                           [validators.Length(min=4, max=20, message='Username should have between 4 and 20 chars')])
    Password = PasswordField('Password',
                             [validators.Length(min=4, max=50, message='Password should have between 4 and 50 chars')])
    RememberMe = BooleanField('Remember')

    def validateCredentials(self):
        return UserService().validate(self.Username.data, self.Password.data)