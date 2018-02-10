class Gbook:
    LOGIN = "admin"
    PASSWORD = "pass@word1"
    TMP_LOGFORM = "gbook/logform.tmp"
    TMP_FORM = "gbook/form.tmp"
    TMP_CONTENT = "gbook/content.tmp"
    TMP_MESSAGE = "gbook/message.tmp"
    DB = "gbook/messages.json"
    
    def __init__(self):
        self.messages = ""
        self.form = ""
        self.content = ""
        self.logform = ""
        
    def read_msgs(self):
        pass
    
    def save_msg(self, name, email, msg):
        pass
    
    def delete_msg(self, id):
        pass
    
    def login(self, login, password):
        pass
    
    def logout(self):
        pass