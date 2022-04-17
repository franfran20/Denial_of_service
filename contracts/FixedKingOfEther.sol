//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract FixedKingOfEther{
    address public King;
    uint256 public ContractBalance;
    mapping(address => uint256) public balance;

    function becomeTheNewKing() public payable{
        require(msg.value > ContractBalance, "You can do better!");

        balance[King] += ContractBalance;

        ContractBalance = msg.value;
        King = msg.sender;
    }

    function claimBalance() public{
        require(msg.sender != King, "You're the current king mahn!");
        require(balance[msg.sender] > 0);
        uint amount = balance[msg.sender];

        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "tx failed");
    }
    
}