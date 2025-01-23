from urllib.parse import quote_plus

username = "rsah"
password = "Mongo@db"

encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

print(f"Encoded Username: {encoded_username}")
print(f"Encoded Password: {encoded_password}")
