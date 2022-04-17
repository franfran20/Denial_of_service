//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

//denial of service

contract KingOfEther{
    address public King;
    uint256 public ContractBalance;

    function becomeTheNewKing() public payable{
        require(msg.value > ContractBalance, "You can do better!");
        ContractBalance = address(this).balance;

        (bool sent, ) = King.call{value: ContractBalance}("");
        require(sent);

        ContractBalance= msg.value;
        King = msg.sender;
    }
    
}