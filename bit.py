import requests
import argparse

BITAPS_API_BASE = "https://api.bitaps.com/btc/testnet/v1"

# Your faucet wallet private key or API credentials here (handle securely)
FAUCET_WALLET_PRIVATE_KEY = "your_faucet_wallet_private_key"

def send_tbtc(to_address, amount_satoshi):
    # This is a simplified example. You need to create and sign the transaction properly.
    # Bitaps API documentation should be referred for exact params and signing process.
    
    # Example endpoint to send transaction (pseudo-code)
    url = f"{BITAPS_API_BASE}/send/transaction"
    
    payload = {
        "from_private_key": FAUCET_WALLET_PRIVATE_KEY,
        "to_address": to_address,
        "amount": amount_satoshi
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Transaction sent successfully:", response.json())
    else:
        print("Failed to send transaction:", response.text)

def main():
    parser = argparse.ArgumentParser(description="Bitaps TBTC Faucet CLI")
    parser.add_argument("address", help="Recipient TBTC address")
    parser.add_argument("--amount", type=int, default=100000, help="Amount in satoshi to send (default 0.001 TBTC)")
    args = parser.parse_args()
    
    send_tbtc(args.address, args.amount)

if __name__ == "__main__":
    main()
