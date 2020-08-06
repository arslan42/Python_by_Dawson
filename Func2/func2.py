#demonstrate parameters and returns
def display(message):
    print(message)
def give_me_five():
    five=5
    return five
def ask_yes_no(question):
    """Asks question with answer yes or no."""
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response
#main part
display("Here is message.\n")
number=give_me_five()
print("This is what function give_me_five() has returned: ",number)
answer=ask_yes_no("\nplease type y or n: ")
print("Thanks for type ", answer)
input("\n\npress enter to exit")
