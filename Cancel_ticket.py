import pandas as pd

def cancel_ticket():

    df=pd.read_csv("Database.csv")

    user:int=int(input("Enter the PNR"))

    result=df[df["PNR"]==user]
    if not result.empty:
        # row delete karo
        df = df[df["PNR"] != user]

        # file update karo
        df.to_csv("Database.csv", index=False)

        print("✅ Your Ticket has been Cancelled")
    else:
        print("❌ Wrong PNR!")