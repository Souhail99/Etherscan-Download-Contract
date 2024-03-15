# Etherscan-Download-Contract

This guide provides instructions on how to set up the code.

The code is implemented in Python and I use Etherscan API.

## Information :

With code you can download any Smart contract from ethereum (and available on etherscan) in .sol format (change the extension if you want txt).


## On your side :

You need an ETHERSCAN API key (Ethereum Blockchain Explorer) and a Smart Contract address.

The fields to be replaced are :

1. :
```python
etherscan_api_key ="YOUR_ETHERSCAN_API_KEY"
```

2. :
```python
adresse_contrat = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
```
### Option :

The same logic applies to BSCSCAN! You just need to replace the query :
```python
 url ="https://api.bscscan.com/api?module=contract&action=getsourcecode&address="+adresse_contrat+"&apikey="+bscscan_api_key
```

And you need to create this value : 
```python
 bscscan_api_key = "YOUR_BSCSCAN_API_KEY"
```