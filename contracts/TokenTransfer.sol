// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TokenTransfer {
    ERC20 private _token;

    constructor (ERC20 token) public {
        _token = token;
    }

    function tokenTransfer(address receipient, uint256 amount) external {
        _token.transferFrom(address(this), receipient, amount);
    }
}