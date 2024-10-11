'''
import win32com.client as win

outlook = win.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Access inbox
inbox = outlook.GetDefaultFolder(6) 

# Search emails
def search_emails(usernames):
    emails = []
    for username in usernames:
        messages = inbox.Items
        messages = messages.Restrict(f"[SenderName] = '{username}'")
        for message in messages:
            emails.append(message.SenderEmailAddress)
    return emails

usernames = ["Jakhmola, Brijmohan (cognizant)"]  
emails = search_emails(usernames)
print(emails)
'''
# ---------------------Email send--------------------
# import win32com.client as win32
# outlook = win32.Dispatch('outlook.application')
# mail = outlook.CreateItem(0)
# mail.To = '2186236@cognizant.com'
# mail.Subject = 'Test Email'
# mail.Body = 'This is a test email from <h1>python.</h1>'
# mail.Send()
# print("Email sent successfully!")

# ------------------------------------------

# import win32com.client as win32
# outlook = win32.Dispatch('outlook.application')
# mail = outlook.CreateItem(0)
# mail.To = '2186236@cognizant.com'
# mail.Subject = 'Test Email'
# mail.BodyFormat = 2  
# mail.HTMLBody = '<h1>This is a test email</h1><p>HTML.</p>'
# mail.Send()
# print("Email sent successfully!")


# ----------------------------------------------------
import win32com.client as win
with open('email.txt', 'r') as file:
    email_addresses = file.readlines()
outlook = win.Dispatch('outlook.application')
for email in email_addresses:
    email = email.strip()
    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = 'Test Email'
    mail.BodyFormat = 2  
    mail.HTMLBody = '<h1>This is a test email</h1><p>HTML.</p>'
    mail.Send()
    print(f"Email sent successfully to {email}!")
print(" emails sent successfully!")



