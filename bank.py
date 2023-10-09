#MKHABELE MMM
#28/06/2023
def main():
    greet=input("Greetings: ")
    def greeting_checker(n):
        n=(n.lower()).split()#splits into list
        if n[0][0:5]=="hello":#check first element of list
                print("$0")
        elif n[0][0]=="h":   
                print('$20')
        else:
            print("$100")
    greeting_checker(greet)
main()