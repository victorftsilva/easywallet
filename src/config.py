import os
import subprocess
from subprocess import DEVNULL, STDOUT

__ENV_PATH = None

def get_env_path():
    """
    Get the path of the environment.
    """
    global __ENV_PATH
    if __ENV_PATH is None:
        __ENV_PATH = __setup_environment()
    return __ENV_PATH

def __setup_environment():
    """
    Create a folder in the users home directory called .easywallet.
    inside the folder a public and private RSA keys will be created to encrypt and decrypt the generated keys.
    """
    home = os.path.expanduser("~")
    path = home + "/.easywallet"
    if not os.path.exists(path):
        os.makedirs(path)    
    __create_keys(path + "/keys")
    return path

def __create_keys(path):
    """Create a public and private RSA keys without printing to the stdout."""      
    if not os.path.exists(path + "/private.pem"):
        subprocess.call(['openssl', 'genrsa', "-out", path, "/private.pem 2048"], stdout=DEVNULL, stderr=STDOUT)
        subprocess.call(['openssl', 'rsa', "-im", path, "/private.pem", "-pubout" "-out", path, "/public.pem"], stdout=DEVNULL, stderr=STDOUT)   
    