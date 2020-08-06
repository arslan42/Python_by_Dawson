#demonstrate modules creation
class Player(object):
    """game member"""
    def __init__(self,name,score=0):
        self.name=name
        self.score=score
    def __str__(self):
        rep=self.name+":\t"+str(self.score)
        return rep

def ask_yes_no(question):
    """Asks a question"""
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response

def ask_number(question,low,high):
    """Asks input number from interval"""
    response=None
    while response not in range(low,high):
        response=int(input(question))
    return response

if __name__=="__main__":
    print("You loaded this module straight, not imported")
    input("\n\nPress enter to exit")
