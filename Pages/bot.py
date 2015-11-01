import random
from TwitterAPI import TwitterAPI
from stringdefs import *
from apscheduler.scheduler import Scheduler

CONSUMER_KEY = 'JLsalg6kGNWR3L9vdYg5ZesOW'
CONSUMER_SECRET = '27xVJ8jDVuCvZz1jyxqIfFgbXv0GDD6q7axJJheQYbXFAnZUDn'
ACCESS_TOKEN = '3269501892-QeI4ToFqAPG2YeGumqPtKSwPhZrKL32uuUWAhxD'
ACCESS_TOKEN_SECRET = 'uPq8hEHegCxx64w8RLsHJ2KnVhPG4ezC2nJ7xWmOfqxkI'

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
sched = Scheduler()

@sched.interval_schedule(hours=1)
def gen_tweet():
    if (random.randint(0,10)>2):
        return
    output=''
    v = random.choice(verbs)+' '
    v=v.capitalize()
    output=output+v
    if (random.randint(0,1)>0):
        output=output+random.choice(adjs)+' '+random.choice(nouns1)
    else:
        output=output+random.choice(nouns2)
    output=output+' using '+random.choice(using)+' to '
    output=output+random.choice(to)+' '
    output=output+random.choice(nouns3)
    output=output+'.'
    twit = api.request('statuses/update', {'status': output})


#sched.configure(options_from_ini_file)
sched.start()