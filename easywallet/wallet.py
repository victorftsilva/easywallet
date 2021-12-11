import os
from easywallet.account import create_account, account_from_pk 
from easywallet.encryption import encrypt


## High level features to interact with user facing blockchain wallet

def create_wallet(path, mnemonic=None, private_key=None):
    """
    create a new file called wallet.txt on the path ( if the file doesn't exist )
    containing a encrypted blockchain wallet information that can be used to send and receive funds
    """
    path = path + "/wallet.txt"
    if os.path.exists(path):
        print("wallet already exists")
        return
    if private_key is not None:
        return _save_wallet(account_from_pk(private_key), path)
    return _save_wallet(create_account(mnemonic), path)


def _save_wallet(wallet, path):
    encrypted_wallet = encrypt(','.join(wallet.values())) #mnemonic,private_key,public_key,address
    with open(path, 'wb') as f:
        f.write(encrypted_wallet)
    print("new wallet saved, address: " + wallet['address'])
    return wallet