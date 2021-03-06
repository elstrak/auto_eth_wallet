from web3.middleware import geth_poa_middleware
from web3 import Web3
import time
from requests import Session
from pyuseragents import random as random_useragent

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
masterWalletUrl = 'https://k6qd41buh0.execute-api.us-east-1.amazonaws.com/prod/register-master-wallet'
session = Session()
session.headers.update({'user-agent': random_useragent(), 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,vi;q=0.8,es;q=0.7', 'referer': 'https://landsale.minesofdalarnia.com/'})

def create_wallet(quantity):
    file = open('wallets.txt', "w")

    for i in range(quantity):
        account = w3.eth.account.create()
        privatekey = str(account.privateKey.hex())
        address = str(account.address)
        file.write(str(address)+":"+str(privatekey)+"\n")

    file.close()

if __name__ == "__main__":
    print('1 - Генерировать кошельки\n')
    choice = input()
    if choice == '1':
        print('Введите количество')
        quantity = int(input())
        create_wallet(quantity)
        print('Кошельки сгенерированы в формате адрес:private key')

