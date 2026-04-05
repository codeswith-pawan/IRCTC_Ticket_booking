import pandas as pd
from utils import seat

df = pd.read_csv("train.csv")

def show_trains():
    print("\nAvailable Trains:\n")
    print(df)
    return df

def select_train(df):
    train_no = int(input("Enter Train number: "))

    train = df[df["Train_No"] == train_no]  # ✅ FIX

    if not train.empty:   
        return train.iloc[0]
    else:
        print("Invalid input")
        return None

def check_availability(train_no):
    try:
        df = pd.read_csv("Database.csv")
        booked = len(df[df["Train_No"] == train_no])
    except:
        booked = 0

    total = 1

    if booked < total:
      total -=1
      return "Confirmed",None  # actual seat
    else:
     return "Waiting", booked - total + 1