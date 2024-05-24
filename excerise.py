import requests

for i in range(50):
    response=requests.get("https://wation.cloud/cyberdev/junior/http/body/"+str(i))  
    if(response.status_code==200):
        print(response.text)
        # print(i)