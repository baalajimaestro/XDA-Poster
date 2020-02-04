#! /usr/bin/env python3
#
# Copyright © 2019 Maestro Creativescape
#
# SPDX-License-Identifier: GPL-3.0
#

import json, requests, os
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk import capture_exception

sentry_sdk.init("https://8a6cee16d17a43ec916bafc296b61110@sentry.io/2240523")

try:
    load_dotenv("config.env")

    filename=os.environ.get("FILE",None)
    XDA_API_KEY=os.environ.get("XDA_API_KEY",None)
    XDA_THREAD_ID=os.environ.get("XDA_THREAD_ID",None)
    r = requests.get("https://api.xda-developers.com/v3/posts",params={"threadid":XDA_THREAD_ID})
    XDA_POST_ID=r.json()["results"][0]["postid"]
    with open(filename) as file:
        cl=file.read()
        cl+="\n\nThis Post was sent from a XDA-Poster Script by @baalajimaestro"
        data={"postid":XDA_POST_ID,"message":cl}
        headers = {'Content-type': 'application/json', 'Authorization': 'Bearer '+XDA_API_KEY}
    r = requests.post('https://api.xda-developers.com/v3/posts/new', data=json.dumps(data), headers=headers)

except BaseException as e:
    x = capture_exception(e)
    msg="Posting to XDA Failed!\n" \
        "The developer was notified.\n" \
        "Error: "+str(type(e).__name__) + "\n" \
        "Error ID: "  + x
    print(msg)
