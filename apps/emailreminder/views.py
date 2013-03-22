#!/usr/bin/python

import logging
import webapp2

from util.urihandler import admin_required, login_required, URIHandler


class ShowEmailIndex(URIHandler):

    @login_required
    @admin_required
    def get(self, user):
        template_values = { 'nickname' : user.nickname() }

        self.response.out.write(self.render_page('emailreminder.html', template_values))
