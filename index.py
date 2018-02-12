#!/usr/bin/env python3

from _gbook import Gbook
from cgi import FieldStorage
import os
import html

gbook = Gbook()

params = FieldStorage()

if os.environ.get("REQUEST_METHOD") == "POST":
    operation = params.getvalue("operation", "")
    if operation == "post":
        name = html.escape(params.getvalue("name"))
        email = html.escape(params.getvalue("email"))
        msg = html.escape(params.getvalue("msg"))
        gbook.save_msg(name, email, msg)

print("Content-Type: text/html;charset=utf-8")
print()

gbook.read_msgs()
print(gbook.content.format(logform=gbook.logform, 
                          form=gbook.form,
                          messages=gbook.messages))