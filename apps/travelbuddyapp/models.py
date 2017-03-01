from __future__ import unicode_literals

from django.db import models
from ..loginapp.models import Registration
from datetime import datetime
class Manager(models.Manager):
    def add_destination(self, DataPost, user):
        Response = {'outcome':'success'}

        if not DataPost['destination']:
            Response['outcome'] = "fail"
            Response['answer'] = "No blanks on destination! Also congrats on getting through the required"
        if not DataPost['description']:
            Response['outcome'] = "fail"
            Response['answer1'] = "No blanks on description! Also congrats on getting through the required"
        if not DataPost['datefrom']:
            Response['outcome'] = "fail"
            Response['answer2'] = "No blanks on datefrom! Also congrats on getting through the required"
        if not DataPost['dateto']:
            Response['outcome'] = "fail"
            Response['answer3'] = "No blanks on dateto! Also congrats on getting through the required"
        if DataPost['datefrom'] > DataPost['dateto']:
            Response['outcome'] = "fail"
            Response['answer4'] = "Cannot Travel To before From!"
        if DataPost['dateto'] < datetime.now().strftime('%Y-%m-%d %H:%M:%S'):
            Response['outcome'] = "fail"
            Response['answer5'] = "Cannot set up a dateto back in time"
        if DataPost['datefrom'] < datetime.now().strftime('%Y-%m-%d %H:%M:%S'):
            Response['outcome'] = "fail"
            Response['answer6'] = "Cannot set up a datefrom back in time"

        if Response['outcome'] != 'success':
            return Response
        else:
            user_object = Registration.objects.get(id = user)
            travel_object = Travel.objects.create(destination = DataPost['destination'], description = DataPost['description'], date_from = DataPost['datefrom'], date_to = DataPost['dateto'], creator = user_object)
            travel_object.traveller.add(user_object)

            Response['outcome'] = "success"

            return Response

    def update_destination(self, destination_id, user_id):
        user_object = Registration.objects.get(id = user_id)
        destination_object = Travel.objects.get(id = destination_id)
        destination_object.traveller.add(user_object)

        Response = {'outcome': 'success'}
        print "got to the add_destination"

        return Response



class Travel(models.Model):
    destination = models.CharField(max_length = 45)
    description = models.CharField(max_length = 255)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    traveller = models.ManyToManyField(Registration, related_name = 'travellersoftrip')
    creator = models.ForeignKey(Registration, related_name = 'creatoroftrip')
    objects = Manager()
