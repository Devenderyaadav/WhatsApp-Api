import pywhatkit
import pandas as pd
import datetime as dt
import keyboard as k  
import time
import sys
import pyautogui

now = dt.datetime.now()
today_date = now.day
today_month = now.month
today_year = now.year
hour = now.hour
minute = now.minute
second = now.second
print(today_date, today_month, today_year)


pd.options.display.max_rows=9999
df = pd.read_excel('C:\\Users\\ajayf\\OneDrive\\Desktop\\whatsappapi\\datesend.xlsx')
print(df)

arr_date = list(df['DOB(Date)'].head(4))
arr_mont = list(df['DOB(Month)'].head(4))
arr_contact = list(df['Contact'].head(4))
arr_name = list(df['Name'].head(4))
arr_msg = list(df["Message"].head(4))

arr_indeces = []
for i in range(len(arr_date)):
    if today_month == arr_mont[i] and today_date==arr_date[i]:
        arr_indeces.append(i) 

contact = []
name = []
message= []

for i in arr_indeces:
    contact.append(arr_contact[i])
    name.append(arr_name[i])
    message.append(arr_msg[i])

print(name, contact)

def stopwatch(x):
    for remaining in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)

for i in range(len(contact)):
    if minute!=59 and second<=45:
        pywhatkit.sendwhatmsg(f"+91-{contact[i]}", message[i], hour, minute+i+1)
        pyautogui.click(1050, 950)
        time.sleep(2)
        k.press_and_release('enter')

    elif minute!=59 and second>45:
        pywhatkit.sendwhatmsg(f"+91-{contact[i]}",message[i], hour, minute+i+2)
        pyautogui.click(1050, 950)
        time.sleep(2)
        k.press_and_release('enter')

    elif minute==59 and second>45:
        pywhatkit.sendwhatmsg(f"+91-{contact[i]}", message[i], hour+1, i+2)
        pyautogui.click(1050, 950)
        time.sleep(2)
        k.press_and_release('enter')

    else:
        pywhatkit.sendwhatmsg(f"+91-{contact[i]}", message[i], hour+1, i)
        pyautogui.click(1050, 950)
        time.sleep(2)
        k.press_and_release('enter')