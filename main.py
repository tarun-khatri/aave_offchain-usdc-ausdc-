from web3 import Web3
from data_collector import DataCollector
from calculator import Calculator
from dotenv import load_dotenv
import os

load_dotenv()


INFURA_URL = os.getenv("INFURA_URL")

USDC_ADDRESS = Web3.to_checksum_address("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")

def main():
    print("Connecting to Ethereum network...")
    collector = DataCollector(INFURA_URL)

    print("Fetching reserve data...")
    reserve_data = collector.get_reserve_data(USDC_ADDRESS)

    calculator = Calculator(reserve_data)

    print("\n--- Aave Exchange Calculator ---")
    token_type = input("Enter the token type (USDC or aUSDC): ").strip().upper()
    amount = float(input("Enter the amount: "))

    if token_type == "USDC":
        ausdc_amount = calculator.calculate_ausdc_from_usdc(amount)
        print(f"{amount} USDC is equivalent to {ausdc_amount:.6f} aUSDC.")
    elif token_type == "AUSDC":
        usdc_amount = calculator.calculate_usdc_from_ausdc(amount)
        print(f"{amount} aUSDC is equivalent to {usdc_amount:.6f} USDC.")
    else:
        print("Invalid token type. Please enter either 'USDC' or 'aUSDC'.")

if __name__ == "__main__":
    main()
