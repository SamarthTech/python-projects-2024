import random
import pandas as pd
import smtplib
import datetime as dt
MY_EMAIL = "soumyo460@gmail.com"
PASSWORD = "shonsupylexvdsnm"
TEMPLATE_LIST = [f"Automated_Birthday_Wisher/letter_templates/letter_{i}.txt" for i in range(1,4)]


# Mail Function
def send_email (mail_address_to_send , messege) :
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=mail_address_to_send, msg=f"subject : Happy Birthday!!\n\n{messege}")






now = dt.datetime.now()
m = now.month
d = now.day
today = (m,d)

# Creating dict with bday info
data = pd.read_csv("32_DAY/happy_birthday/birthdays.csv")
birthdays_dict ={
    (data_row["month"] , data_row["day"]) : data_row for (index, data_row) in data.iterrows()
}



if today in birthdays_dict:

    bday_prsn = birthdays_dict[today]["name"]
    email_add = birthdays_dict[today]["email"]

    # Pick a random letter template for each person
    selected_template = random.choice(TEMPLATE_LIST)

    with open(selected_template, "r") as st:
        text = st.read()
        new_text = text.replace("[NAME]", bday_prsn)

        send_email(email_add, new_text)


