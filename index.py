#!/usr/bin/env python3

from _gbook import Gbook
from cgi import FieldStorage
from http import cookies
import os
import html

gbook = Gbook()

params = FieldStorage()

admin = False

if "HTTP_COOKIE" in os.environ:
    cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE")).get("admin")
    if cookie is not None:
        admin = True

if os.environ.get("REQUEST_METHOD") == "POST":
    operation = params.getvalue("operation", "")
    if operation == "post":
        name = html.escape(params.getvalue("name"))
        email = html.escape(params.getvalue("email"))
        msg = html.escape(params.getvalue("msg"))
        gbook.save_msg(name, email, msg)
    elif operation == "login":
        login = html.escape(params.getvalue("login"))
        password = html.escape(params.getvalue("password"))
        admin = gbook.login(login, password)
    elif operation == "logout":
        gbook.logout()
        admin = False

if 'del' in params:
    id = int(params.getvalue('del'))
    if id:
        gbook.delete_msg(str(id))

gbook.read_msgs(admin)

######################################################

print("Content-Type: text/html;charset=utf-8")
print()
print(gbook.content.format(logform=gbook.logform, 
                          form=gbook.form,
                          messages=gbook.messages))