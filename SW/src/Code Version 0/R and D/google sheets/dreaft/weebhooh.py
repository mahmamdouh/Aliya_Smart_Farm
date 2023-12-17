import datetime
import psutil
import requests

data_to_send = {}
data_to_send["date"] = str(datetime.datetime.now())
data_to_send["temp"] = str(50)


print(str(data_to_send))

r = requests.post("https://hook.integromat.com/byofh7ubmvs4ejkdlmojita0nh5eacwl", data= str(data_to_send))

print(r.status_code)