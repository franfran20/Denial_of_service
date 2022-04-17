from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import KingOfEther, Attack, FixedKingOfEther, accounts


def deploy_contract():
    account = get_account()
    king_of_ether = KingOfEther.deploy({"from": account})
    attack = Attack.deploy({"from": account})
    fixed_king_of_ether = FixedKingOfEther.deploy({"from": account})

    return king_of_ether, attack, fixed_king_of_ether


def main():
    deploy_contract()
