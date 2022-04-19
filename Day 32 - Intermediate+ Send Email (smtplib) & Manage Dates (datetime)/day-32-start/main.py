import random
import smtplib

my_email = "26omerdikyol@gmail.com"
password = "anothertime2662"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls() # Securing our connection with server ( Message will be encrypted )
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs= "omerdikyol02@gmail.com",
#                     msg="Subject:Hello\n\n""This is the body of my email.")
# connection.close()

# with smtplib.SMTP("smtp.gmail.com") as connection:

import datetime as dt
#
# now = dt.datetime.now()
# print(now)  # type == datetime.datetime
# print(now.year)  # type == int
# print(now.weekday())
#
# date_of_birth = dt.datetime(2002, 4 , 2)
# print(date_of_birth)



# Challenge 1 - Send motivational quotes on mondays via email
import random

day = dt.datetime.now().weekday()
print(day)
with open("quotes.txt", mode="r") as data:
    quotes = data.readlines()
if day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs= my_email,
                            msg=f"Subject:Quote of Monday\n\n{random.choice(quotes)}")
