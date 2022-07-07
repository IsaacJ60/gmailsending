from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


with open("accounts.txt", mode="r", encoding="utf-8") as accounts:
    for account in accounts:
        username = (account.split()[0])
        password = (account.split()[1])

s = smtplib.SMTP(host="smtp.gmail.com", port=587)
s.starttls()
s.login(username, password)


def getContacts(filename):
    n = []
    e = []
    with open(filename, mode="r", encoding="utf-8") as contacts:
        for contact in contacts:
            n.append(contact.split()[0])
            e.append(contact.split()[1])
    return n, e


def readTemplate(filename):
    with open(filename, mode="r", encoding="utf-8") as templateFile:
        templateContent = templateFile.readlines()
        subject = templateContent.pop(0)
        templateContent = "".join(templateContent)
    return Template(templateContent), subject


def main():
    names, emails = getContacts("mycontacts.txt")
    msgTemplate = readTemplate("message.txt")[0]

    for name, email in zip(names, emails):
        msg = MIMEMultipart()

        message = msgTemplate.substitute(PERSON_NAME=name.title())

        msg["From"] = "pythontests68@gmail.com"
        msg["To"] = email
        msg["Subject"] = readTemplate("message.txt")[1]

        msg.attach(MIMEText(message, "plain"))

        s.send_message(msg)

        del msg

    s.quit()


if __name__ == "__main__":
    main()
