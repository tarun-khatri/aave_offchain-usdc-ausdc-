from dotenv import load_dotenv
import os
from web3 import Web3
import json

load_dotenv()

class DataCollector:
    def __init__(self, infura_url):
        
        self.web3 = Web3(Web3.HTTPProvider(os.getenv("INFURA_URL")))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to the Ethereum network.")

       
        self.lending_pool_address = Web3.to_checksum_address(os.getenv(
            "LENDING_POOL_ADDRESS"
        ))
        
        try:
            with open("lending_pool_abi.json", "r") as abi_file:
                abi_data = json.load(abi_file)
                self.lending_pool_abi = abi_data["abi"]
        except FileNotFoundError:
            raise FileNotFoundError("ABI file 'lending_pool_abi.json' not found.")
        except KeyError:
            raise KeyError("Invalid ABI file format. Missing 'abi' key.")

        self.lending_pool_contract = self.web3.eth.contract(
            address=self.lending_pool_address,
            abi=self.lending_pool_abi
        )

    def get_latest_block(self):
        try:
            return self.web3.eth.block_number
        except Exception as e:
            raise Exception(f"Error fetching latest block: {str(e)}")

    def get_reserve_data(self, asset_address):
        try:
            checksum_address = Web3.to_checksum_address(asset_address)
            print(f"Fetching data for asset: {checksum_address}")
            
            reserve_data = self.lending_pool_contract.functions.getReserveData(checksum_address).call()
            print(f"Raw Reserve Data: {reserve_data}")
            return reserve_data
            
        except Exception as e:
            print(f"Error: {str(e)}")
            raise Exception(f"Error fetching reserve data for asset {asset_address}: {str(e)}")
    
    def get_liquidity_rate(self, asset_address):
        try:
            reserve_data = self.get_reserve_data(asset_address)
            return reserve_data[2]
        except Exception as e:
            raise Exception(f"Error fetching liquidity rate for asset {asset_address}: {str(e)}")
