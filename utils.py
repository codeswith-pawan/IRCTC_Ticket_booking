import random
from fpdf import FPDF
from datetime import datetime
import pandas as pd
def Aadhar():
    while True:
        aadhar = input("Enter Aadhar Number: ")
        if len(aadhar) == 12 and aadhar.isdigit():
            return aadhar
        else:
            print("Invalid! Try again")
def generate_pnr():
    return random.randint(1000000000, 9999999999)

def generate_pdf(ticket):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for key, value in ticket.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.output(f"tickets_db/{ticket['PNR']}.pdf")

def calculate_fare(distance, travel_class):
    if travel_class == "Sleeper":
        return distance * 0.5
    elif travel_class == "AC":
        return distance * 1.5
# Date
date = datetime.now().strftime("%d-%m-%Y %H:%M")

# Seat Allocation
def seat_allocation_Sleeper():
    coach = random.choice(["S1","S2","S3","S4","S5","S6","S7"])
    seat_no = random.randint(1,72)
    return f"{coach}-{seat_no}"

def seat_allocation_AC():
    coach = random.choice(["A1"])
    seat_no = random.randint(1,72)
    return f"{coach}-{seat_no}"

# Seat + Class
def seat():
    while True:
        sl = int(input("Select Class:\n1) Sleeper\n2) AC\n"))

        if sl == 1:
            return "Sleeper", seat_allocation_Sleeper()
        elif sl == 2:
            return "AC", seat_allocation_AC()
        else:
            print("Invalid choice!")

