import smtplib
import quotes


def send_email():
    """Send an email with subject and text body through Python """
    my_email = "youremail.com"
    password = "yourpassword"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="recipientemail.com",
                        msg="Subject:Hello\n\nThis is the body of the email")
    connection.close()

# ---------------------------

# print a motivational quote if day of the week is Monday.


quotes.get_current_datetime()
