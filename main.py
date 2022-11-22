import webbrowser

from fpdf import FPDF


class Bill:
    """"
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Roommates:
    """"
    Roommate that lives in the house, contain information about name and days that roommate has been in the house.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, slacker2):
        return f"{bill * (self.days_in_house / (self.days_in_house + slacker2)):.2f}"


class PdfReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        """"
        Generating PDF file with bill
        """
        # setting the amount that every roommate has to pay
        dynamic_amount_per_roommate1 = str(roommate1.pays(bill.amount, roommate2.days_in_house))
        dynamic_amount_per_roommate2 = str(roommate2.pays(bill.amount, roommate1.days_in_house))

        # creating page for the PDF report
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon to the PDF file
        pdf.image("house.png", w=50, h=50)

        # Title of the report
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Roommates Bill", border=1, ln=1, align="C")

        # current period
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=120, h=80, txt="Period:", border=1, ln=0)
        pdf.cell(w=0, h=80, txt=bill.period, border=1, ln=1)

        # roommate1
        pdf.cell(w=120, h=80, txt=roommate1.name + ":", border=1, ln=0)
        pdf.cell(w=0, h=80, txt=dynamic_amount_per_roommate1 + "$", border=1, ln=1)

        # roommate2
        pdf.cell(w=120, h=80, txt=roommate2.name + ":", border=1, ln=0)
        pdf.cell(w=0, h=80, txt=dynamic_amount_per_roommate2 + "$", border=1, ln=1)

        pdf.output(self.filename)
        # setting to open the current pdf file
        webbrowser.open(self.filename)


print("Current App is used to calculate how much every roommate has to pay based on "
      "the days he stayed in the house."
      "\n""When you fill up the information you will receive PDF report. :)")

current_bill = Bill(amount=int(input("Please enter amount of the Bill: ")),
                    period=input("Please enter current Month: "))
roommate_one = Roommates(name=input("Enter your name: "),
                         days_in_house=int(input("Enter how many days you stayed in the house: ")))
roommate_two = Roommates(name=input("Enter your roommate name: "),
                         days_in_house=int(input("Enter how many days he stayed in the house: ")))


current_pdf = PdfReport(f"{current_bill.period}_bill.pdf")

current_pdf.generate(roommate_one, roommate_two, current_bill)
