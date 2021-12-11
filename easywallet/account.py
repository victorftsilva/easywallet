from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from mnemonic import Mnemonic

## Low level features used create and generate all features requires for blockchain wallet ( account )

def account_from_pk(private_key) -> dict:
    public_key = _pubkey_from_secret(private_key)
    address = _addr_from_pubkey(public_key)
    return {
        'private_key': private_key,
        'public_key': public_key.hex(),
        'address': _addr_eth_format(address),
    }

def create_account(mnemonic=None) -> dict:
    if mnemonic is None:
        mnemonic = Mnemonic('english').generate(strength=256)
    private_key = _generate_pk(mnemonic)
    public_key = _pubkey_from_secret(private_key)
    address = _addr_from_pubkey(public_key)
    return {
        'mnemonic': mnemonic,
        'private_key': private_key.hex(),
        'public_key': public_key.hex(),
        'address': _addr_eth_format(address),
    }
    
def _generate_pk(mnemonic=None) -> bytes:
    seed = Mnemonic('english').to_seed(mnemonic) if mnemonic else token_bytes(32)
    return keccak_256(seed).digest()

def _pubkey_from_secret(private_key) -> PublicKey:
    return PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]

def _addr_from_pubkey(public_key) -> str:
    return keccak_256(public_key).digest()[-20:].hex()

def _addr_eth_format(addr) -> str:
    return f'0x{addr}'