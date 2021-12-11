import argparse
from easywallet import wallet_parser
from easywallet.encryption import env_path

NETWORKS = {
    "eth": "Ethereum mainnet",
    "bsc": "Binance Smart Chain",
    "avax": "Avax mainnet",
    "polygon": "Polygon mainnet",
    "ganache": "Ganache testnet",
}

def execute(args):
    if args.create_wallet:
        wallet_parser.create_wallet(env_path())
    return args


def parse_args():
    parser = argparse.ArgumentParser(description='Welcome to EasyWallet, your command line blockchain wallet')

    #wallet
    parser.add_argument('-create_wallet', action='store_true', help='generate a seed phrase and activate a new wallet from it')
    parser.add_argument('-load_seed', action='store_true', help='load a wallet from a seed phrase')
    parser.add_argument('-load_pk', action='store_true', help='load a wallet from a private key')
    parser.add_argument('-balance', action='store_true', help='show the balance for the active wallet')

    #contacts 
    parser.add_argument('-list_contacts', action='store_true', help='list all your contacts')
    parser.add_argument('-add_contact', type=str, nargs=2, help='add a new contact address to your contact list. The first argument is the name of the contact and the second argument is the address')
    parser.add_argument('-remove_contact', type=str, nargs=1, help='remove an address from your contact list. The expected argument is the name of the contact')

    #transactions
    parser.add_argument('-send', nargs=2, help='send a transaction with value from the active wallet. The first argument is the address or contact name of the recipient and the second argument is the value to send')
    parser.add_argument('-deploy_contract', type=str, nargs=1, help='deploy a solidity smart contract to the blockchain')
    
    #network
    parser.add_argument('-list_networks', action='store_true', help='list all avaliable networks for use')
    parser.add_argument('-set_network', choices=NETWORKS.keys(), help='activate a specific network for usage in the current environment')

    #environment
    parser.add_argument('-env_info', action='store_true', help='show all the information about the current active environment')
    parser.add_argument('-list_envs', action='store_true', help='list all available environments for use')
    parser.add_argument('-remove_env', action='store_true', help='Destroy the current active environment. (All data will be lost)')
    args =  parser.parse_args() 

    #check if args is empty
    if not any(vars(args).values()):
        print("easywallet: try 'easywallet --help' for more information")
        return None
    return execute(args) 


