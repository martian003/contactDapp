from web3 import Web3, HTTPProvider
import json
import time

def connect_with_blockchain(acc):
    rpcServer = "http://127.0.0.1:7545"
    web3 = Web3(HTTPProvider(rpcServer))
    print('connected a blockchain')

    if acc == 0:
        web3.eth.defaultAccount = web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount = web3.eth.accounts[acc]

    with open(r'C:\Users\rohit raj\Desktop\ContractDaap\build\contracts\contact.json') as f:
        contract_json = json.load(f)
        contract_abi = contract_json['abi']
        contract_address = contract_json['networks']['5777']['address']

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    return(contract,web3)

try:
    contract,web3 = connect_with_blockchain(0)
    print("Sending Transation....\n")
    tx_hash = contract.functions.insertContact("Rohit", "6206699427", "abc@gmail.com", "Google").transact({'from': web3.eth.defaultAccount})
    print(f"Transation Hash: {tx_hash.hex()}\n")
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("This contact information was added successfully")
        
except Exception as e:
    print("This contact is already available");

contract,web3 = connect_with_blockchain(0)

name, mobile, email, org = contract.functions.viewContacts().call()
print(name)
print(mobile)
print(email)
print(org)