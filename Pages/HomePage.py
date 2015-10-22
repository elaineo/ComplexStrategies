import random
from Handlers.BaseHandler import *
from stringdefs import *
import urllib2

from google.appengine.api import mail

class HomePage(BaseHandler):
    """ Home page, first page shown """
    def get(self):
        self.render('home.html', **self.params)
        
class AboutPage(BaseHandler):
    """ About page """
    def get(self):
        self.render('about.html', **self.params)
                
class InvestorPage(BaseHandler):
    def get(self):
        self.render('invest.html', **self.params)
          
    def post(self):
        msg = self.request.get('message')
        subject = self.request.get('subject')
        email = self.request.get('email')
        name = self.request.get('name')
        remoteip = self.request.remote_addr
        self.send_message(msg,subject,email,name,remoteip)
        self.render('thanks.html')

    def send_message(self,msg,subject,email,name,remoteip):
        if not name:
            name = "Complex Strategies"
        if not subject:
            subject = "Feedback"
        text = u'From: %s (%s)' % (name, email)
        text += u'\n' + ('-' * len(text)) + '\n\n' + msg + '\n\n' + remoteip
        mail.send_mail('elaine.ou@gmail.com','elaine.ou@gmail.com', subject=subject, body=text)
        
class Generator(BaseHandler):
    # verb [adj noun1] or noun2, 'using' using 'to' to noun3, and then ...
    def get(self):
        output=''
        j=0
        while j<2:
            v = random.choice(verbs)+' '
            if j==0:
                v=v.capitalize()
            output=output+v
            if (random.randint(0,1)>0):
                output=output+random.choice(adjs)+' '+random.choice(nouns1)
            else:
                output=output+random.choice(nouns2)
            output=output+' using '+random.choice(using)+' to '
            output=output+random.choice(to)+' '
            output=output+random.choice(nouns3)
            j=j+1
            if j<2:
                output=output + ', and then '
        output=output+'.'
        self.write(output)