from format import msg_format
from datetime import datetime
import requests
import sys


def send(name, website=None):
    if website != None:
        msg = msg_format(name= name, website = website)
    else:
        msg = msg_format(name= name)
    r = requests.get("http://httpbin.org/json")
    if r.status_code==200:
        return r.json()
    else:
        return "There was an error"
    


send("Usama")