from email import header
from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

headers = {
  "Accept-Language": "en-US",
  "User-Agent":"Chrome"
}

response = requests.get(url="https://www.amazon.com/dp/B0773ZY26F?ref_=cm_sw_r_cp_ud_dp_MXXJE8623PZ3JPH8B488", headers=headers)
website = response.text

soup = BeautifulSoup(website, "lxml")
price = float(soup.find(name="span", class_="a-offscreen").text[1:])
title = soup.find(id="productTile").get_text().strip()

BUY_PRICE = 500

if price < BUY_PRICE:
  message = f"{title} is now {price}"

  with smtplib.SMTP("smtp@gmail.com", port=587) as connection:
    connection.starttls()
    result = connection.login(MAIL, PASSWORD)
    connection.sendmail(from_addr=MAIL,
                        to_addrs=MAIL,
                        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
                        )
