import pandas as pd

def search_ticket():

    df=pd.read_csv("Database.csv")

    user:int=int(input("Enter your PNR number"))

    result =df[df["PNR"]== user]

    if not result.empty:
        print("\n🎫 Your Ticket:\n")
        print(result)
    else:
        print("❌ No ticket found with this PNR")