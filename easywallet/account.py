"""
The account module encapsulates all the functions required to create, generate and validate a blockchain account/wallet.
this module aims to facilitate access to low level functions and to provide a high level interface to the blockchain account creation.
"""
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from mnemonic import Mnemonic


def account_from_pk(private_key: bytes) -> dict:
    """uses a private key to create a dictorary containing all the required information for an blockchain account (  private key, public key, address )"""
    public_key = _pubkey_from_pk(private_key)
    address = _addr_from_pubkey(public_key)
    return {
        'private_key': private_key,
        'public_key': public_key.hex(),
        'address': _addr_eth_format(address),
    }

def create_account(mnemonic: str = None) -> dict:
    """creates new and unique dictorary containing all the required information for an blockchain account ( mnemonic, private key, public key, address )"""
    if mnemonic is None:
        mnemonic = Mnemonic('english').generate(strength=256)
    private_key = _generate_pk(mnemonic)
    public_key = _pubkey_from_pk(private_key)
    address = _addr_from_pubkey(public_key)
    return {
        'mnemonic': mnemonic,
        'private_key': private_key.hex(),
        'public_key': public_key.hex(),
        'address': _addr_eth_format(address),
    }
    
def _generate_pk(mnemonic: str=None) -> bytes:
    """deterministically generates a private key from a mnemonic for a blockchain account/wallet"""
    seed = Mnemonic('english').to_seed(mnemonic) if mnemonic else token_bytes(32)
    return keccak_256(seed).digest()

def _pubkey_from_pk(private_key: bytes) -> PublicKey:
    """deterministically generates a public key from a private key for a blockchain account/wallet"""
    return PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]

def _addr_from_pubkey(public_key: PublicKey) -> str:
    """deterministically generates a address from a public key for a blockchain account/wallet"""
    return keccak_256(public_key).digest()[-20:].hex()

def _addr_eth_format(addr: str) -> str:
    """applies the hex 0x prefix to a address that is the standard used in the blockchain wallets/accounts"""
    return f'0x{addr}'