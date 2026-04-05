import pandas as pd
import os
from utils import Aadhar,generate_pnr,generate_pdf,seat,calculate_fare,date
from train_info import check_availability,select_train,show_trains
def create_ticket():

    train_df = show_trains()
    train = select_train(train_df)

    if train is None:
        return

    train_no = train["Train_No"]
    train_name = train["Train_Name"]

    status, info = check_availability(train_no)
    name = input("Enter Name: ")
    try:
      age = int(input("Enter Age: "))
    except:
       print("Invalid input")
    aadhar_number = Aadhar()
    source = input("From: ")
    destination = input("To: ")
    distance = int(input("Distance: "))

    travel_class, seat_no = seat() # ✅ ek hi baar call
    fare = calculate_fare(distance, travel_class)  # ✅ fix

    pnr = generate_pnr()

    ticket = {
    "PNR": pnr,
    "Name": name,
    "Age": age,
    "Aadhar": aadhar_number,
    "Train_No": train_no,     # ✅ MUST
    "Train_Name": train_name, # ✅ MUST
    "From": source,
    "To": destination,
    "Class": travel_class,
    "Seat": seat_no,
    "Fare": fare,
    "Date": date,
    "Status": status,
    "Seat/Waiting": info
}

    generate_pdf(ticket)

    df = pd.DataFrame([ticket])
    file_exists = os.path.isfile("Database.csv")
    df.to_csv("Database.csv", mode='a', index=False, header=not file_exists,encoding="utf-8")

    print("\n🎫 Ticket Generated Successfully...\n")
    print(df)

    