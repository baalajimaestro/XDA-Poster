#! /usr/bin/env python3
import json,requests,os
filename=os.environ.get("FILE",None)
XDA_API_KEY=os.environ.get("XDA_API_KEY",None)
XDA_THREAD_ID=os.environ.get("XDA_POST_ID",None)
with open(filename) as file:
  cl=file.read()
  cl+="This Post was sent from a Script by @baalajimaestro"
  data={"postid":XDA_POST_ID,"message":cl}
  headers = {'Content-type': 'application/json', 'Authorization': 'Bearer '+XDA_API_KEY}
r = requests.post('https://api.xda-developers.com/v3/posts/new', data=json.dumps(data), headers=headers)
print(r)
