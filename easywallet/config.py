import os
from cryptography.fernet import Fernet

fernet_key = None

def get_key() -> Fernet:
    setup_environment()
    return fernet_key

def setup_environment() -> str:
    """
    Create a folder in the users home directory called .easywallet.
    inside the folder a public and private RSA keys will be created to encrypt and decrypt the generated keys.
    """
    global fernet_key
    
    home = os.path.expanduser("~")
    path = home + "/.easywallet"
    if not os.path.exists(path):
        os.makedirs(path +'/keys')   
        fernet_key = __create_key(path)
    elif fernet_key is None:
        with open(path + '/mykey.key', 'rb') as f:
            fernet_key = Fernet(f.read())
    return path

def __create_key(path) -> Fernet:
    key = Fernet.generate_key()
    with open(path + '/mykey.key', 'wb') as f:
        f.write(key)
    return key
    
def encrypt(string: str) -> str:
    """
    returns bytes for the encrypted string
    """
    fkey = get_key()
    return fkey.encrypt(string.encode())

def decrypt(encrypted: str) -> str:
    """
    returns a decrypted a string 
    """
    fkey = get_key()
    return fkey.decrypt(encrypted).decode()
    
   
    
  
    