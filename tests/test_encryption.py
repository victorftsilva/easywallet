from easywallet.config import encrypt, decrypt, setup_environment

def test_string_encrypt_decrypt():
    setup_environment()
    hello_world = "Hello World!"
    encrypted_hello = encrypt(hello_world)

    assert encrypted_hello != hello_world # encrypted string should not be the same as the original string
    assert encrypted_hello != hello_world.encode() # encrypted string should not be the same as the original string only enconded to bytes
    assert hello_world == decrypt(encrypted_hello) # decrypted string should be the same as the original string
    assert "Hello World!".encode() == decrypt(encrypted_hello).encode() # decrypted string should be the same as the original when both are enconded to bytes