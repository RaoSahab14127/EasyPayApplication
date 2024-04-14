from flask import Flask, request

from moralis import evm_api
import json
import os


app = Flask(__name__)
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6ImI0YjY0MTY4LTVjYzUtNDAzMi04MDFmLTljOGM3NWJhNzRjMSIsIm9yZ0lkIjoiMzc0NTk1IiwidXNlcklkIjoiMzg0OTU3IiwidHlwZUlkIjoiYjhhYmI3M2ItMDUzNi00OTRkLTlhNDYtYmM2ZTMzM2UzNzFmIiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3MDY0MzA0MDUsImV4cCI6NDg2MjE5MDQwNX0.hjAKrflxzt9pBmDJCNs0PjCLSq6P27GOFzjv7IT0QbU"


@app.route("/get_token_balance", methods=["GET"])
def get_tokens():
    chain = request.args.get("chain")
    address = request.args.get("address")

    params = {
        "address": address,
        "chain": chain,
    }
    result = evm_api.balance.get_native_balance(
        api_key=api_key,
        params=params,
    )

    return result


@app.route("/get_user_nfts", methods=["GET"])
def get_nfts():
    address = request.args.get("address")
    chain = request.args.get("chain")
    params = {
        "address": address,
        "chain": chain,
        "format": "decimal",
        "limit": 100,
        "token_addresses": [],
        "cursor": "",
        "normalizeMetadata": True,
    }

    result = evm_api.nft.get_wallet_nfts(
        api_key=api_key,
        params=params,
    )

    # converting it to json because of unicode characters
    response = json.dumps(result, indent=4)
    print(response)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
