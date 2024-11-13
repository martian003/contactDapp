# # from flask import Flask,render_template #flask is a lib and Flask is a class
# # object=Flask(__name__)
# # if __name__=="__main__":
# #     app.run(host='0.0.0.0',port=5001,debug=True)
# from flask import Flask, render_template,request #flask is a lib and Flask is class
# from web3 import Web3,HTTPProvider #web3 is a bridge between python and blockchain

# #create an object
# app = Flask(__name__)
# @app.route('/insertcontact',methods=["post"]) #handler handling home '/'
# def insertcontact():
#     name=request.form["name"]
#     mobile=request.form['mobile']
#     email=request.form['email']
#     org=request.form['org']
#     print(name,mobile,email,org)
#     return render_template("index.html")

#     #access blockchain
#     # try:
#     #     contract,web3=connect_with_blockchain(0)
#     #     tx_hash=contract.functions.insertContact(name,mobile,email)
#     #     web3.eth.wait_for_transaction_receipt(tx_hash)
#     #     return render_template('index.html',res='this contact is ')
#     # except:
#     #     return
# # def hompage(): #handler fuunction
#     # return render_template("index.html")
#     # return "Hello World"

# if __name__ =="__main__":
#     app.run(host='0.0.0.0', port='5001', debug=True)

# from flask import Flask, render_template, request

# app = Flask(_name_)

# @app.route('/')
# def home():
#     # return "Hello, World!"
#     return render_template("index.html")
#     # return render_template("home.html")

# @app.route('/insertContact', methods=["post"]) #get the data from the thml 
# def insertContact():
#     name=request.form['name']
#     mobile=request.form['mobile']
#     email=request.form['email']
#     org = request.form['org']

#     print(name, mobile, email, org)
#     return render_template("index.html")

# if _name_ == "_main_":
#     app.run(host='0.0.0.0', port=5001, debug=True)


from flask import Flask, render_template, request
from web3 import Web3
import json

app = Flask(__name__)

# Connect to Ganache
def connect_with_blockchain():
    rpc_server = "http://127.0.0.1:7545"  # Change if your Ganache is running on a different port
    web3 = Web3(Web3.HTTPProvider(rpc_server))
    print('Connected to blockchain:', web3.isConnected())

    # Load the contract
    with open(r'C:\Users\rohit raj\Desktop\ContractDaap\build\contracts\contact.json') as f:
        contract_json = json.load(f)
        contract_abi = contract_json['abi']
        contract_address = contract_json['networks']['5777']['address']

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    return contract, web3

# Home route
@app.route('/')
def home():
    contract, web3 = connect_with_blockchain()
    name, mobile, email, org = contract.functions.viewContacts().call()

    contacts = zip(name, mobile, email, org)
    return render_template('index.html', contacts=contacts)

# Insert contact route
@app.route('/insertContact', methods=["POST"])
def insertContact():
    name = request.form['name']
    mobile = request.form['mobile']
    email = request.form['email']
    org = request.form['org']

    contract, web3 = connect_with_blockchain()

    try:
        tx_hash = contract.functions.insertContact(name, mobile, email, org).transact({
            'from': web3.eth.accounts[0]  # Use the first account from Ganache
        })
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Contact {name} added successfully")

    except Exception as e:
        print(f"Error: {e}")

    return home()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)