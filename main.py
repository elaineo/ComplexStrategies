import webapp2
import sys

from Handlers.BaseHandler import *

from Pages.HomePage import *
#add json for android app
app = webapp2.WSGIApplication([('/', HomePage),
                                ('/about', AboutPage),
                                ('/investor', InvestorPage),
                            ('/generate', Generator)],
  debug=True)