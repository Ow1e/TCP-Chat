from base64 import encode
from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

message = "my deep dark secret"
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)

f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)
print(decrypted.decode())