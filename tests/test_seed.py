from easywallet.seed import create_account

def test_account_info_from_mnemonic():
    mnemonic = 'adjust skin maple rotate quiz wedding ill organ target rare hand range afraid flavor hole erupt bullet color crime rookie cat phone advance winter'
    acc = create_account(mnemonic)

    assert acc['mnemonic'] == mnemonic
    assert acc['private_key'] == 'c0347b07909d2f364409edf0792b6b4009036468455f9404d5cb4f693f3da420'
    assert acc['public_key'] == '9d8f9358ccf569ac7d7066e9db1bc8bd24be9d2c6b05ac363f517cbef91a78f99095d197e4ceaede5883f7252d8bf3af4490ea4fd01e95b9819172fc70bf6931'
    assert acc['address'] == '0x40b8ac1d1df74e0649cea84e896c70c18de834fd'

def test_generate_new_account():
    acc = create_account()
    assert len(acc['mnemonic'].split(' ')) == 24
    assert len(acc['private_key']) == 64
    assert len(acc['public_key']) == 128
    assert len(acc['address']) == 42

def test_address_is_standard():
    acc = create_account()
    assert acc['address'].startswith('0x')
    