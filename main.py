import webapp2
import logging
# step 1 import jinja and os
import jinja2
import os

# step 2: set up jinja environment
env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/start.html")
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug = True)
