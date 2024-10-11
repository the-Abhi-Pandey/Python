#------------Generate Secrets key--------------
import secrets
def generate_secret_key(length=8):
    return secrets.token_hex(length)
secret_key = generate_secret_key()
print(f"Your secret key: {secret_key}")

#------------Geneate Password---------
'''
import secrets
import string
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
# Generate a 12-character password
password = generate_password()
print(f"here is password bro!:  {password}")

'''

# -----------------------------------

