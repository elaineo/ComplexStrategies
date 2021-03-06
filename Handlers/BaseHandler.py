import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader('templates'), autoescape = True)

class BaseHandler(webapp2.RequestHandler):
    """ BaseHandler, generic helper functions and user handling """
    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        """ render jinja tempalte """
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        """ render and write """
        if len(kw) == 0:
            self.write(self.render_str(template, **self.params))
        else:
            self.write(self.render_str(template, **kw))

    def initialize(self, *a, **kw):
        """ called every time """
        webapp2.RequestHandler.initialize(self, *a, **kw) 
        self.params = {} 