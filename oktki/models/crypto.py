import binascii, hashlib, os


def create_salt():
    return binascii.hexlify(os.urandom(64)).decode('utf-8')

def hash_password(password, salt, iterations=10000):
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    for i in range(iterations):
        password = hashlib.sha512(password + salt).hexdigest().encode('utf-8')
    return password.decode('utf-8')
