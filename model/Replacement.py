
class Replacement:

    def __init__(self,match):
        self.offset = match.offset
        self.error_length = match.errorlength
        self.msg = match.msg
        self.replacements = match.replacements
        self.issue_type = match.locqualityissuetype
        self.category = match.category


    def to_dict(self):
        dict = {
            "msg": self.msg,
            "replacements": self.replacements,
            "offset": self.offset,
            "error_length": self.error_length,
            "category": self.category,
            "issue_type":self.issue_type
        }
        return dict

    def print_details(self):

        print(f'msg: {self.msg}')
        print(f'replacements: {self.replacements}')
        print(f'offset: {self.offset}')
        print(f'error length: {self.error_length}')
        print(f'category: {self.category}')
        print()