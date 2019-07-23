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


# First options

class RunHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/run.html")
        self.response.write(template.render())

# options after run

class FasterHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/faster.html")
        self.response.write(template.render())

class OstrichHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates")



# ----------------------


class JumpHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/jump.html")
        self.response.write(template.render())

# options after jump





# ----------------------
class GriffinHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/griffin.html")
        self.response.write(template.render())

#options after griffin



# -----------------------

class CallHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/call.html")
        self.response.write(template.render())

#options after call









app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/run', RunHandler),
    ('/jump', JumpHandler),
    ('/griffin', GriffinHandler)
    ('/call', CallHandler)
], debug = True)
