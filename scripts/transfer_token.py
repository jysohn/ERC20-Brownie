from brownie import OurToken, accounts, TokenTransfer, config
from scripts.helpful_scripts import get_account
from web3 import Web3

def main():
    account = get_account()
    our_token = OurToken[-1]
    TokenTransfer.deploy(our_token,{"from": account})
    token_transfer = TokenTransfer[-1]
    print("transferring now...")
    #receipient = '0x2CC8781EBb87D78ad45E84C57CcEB2F9756Cc4D1'
    receipient = get_account(index=1)
    amount = 1
    tx = token_transfer.tokenTransfer(receipient, amount, {"from": account})
    tx.wait(1)
    print("transfer complete!")