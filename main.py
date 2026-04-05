
from Search_ticket import search_ticket
from Cancel_ticket import cancel_ticket
from Create_ticket import create_ticket


while True:
    print("\n====== IRCTC SYSTEM ======")
    user=int(input("Enter The choice\n1)Create Ticket\n2)View Ticket\n3)Cancel Ticket\n4)Exit\n"))
    if(user==1):
        create_ticket()
    elif(user==2):
        search_ticket()
    elif(user==3):
        cancel_ticket()
    elif(user==4):
        print("You exit the program")
        break
# Run
