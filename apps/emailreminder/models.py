import os
import logging

from datetime import datetime, date, timedelta

from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.api.mail import EmailMessage
from google.appengine.ext import db

class EmailReminder( db.Model ):
    from_user = db.UserProperty( indexed = False)

    to_addr   = db.EmailProperty( indexed = False )
    subject   = db.StringProperty( indexed = False)
    body      = db.TextProperty( indexed = False )

    send_date = db.DateTimeProperty( indexed = True )
    sent      = db.BooleanProperty( indexed = True, default = False )

    def __init__(self, *args, **kwargs):
        super(EmailReminder, self).__init__(*args, **kwargs)

    def send( self ):
        # Add a check that it can only send on the date it's suppsoed to?
        
        e = EmailMessage( sender  = self.from_user.email(), 
                          to      = self.to_addr,
                          subject = self.subject, 
                          html    = self.body )
        e.send()

        self.sent = True
        self.put()
