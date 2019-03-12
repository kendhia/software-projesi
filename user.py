
class User:
    user_name = ""
    
    def get_name(self):
        return self.user_name

    def add_name(self, name_str):
        self.user_name = name_str
        