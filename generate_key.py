from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

file = open('key.key', 'w')
file.write(key.decode())
file.close()