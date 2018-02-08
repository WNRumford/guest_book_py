import json
from datetime import datetime
import time
    #эТО ОСНОВНОЙ КЛАСС
class Gbook:
    LOGIN = 'admin'
    PASSWORD = 'pass@word1'
    TMP_LOGFORM = 'gbook/logform.tmp'
    TMP_FORM = 'gbook/form.tmp'
    TMP_CONTENT = 'gbook/content.tmp'
    TMP_MESSAGE = 'gbook/message.tmp'
    DB = 'gbook/messages.json'
    
    def __init__(self):
        self.messages = ""
        self.form = ""
        self.content = ""
        self.logform = ""
        
        with open(self.TMP_FORM, "r", encoding="utf-8") as f:
            self.form = f.read()
            
        with open(self.TMP_CONTENT, "r", encoding="utf-8") as f:
            self.content = f.read()
        
        try:
            with open(self.DB, "r", encoding="utf-8") as f:
                pass
        except FileNotFoundError:
            with open(self.DB, "w", encoding="utf-8") as f:
                json.dump({}, f)
        
    
    def read_msgs(self):
        with open(self.DB, "r", encoding="utf-8") as f:
            m = json.load(f)
            if not m:
                self.messages = "There are no any posts!"
                return
            with open(self.TMP_MESSAGE, "r", encoding="utf-8") as f:
                pattern = f.read()
            for id in sorted(m.keys(), reverse=True):
                date = datetime.fromtimestamp(int(id)).strftime('%d-%m-%Y %H:%M')
                self.messages += pattern.format(msg=m[id]["msg"],
                                                datetime=date,
                                                name=m[id]["name"],
                                                email=m[id]["email"])
            
            
    
    def save_msg(self, name, email, msg):
        ts = int(time.time())
        with open(self.DB, "r", encoding="utf-8") as f:
            m = json.load(f)
        m[ts] = {"name":name, "email":email, "msg":msg}
        with open(self.DB, "w", encoding="utf-8") as f:
            json.dump(m, f)
        
    def delete_msg(self, id):
        pass
    
    def login(self, login, password):
        pass
    
    def logout(self):
        pass