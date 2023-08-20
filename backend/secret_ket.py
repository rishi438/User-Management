import secrets

SECRET_KEY = secrets.token_hex(32)  # Generate a 64-character hexadecimal key
print(SECRET_KEY)