import random
import datetime as dt
import smtplib as s

def is_friday(date):
    # Check if the weekday of the date is Tuesday (1)
    return date.weekday() == 4


def read_file_to_list(filename):
    try:
        with open(filename, 'r') as file:
            # Read lines from the file and split them into a list
            lines = file.readlines()
            # Remove newline characters from each line
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


email = "add your mail here"
password = "Add your own password"

filename = r'D:\Python VS CODE\Birthday Wisher\quotes.txt' 
text_list = read_file_to_list(filename)
date_to_check = dt.datetime.now()  # You can replace this with any other datetime object


# Set up the secure connection
if is_friday(date_to_check):
    connection = s.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email,password=password)
    text = random.choice(text_list)
    connection.sendmail(
                        from_addr=email,
                        to_addrs="...................",
                        msg=f"Subject:Friday Motivation\n\n {text}")
