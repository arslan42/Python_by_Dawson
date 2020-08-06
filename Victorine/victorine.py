#VIctorine
#quetions read from file
import sys

#opens file
def open_file(file_name,mode):
    """Open file"""
    try:
        the_file=open(file_name,mode,encoding='utf-8')
    except IOError as e:
            print("Impossible to open file ", file_name,". Programm will stop\n",e)
            input("\n\nPress Enter to exit")
            sys.exit()
    else:
        return the_file

#next_line
def next_line(the_file):
    """returns formatted strings from file"""
    line=the_file.readline()
    line=line.replace("/","\n")
    return line

#next_block
def next_block(the_file):
    """Return data block from file"""
    category=next_line(the_file)
    question=next_line(the_file)
    answers=[]
    for i in range(4):
        answers.append(next_line(the_file))
    correct=int(next_line(the_file))
    explanation=next_line(the_file)
    return category,question,answers,correct,explanation

#welcome
def welcome(title):
    """Welcomes player and tells theme of the game"""
    print("\t\tWelcome to the game 'Victorina'")
    print("\t\t",title,"\n")

#main
def main():
    trivia_file=open_file("Trivia.txt","r")
    title=next_line(trivia_file)
    welcome(title)
    score=0
    #taking first block
    category,question,answers,correct,explanation=next_block(trivia_file)

    print(category)
    print(question)
    for i in answers:
        print("\n",i)

    answer=int(input("Your answer: "))
    print(correct)

    #taking answer
    if answer==correct:
        print("\nYes!",end=" ")
        score+=1
    else:
        print("\nNo.",end=" ")
    print(explanation)
    print("Score: ",score,"\n\n")

    #next_block
    category,question,answers,correct,explanation=next_block(trivia_file)

    #close
    trivia_file.close()
    print("it was last question")
    print("Your score",score)

main()
input("\n\nPress Enter to exit")
