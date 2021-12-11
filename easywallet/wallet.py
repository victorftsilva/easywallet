"""
The wallet module is responsible for managing the wallet.txt file that contains the encrypted blockchain account/wallet information. 
It is responsible for creating a new wallet, loading an existing wallet, and saving the wallet.
it provides a high level utility function for sending, receiving funds and other interactions abstracting the web3 and blockchain details.
"""
import os
from easywallet.account import create_account, account_from_pk 
from easywallet.encryption import encrypt, decrypt

WALLET_FILE = 'wallet.txt'
DEFAULT_WALLET_PATH = os.path.join(os.path.expanduser('~'), '.easywallet')

class Wallet:
    """
    Creates a new wallet or load an existing wallet from a file.
    * if wallet path and a wallet exists on the path, load the wallet.
    * if a mnenomic or private key is provided, it will create the wallet using the field as a seed to deterministically generating the wallet data.
    * if no wallet data is provided a new wallet will be generated from a seed phrase (mnemonic)
    * to save the wallet to file you must explicitly call save_wallet() method.this is the only way to ensure the wallet is saved to the correct location.
    """
    def __init__(self, mnemonic: str =None, private_key: bytes=None, wallet_path: str = DEFAULT_WALLET_PATH):
        if wallet_path is not None and os.path.exists(wallet_path):
            self._load_existing_wallet()
        elif mnemonic is not None:
            self._load_from_mnemonic(mnemonic)
        elif private_key is not None:
            self._load_from_private_key(private_key)
        self._set_attributes(create_account())

    def save(self):
        """
        Encrypts and save the wallet information on wallet.txt located in wallet_path for future use.
        * will raise a ValueError if the wallet_path is None or if the wallet fields are not set
        """
        wallet = [self.private_key, self.public_key, self.address, self.mnemonic]
        wallet = [field for field in wallet if field is not None]
        if len(wallet) < 3:
            raise ValueError("invalid wallet, must have at least 3 fields")
        encrypted_wallet = encrypt(','.join(wallet.values()))
        with open(self.wallet_path, 'wb') as f:
            f.write(encrypted_wallet)
        print("new wallet saved, address: " + wallet['address'])
        return wallet
 
    def _load_from_mnemonic(self, mnemonic):
        """
        create a new wallet from a mnemonic seed phrase
        """
        wallet_data = create_account(mnemonic)
        self._set_attributes(wallet_data)
    
    def _load_from_private_key(self, private_key):
        """
        create a new wallet from a private key
        """
        wallet_data = account_from_pk(private_key)
        self._set_attributes(wallet_data)
    
    def _exists_wallet(self, path):
        """check if a file with wallet information exists on the provided path"""
        path = f"{path}/{WALLET_FILE}"
        return os.path.exists(path)
    
    def _load_existing_wallet(self):
        """
        load an existing wallet file from the path provided
        """
        if self.wallet_path is None:
            raise ValueError("wallet path is not set")
        if not self._exists_wallet(self.wallet_path):
            raise ValueError(f"wallet does not exist on the path: {self.wallet_path}")
        with open(f"{self.wallet_path}/{WALLET_FILE}", "r") as f:
            encrypted_wallet = f.read()
            wallet_info = decrypt(encrypted_wallet).split(",")
            if len(wallet_info) < 3:
                raise ValueError("invalid wallet file, the wallet must have a minimum of 3 fields")
            self.private_key = wallet_info[0]
            self.public_key = wallet_info[1]
            self.address = wallet_info[2]
            if len(wallet_info) > 3:
                self.mnemonic = wallet_info[3]

    def _set_attributes(self, wallet_info):
        self.mnemonic = wallet_info.mnemonic
        self.private_key = wallet_info.self.account.private_key
        self.public_key = wallet_info.public_key
        self.address = wallet_info.address