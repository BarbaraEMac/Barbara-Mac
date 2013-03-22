#!/usr/bin/python

import logging

import webapp2

from util.urihandler import URIHandler

class ShowEmailIndex(URIHandler):
    def get(self):
        template_values = { }

        self.response.out.write(self.render_page('emailreminder.html', template_values))
