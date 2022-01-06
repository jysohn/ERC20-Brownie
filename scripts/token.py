from scripts.helpful_scripts import get_account
from brownie import OurToken, TokenTransfer, accounts, config
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

def deploy_token():
    account = get_account()
    our_token = OurToken.deploy(initial_supply, {"from": account})
    print(our_token.name())

def transfer_token():
    account = accounts.add(config["wallets"]["from_key"])
    receipient = accounts.add(config["wallets"]["from_key2"])
    #our_token = '0xc5cd7587c0cd72a38e42e560440d985b3cc0490e'
    our_token = OurToken[-1]
    print(f"printing account {account}")
    print(f"printing receipient {receipient}")
    print(f"printing our_token {our_token}")

    TokenTransfer.deploy(our_token,{"from": account})
    token_transfer = TokenTransfer[-1]
    print("transferring now...")
    
    amount = "1000 wei"
    print(account.balance())
    print(receipient.balance())
    tx = token_transfer.tokenTransfer(receipient, amount, {"from": account})
    tx.wait(1)
    print("transfer complete!")
    print(account.balance())
    print(receipient.balance())

def main():
    #deploy_token()
    transfer_token()