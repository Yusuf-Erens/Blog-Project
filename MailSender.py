import smtplib
import os

def SendMail(name="",email="",number="DOESNT FILLED",message=""):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(os.getenv('FROM_MAIL'),os.getenv('APP_PASS'))
        connection.sendmail(from_addr=os.getenv('FROM_MAIL'),
                            to_addrs=os.getenv('TO_MAIL'),
                            msg=f"Subject:{name}\n\nName:{name}\nEmail:{email}\nPhone Number:{number}\n{message}")
