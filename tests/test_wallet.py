import os
import mnemonic
from easywallet.wallet import create_wallet
from easywallet.encryption import encrypt, decrypt

def test_create_new_wallet():
    """
    Test creating a new wallet in a temp folder
    """
    temp = os.path.join(os.path.expanduser('~'), '.temp/new_wallet')
    if not os.path.exists(temp):
        os.mkdir(temp)

    # remove wallet.txt file if exists in temp directory
    if os.path.exists(os.path.join(temp, 'wallet.txt')):
        os.remove(os.path.join(temp, 'wallet.txt'))
    
    new_wallet = create_wallet(temp)
    
    # check if wallet.txt file was created in temp directory
    assert os.path.exists(os.path.join(temp, 'wallet.txt'))

    # check if wallet.txt file is not empty
    assert os.stat(os.path.join(temp, 'wallet.txt')).st_size > 0

    # check if the wallet information was saved in the expected format inside the file
    # format: mnemonic,private_key,public_key,address
    saved_wallet_info = ','.join(new_wallet.values())
    with open(os.path.join(temp, 'wallet.txt'), 'rb') as f:
        file_content = f.read()
        assert saved_wallet_info != file_content
        assert saved_wallet_info.encode() != file_content
        assert saved_wallet_info == decrypt(file_content)

def test_create_wallet_from_mnemonic():
    """
    Test creating a new wallet from a mnemonic
    """
    temp = os.path.join(os.path.expanduser('~'), '.temp/wallet_from_mnemonic')
    if not os.path.exists(temp):
        os.mkdir(temp)

    mnemonic = 'clutch expand nest girl nothing february engine trophy assault attitude joke fat ivory mind rib forget burden risk early assume crime scare patch scorpion'

    # remove wallet.txt file if exists in temp directory
    if os.path.exists(os.path.join(temp, 'wallet.txt')):
        os.remove(os.path.join(temp, 'wallet.txt'))
    
    new_wallet = create_wallet(temp, mnemonic=mnemonic)
    
    # check if wallet.txt file was created in temp directory
    assert os.path.exists(os.path.join(temp, 'wallet.txt'))

    # check if wallet.txt file is not empty
    assert os.stat(os.path.join(temp, 'wallet.txt')).st_size > 0

    # check if the wallet information was saved in the expected format inside the file
    # format: mnemonic,private_key,public_key,address
    saved_wallet_info = ','.join(new_wallet.values())
    expected_wallet_info = 'clutch expand nest girl nothing february engine trophy assault attitude joke fat ivory mind rib forget burden risk early assume crime scare patch scorpion,8e8a215e490711bc0fc3d922d4cc8f99f02f6e72cd7c535cdd5157eb0b507f9c,00b7e9fad40b3547e5dbb86a86c91473f85b8b54525f9f378312f2f610bd449241567dfcdc8f326e3489b3247acf528c2842608d7fc1ebce1c95361301de49b2,0xdc65c4a7a182fa870ed01eb8aa6008e386c68175'
    assert saved_wallet_info == expected_wallet_info
    with open(os.path.join(temp, 'wallet.txt'), 'rb') as f:
        file_content = f.read()
        assert saved_wallet_info != file_content
        assert saved_wallet_info.encode() != file_content
        assert saved_wallet_info == decrypt(file_content)
        assert expected_wallet_info == decrypt(encrypt(saved_wallet_info))
    
def test_create_wallet_from_private_key():
    """
    Test creating a new wallet from a private key
    """
    temp = os.path.join(os.path.expanduser('~'), '.temp/wallet_from_private_key')
    if not os.path.exists(temp):
        os.mkdir(temp)

    private_key = '8e8a215e490711bc0fc3d922d4cc8f99f02f6e72cd7c535cdd5157eb0b507f9c'

    # remove wallet.txt file if exists in temp directory
    if os.path.exists(os.path.join(temp, 'wallet.txt')):
        os.remove(os.path.join(temp, 'wallet.txt'))
    
    new_wallet = create_wallet(temp, private_key=private_key)
    
    # check if wallet.txt file was created in temp directory
    assert os.path.exists(os.path.join(temp, 'wallet.txt'))

    # check if wallet.txt file is not empty
    assert os.stat(os.path.join(temp, 'wallet.txt')).st_size > 0

    # check if the wallet information was saved in the expected format inside the file
    # format: mnemonic,private_key,public_key,address
    saved_wallet_info = ','.join(new_wallet.values())
    expected_wallet_info = '8e8a215e490711bc0fc3d922d4cc8f99f02f6e72cd7c535cdd5157eb0b507f9c,00b7e9fad40b3547e5dbb86a86c91473f85b8b54525f9f378312f2f610bd449241567dfcdc8f326e3489b3247acf528c2842608d7fc1ebce1c95361301de49b2,0xdc65c4a7a182fa870ed01eb8aa6008e386c68175'
    assert saved_wallet_info == expected_wallet_info
    with open(os.path.join(temp, 'wallet.txt'), 'rb') as f:
        file_content = f.read()
        assert saved_wallet_info != file_content
        assert saved_wallet_info.encode() != file_content
        assert saved_wallet_info == decrypt(file_content)
        assert expected_wallet_info == decrypt(encrypt(saved_wallet_info))