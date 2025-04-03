import pandas as pd
import re
file_path = "emails.txt" 


email_list = [
    "nslosman@013net.net", "info@03beheer.be", "contact@109immobilier.com",
    "sales@101cph.com", "john@100foldstudio.org", "info@10hoog.nl"
]

# Define generic email prefixes
generic_prefixes = ("info", "sales", "contact", "support", "help", "admin", "mail", "events", "post")

generic_emails = [email for email in email_list if email.split('@')[0].startswith(generic_prefixes)]
specific_emails = [email for email in email_list if email not in generic_emails]


df = pd.DataFrame({"Generic Emails": pd.Series(generic_emails), "Specific Emails": pd.Series(specific_emails)})


df.to_csv("separated_emails.csv", index=False)
print("Emails separated and saved to 'separated_emails.csv'")
print(df)