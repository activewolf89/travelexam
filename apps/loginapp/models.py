from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  =   re.compile(r'^[a-zA-Z]')

class UserInput(models.Manager):


    def input(self, DataPost):
        count = 0
        dictionary = {}
        if not NAME_REGEX.match(DataPost['first_name_registration']):
            dictionary['error1'] = "first name contains errors"
            dictionary['outcome'] = 'fail'
            count = 1

        if not len(DataPost['first_name_registration']) >= 2:
            dictionary['error2'] = "first name cant be less than 2"
            dictionary['outcome'] = 'fail'
            count = 1
        if not NAME_REGEX.match(DataPost['last_name_registration']):
            dictionary['error3'] = "last name contains errors"
            dictionary['outcome'] = 'fail'
            count = 1
        if not len(DataPost['last_name_registration']) >= 2:
            dictionary['error4'] = "last name cant be less than 2"
            dictionary['outcome'] = 'fail'
            count = 1
        if not EMAIL_REGEX.match(DataPost['email_registration']):
            dictionary['error5'] = "email contains errors"
            dictionary['outcome'] = 'fail'
            count = 1
        if not len(DataPost['password_registration']) >= 8:
            dictionary['error6'] = "password is less than 8"
            dictionary['outcome'] = 'fail'
            count = 1
        if not DataPost['password_registration'] == DataPost['confirm_password_registration']:
            dictionary['error7'] = "password does not match confirm password"
            dictionary['outcome'] = 'fail'
            count = 1
        if self.filter(email__iexact = DataPost['email_registration']):
            dictionary['error8'] = "email is already in use"
            dictionary['outcome'] = 'fail'

            count = 1
        if count != 1:
            hashed_password = bcrypt.hashpw(DataPost['password_registration'].encode(), bcrypt.gensalt())
            user = self.create(first_name = DataPost['first_name_registration'], last_name = DataPost['last_name_registration'], email = DataPost['email_registration'], password = hashed_password)
            dictionary['outcome'] = 'success'
            user = self.filter(email = DataPost['email_registration'])
            dictionary['user'] = user[0]
        return dictionary
    def input2(self, DataPost2):
        modelResponse = {}
        user = self.filter(email__iexact = DataPost2['email_login'])

        if user:
            if bcrypt.checkpw(DataPost2['password_login'].encode(), user[0].password.encode()):

                modelResponse['status'] = True
                modelResponse['user'] = user[0]
            else:
                modelResponse['status'] = False
                modelResponse['error'] = 'Invalid email/password combination'
        else:
            modelResponse['status'] = False
            modelResponse['error'] = 'Invalid email'

        return modelResponse

class Registration(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    objects = UserInput()
