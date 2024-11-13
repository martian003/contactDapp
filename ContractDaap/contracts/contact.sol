// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract contact {
  address owner; //state var
  string[] names;
  string[] mobiles;
  string[] emails;
  string[] orgainizations;
  mapping(string=>bool) _contacts;
  constructor() public{
    owner=msg.sender; //global var,storing owner address
  }
  modifier onlyOwner{  //function modifier only owner can save the contact/telegram uses blockchain
  require((owner==msg.sender));
  _;
  }
  //inserting the contact into the daap
  function insertContact(string memory name,string memory mobile,string memory email,string memory org)public onlyOwner{
    require((!_contacts[mobile])); //if mobile no is not in contact,like _contacts['9000067888]->false
    names.push(name);
    mobiles.push(mobile);
    emails.push(email);
    orgainizations.push(org);
    _contacts[mobile]=true;
  }
  //read contact from blockchain
  function viewContacts() public view returns(string[] memory,string[] memory,string[] memory,string[] memory){
    return(names,mobiles,emails,orgainizations);
  }
}
