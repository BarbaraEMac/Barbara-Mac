#!/usr/bin/python

import inspect
import jinja2
import logging
import os
import webapp2

from google.appengine.api import users
from util.consts          import *

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

################################################################################
# Decorators
################################################################################
def login_required( fn ):
    def check( self ):
        user = self.get_user( )
        logging.info("USER: +" + str(fn))
        if user:
            fn( self, user )
        else:
            # Go log in
            self.redirect( users.create_login_url( '/email' ) )
            return
    
    return check

def admin_required( fn ):
    def check( self, user ):
        if user and (user.email() in ADMIN_EMAILS):
            fn( self, user )
        else:
            # Go log in
            self.redirect( users.create_login_url( '/email' ) )
            return
    
    return check

################################################################################
# URIHandler Class
################################################################################
class URIHandler( webapp2.RequestHandler ):

    def __init__(self, *args, **kwargs):
        super(URIHandler, self).__init__(*args, **kwargs)
        
        # For simple caching purposes. Do not directly access this. 
        # Use self.get_user() instead.
        self.user = None

    # Return None if not authenticated.
    # Otherwise return db instance of user.
    def get_user(self):
        if self.user:
            return self.user

        return users.get_current_user()   

    def render_page(self, template_file_name, template_values):
        """This re-renders the full page with the specified template."""
        user = self.get_user()

        # Merge default values + page-specific values
        default_template_values = {
            'URL'  : URL,
            'user' : user
        }
        final_values = dict(default_template_values)
        final_values.update(template_values)
        
        # Get path to template file within apps dir
        path = os.path.join('templates/', template_file_name)
        path = os.path.join(self.get_app_path() , path)
        logging.info("Rendering %s" % path )

        return jinja_environment.get_template(path).render(final_values) 

    def get_app_path(self):
        module = inspect.getmodule(self).__name__
        parts = module.split('.')
        app_path = None 
        
        if len(parts) > 2:
            if parts[0] == 'apps':
                # we have an app
                app_path = '/'.join(parts[:-1])

        return app_path
