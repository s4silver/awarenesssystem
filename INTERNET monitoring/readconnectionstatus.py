import urllib2

def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com',timeout=2)
        return True
    except:
        return False

status = internet_on()
print status
