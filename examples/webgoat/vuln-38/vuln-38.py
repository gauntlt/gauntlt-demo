import urllib2 
import urllib
import cookielib
import re

def write_f_to_f(fname,f):
    f1 = open(fname,"w")
    f1.write(f.read())
    f1.close()

def gen_req(url,referer=None):
    req = urllib2.Request(url)
    return req



myjar = cookielib.FileCookieJar("cookies.txt");
cookieHandler = urllib2.HTTPCookieProcessor(myjar)

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
tlurl="http://127.0.0.1:8081/webgoat/attack"

password_mgr.add_password(None,tlurl,user="guest",passwd="guest")
find = "Blind Numeric."

authhandler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(authhandler,cookieHandler)

url = "http://127.0.0.1:8081/webgoat/attack"
req = gen_req(url,url)
f = opener.open(req)# Setup session and login.

params = urllib.urlencode({'start':'Start WebGoat'})
url = "http://127.0.0.1:8081/webgoat/attack"
req = gen_req(url,url)
f = opener.open(req,params) # Submit the "Start" form
dat = f.read() # Get the menu html from the firstpage.
f.close()


m = re.search("attack\?Screen=(\d+).*%s"%find,dat) # Try to find screen id for what i want
if not m is None:
    scr= m.group(1)
    qs = urllib.urlencode( {'Screen':scr, 'menu':1200 } )
    ourl = url
    url = "http://127.0.0.1:8081/webgoat/attack?%s"%qs
    req = gen_req(url,ourl)
    f = opener.open(req)
    write_f_to_f("f4.html",f)
    f.close()
    print "Found the page and saved it to f4.html"
else:
    print "Didnt find screen id for %s"%find
