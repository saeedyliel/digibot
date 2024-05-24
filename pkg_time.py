import time
from jdatetime import datetime
import random
import subprocess

print(time.time())

today=datetime.now().strftime("%H %M %S")

print(today)

username=["a","b","c"]
print(random.choice(username))

file=subprocess.run(['dir'],stdout=subprocess.PIPE,shell=True)
print(file.stdout)