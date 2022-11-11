// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract SimpleStorage {
    uint storedData;

    // Sets the value 
    function set(uint x) public {
        storedData = x;
    }

    // Gets the value
    function get() public view returns (uint) {
        return storedData;
    }
}
