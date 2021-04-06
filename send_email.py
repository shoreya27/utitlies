'''
Module sends email from terminal.
User inputs the required subject, body, recipent 
'''
import smtplib
from email.message import EmailMessage


class EmailService():

    BY = "assignmnt.zelth06@gmail.com"
    PASS = "ZelthyP06"

    def __init__(self, body, subject, recipent):
        self.body = body
        self.subject = subject
        self.recipent = recipent
    
    def _send(self):
        msg = EmailMessage()
            
        msg.set_content(self.body)
        msg["From"] = self.BY
        msg["To"] = self.recipent
        msg["Subject"] = self.subject
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # server = smtplib.SMTP('localhost')
        server.starttls()
        server.login(self.BY, self.PASS)
        server.send_message(msg)
        server.quit()

    def trigger_mail(self):
        self._send()

def please_send_my_mail():
    '''
    This function is called from __main__
    and instantiates the EmailService()
    '''

    subject = input("Subject? ")
    body    = input("Body? ")
    recipent= input("Recipent? ")

    service_obj = EmailService(body = body,
                               subject = subject,
                               recipent= recipent
                               )
    service_obj.trigger_mail()


if __name__ == "__main__":
    please_send_my_mail()
    print("Email sent!")