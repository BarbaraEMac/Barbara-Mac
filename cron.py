# Email Reminder App
# 
#

import os, logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template


####################################################################################
# Decorators
####################################################################################
def login_required( fn ):
    def check( self ):
        user = self.get_user( )
        if user:
            fn( self, user )
        else:
            # Go log in
            self.redirect( users.create_login_url( '/account' ) )
            return
    
    return check


################################################################################
# Handlers
################################################################################
class URIHandler( webapp.RequestHandler ):

    def __init__(self):
        # For simple caching purposes. Do not directly access this. Use self.get_user() instead.
        self.user = None

    def get_user(self):
        if self.user:
            return self.user

        # Get the Google session (not from the db)
        google_user = users.get_current_user()

        if google_user:
            # Now we get the user from the db
            self.user = User.get_or_create_by_google_user(google_user)

        return self.user    

    def render_page(self, template_file_name, content_template_values):
        """This re-renders the full page with the specified template."""

        main_path = os.path.join('templates/index.html')
        content_path = os.path.join('templates/' + template_file_name )

        user = self.get_user()

        content_values = {
            'user' : user
        }
        merged_content_values = dict(content_values)
        merged_content_values.update(content_template_values)

        content = template.render( content_path, merged_content_values )

       #/msgs = user.messages
       # msgs.reverse()

        show_messages = False
        #if len( user.messages ) != 0:
        #    if 'result' in template_file_name or 'account' in template_file_name or 'about' in template_file_name:
        #       show_messages = True
        #        user.messages = []
        #        user.put()

        template_values = {
            'CONTENT': content,
            'LOGOUT_URL' : users.create_logout_url('/'),
            'user' : user,
            'show_messages' : show_messages,
         #   'msgs' : msgs
        }
        merged_values = dict(template_values)
        merged_values.update(content_template_values)

        return template.render(main_path, merged_values)


### HTML Handlers
class MainHandler(webapp.RequestHandler):
    def get(self):
        
        path = os.path.join(os.path.dirname(__file__), 'static/index.html')
        self.response.out.write(template.render(path, []))

class EmailHandler(webapp.RequestHandler):
    def get(self):
        
        path = os.path.join(os.path.dirname(__file__), 'static/pages/email.html')
        self.response.out.write(template.render(path, []))



### Poor form, but cron job is here..
class CronChecker(webapp.RequestHandler):
    def post(self):
        logging.info("GOT A POST %r %s %s %s" % (self.request, self.request.get('timestamp'), self.request.get('referrer_id'), self.request.get('referree_id')))


def main():
    application = webapp.WSGIApplication([('/',           MainHandler), 
                                          ('/cron/check', CronChecker)],
                                          ('/email',      EmailHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
