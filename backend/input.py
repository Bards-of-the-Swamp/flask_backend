import requests
import json

separator = ","
prompt = input("Enter grocery foods separated by commas: ")
lst = prompt.split(separator)

url = "https://flask-backend2-doabvle5va-uk.a.run.app/process_strings"
obj = {"string_list": lst}

x = requests.post(url, json= obj)
str = json.dumps(x.json(), indent=2)


print(str)
