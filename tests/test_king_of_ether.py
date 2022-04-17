import pytest
from scripts.deploy_contract import deploy_contract
from brownie import accounts, exceptions, network
from web3 import Web3

from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENV


def test_king_of_ether_expected():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("Only for local testing")
    # deploy contract
    king_of_ether, attack, fixed_king_of_ether = deploy_contract()

    # making new kings
    tx_king1 = king_of_ether.becomeTheNewKing(
        {"from": accounts[0], "value": Web3.toWei(1, "ether")}
    )
    print(f"{king_of_ether.King()}")
    tx_king1.wait(1)

    tx_king1 = king_of_ether.becomeTheNewKing(
        {"from": accounts[1], "value": Web3.toWei(2, "ether")}
    )
    print(f"{king_of_ether.King()}")
    tx_king1.wait(1)

    assert king_of_ether.King() == accounts[1].address


def test_perform_denial_of_service():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("Only for local testing")
    # deploy contract
    king_of_ether, attack, fixed_king_of_ether = deploy_contract()

    # making new kings
    tx_king1 = king_of_ether.becomeTheNewKing(
        {"from": accounts[0], "value": Web3.toWei(1, "ether")}
    )
    print(f"{king_of_ether.King()}")
    tx_king1.wait(1)

    tx_king2 = king_of_ether.becomeTheNewKing(
        {"from": accounts[1], "value": Web3.toWei(2, "ether")}
    )
    print(f"{king_of_ether.King()}")
    tx_king2.wait(1)

    tx_attack = attack.denialOfService(
        king_of_ether.address, {"from": accounts[2], "value": Web3.toWei(3, "ether")}
    )
    tx_attack.wait(1)

    with pytest.raises(exceptions.VirtualMachineError):
        tx_king4 = king_of_ether.becomeTheNewKing(
            {"from": accounts[3], "value": Web3.toWei(4, "ether")}
        )
        print(f"{king_of_ether.King()}")
        tx_king4.wait(1)


def test_fixed_king_of_ether():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("Only for local testing")
    # deploy contract
    king_of_ether, attack, fixed_king_of_ether = deploy_contract()

    # making new kings
    tx_king1 = fixed_king_of_ether.becomeTheNewKing(
        {"from": accounts[0], "value": Web3.toWei(1, "ether")}
    )
    print(f"{fixed_king_of_ether.King()}")
    tx_king1.wait(1)

    tx_king2 = fixed_king_of_ether.becomeTheNewKing(
        {"from": accounts[1], "value": Web3.toWei(2, "ether")}
    )
    print(f"{fixed_king_of_ether.King()}")
    tx_king2.wait(1)

    tx_attack = attack.denialOfService(
        fixed_king_of_ether.address,
        {"from": accounts[2], "value": Web3.toWei(3, "ether")},
    )
    tx_attack.wait(1)

    tx_king4 = fixed_king_of_ether.becomeTheNewKing(
        {"from": accounts[3], "value": Web3.toWei(4, "ether")}
    )
    print(f"{fixed_king_of_ether.King()}")
    tx_king4.wait(1)

    assert accounts[3].address == fixed_king_of_ether.King()
