# You will need birthday.cvs. Data shoudl be entered as [ name,email,year,month,day ]
# Sample letter with [NAME]
# On the correct day, an auto email will be sent out

import pandas
import smtplib
import random
from datetime import datetime

Email = ""
password = ""

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(Email, password)
        connection.sendmail(
            from_addr=Email, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
