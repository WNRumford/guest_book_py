#!/usr/bin/env python3

from _gbook import Gbook

print("Content-Type: text/html;charset=utf-8")
print()

gbook = Gbook()
print(gbook.content.format(logform=gbook.logform, 
                          form=gbook.form,
                          messages=gbook.messages))