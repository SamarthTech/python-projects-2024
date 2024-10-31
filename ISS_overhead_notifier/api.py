import requests
from datetime import datetime
import smtplib

USER_LATITUDE = 22.572645
USER_LONGITUDE = 88.363892
MY_EMAIL = "soumyo460@gmail.com"
PASSWORD = "shonsupylexvdsnm"
to_addrs = None

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()
data1 = response1.json()
iss_lat = float(data1["iss_position"]["latitude"])
iss_lng = float(data1["iss_position"]["longitude"])

def is_iss_over_head () :
    if iss_lat-5 <= USER_LATITUDE <= iss_lat+5 and iss_lng-5 <= USER_LONGITUDE <= iss_lng+5 :
        return True
    else:
        return False
    

# Sunset sunrise time
parameters = {
    "lat" : USER_LATITUDE,
    "lng" : USER_LONGITUDE,
    "formatted" : 0,
}
response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data = response2.json()
sunset_time = int(data['results']["sunset"].split("T")[1].split(":")[0])
sunrise_time = int(data['results']["sunrise"].split("T")[1].split(":")[0])
now_hr = int(datetime.now().hour)

def is_night() :
    if sunset_time < now_hr < sunrise_time :
        return True
    else:
        return False


# Sending email
def send_email () :
    with smtplib.SMTP("smtp.gmial.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="", msg="subject: LOOK UP!! \n\n ISS is over your head look up!!!")


def checking_and_sending () :
    while True:
        if is_iss_over_head() and is_night() :
            send_email()

        
def take_details () :
    global USER_LATITUDE, USER_LONGITUDE, to_addrs
    while True:
        try:
            USER_LATITUDE = float(input("ENTRE YOUR LOCAL LATITUDE: "))
            USER_LONGITUDE = float(input("ENTRE YOUR LOCAL LONGITUDE: "))
            break
        except ValueError:
            print("INVALID INPUTSSS!!!")
            
    to_addrs = input("ENTRE YOUR EMAIL ADDRESS: ")
    print("WAIT FOR THE MAIL...👀")
    



take_details()
checking_and_sending ()





