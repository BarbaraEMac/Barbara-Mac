#!/usr/bin/python

import logging
import webapp2

from datetime import datetime
from time import mktime

from apps.emailreminder.models import EmailReminder
from util.parsedatetime import parsedatetime as pdt
from util.urihandler import admin_required, login_required, URIHandler

class ShowEmailIndex(URIHandler):

    @login_required
    @admin_required
    def get(self, user):
        template_values = { 'nickname' : user.nickname() }

        self.response.out.write(self.render_page('emailreminder.html', template_values))

class DoCreateEmailReminder(URIHandler):

    @login_required
    @admin_required
    def post(self, user):
        # Get varz
        subj = self.request.get( 'subject' )
        body = self.request.get( 'body' )
        date = self.request.get( 'date_str' )

        # Convert time
        c = pdt.Constants()
        c.BirthdayEpoch = 80    
        p = pdt.Calendar(c)
        val, result = p.parse( date )

        # Create Reminder
        er = EmailReminder( from_user = user,
                            to_addr   = user.email(),
                            subject   = subj,
                            body      = body,
                            send_date = datetime.fromtimestamp(mktime(val)) )
        er.put()

        self.redirect( '/email' )
