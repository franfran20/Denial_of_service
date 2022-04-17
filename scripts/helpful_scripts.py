from brownie import accounts, network
from web3 import Web3

LOCAL_BLOCKCHAIN_ENV = ["development", "ganache", "hardhat"]


def get_account(id=None, index=None):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        return accounts[0]
    if id:
        return accounts.load(id)
    if index:
        return accounts[index]
