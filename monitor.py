import requests
import time
import smtplib
from bs4 import BeautifulSoup

SENDER_EMAIL = ""
SENDER_PASSWORD = ""
RECEIVER_LIST = []
MOVIE_URL = ""

def check(movie_url):
    req = requests.get(movie_url)
    soup = BeautifulSoup(req.text, "html.parser")

    if (soup.find_all(id='page-cta-container') == []):
        return False

    return True

def send_email():
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()

    # Authentication
    s.login(SENDER_EMAIL, SENDER_PASSWORD)

    # message to be sent
    message = ""

    for receiver in RECEIVER_LIST:

        # sending the mail
        s.sendmail(SENDER_EMAIL, receiver, message)

    # terminating the session
    s.quit()

if __name__ == '__main__':
    while (True):
        ch = check(movie_url)
        if (ch):
            send_email()
            break
        else:
            time.sleep(3*60)
