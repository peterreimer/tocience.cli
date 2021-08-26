#!/usr/bin/env python3
import requests
import urllib.parse


user = "lschruff"
password = "<top-secret>"

# private
path = "/".join(("resource", "frl:6426929.json2"))

# public
# path = "/".join(("resource", "frl:6425464.json2"))

url = urllib.parse.urlunparse(("https", "frl.publisso.de" , path, "", "", ""))
print(url)

auth = (user, password)

r = requests.get(url, auth=auth)
#r = requests.get(url)
print(r.status_code)
print(r.text)

