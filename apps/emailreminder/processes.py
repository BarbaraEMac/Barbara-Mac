#!/usr/bin/env python

import logging, webapp2
from datetime import datetime

from apps.emailreminder.models import EmailReminder
from google.appengine.api import taskqueue

class CronCheckAndSend( webapp2.RequestHandler ):
    def get(self):
        reminders = EmailReminder.all().filter( 'sent =', False ).filter( 'send_date <=', datetime.today() )
        
        for er in reminders:
            taskqueue.add( url    = '/email/queue/sendEmail',
                           params = {'key' : er.key()} )
        
class QueueSendEmail( webapp2.RequestHandler ):
    def post( self ):
        er = EmailReminder.get( self.request.get('key') )

        er.send()
