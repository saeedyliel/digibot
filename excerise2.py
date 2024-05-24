import requests

for i in range(100,151):
    print(i)
    response=requests.get("https://wation.cloud/cyberdev/junior/http/header/"+str(i))  
    if "WationSecret" in response.headers:
        print(response.headers['WationSecret'])

        # print(i)sss