# NEO Workshop

This git repo contains some useful material to be used in NEO workshops.

Index:

1. [Wallets: Linus and Margaret](#wallets-linus-and-margaret)
2. [JSON-RPC Examples](#json-rpc-examples)

## Wallets: Linus and Margaret

### Linus

Public Key: `031a6c6fbbdf02ca351745fa86b9ba5a9452d785ac4f7fc2b7548ca2a46c4fcf4a`
Private Key: `1dd37fba80fec4e6a6f13fd708d8dcb3b29def768017052f6c930fa1c5d90bbb`
Address: `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`

### Margaret

Public Key: `0265bf906bf385fbf3f777832e55a87991bcfbe19b097fb7c5ca2e4025a4d5e5d6`
Private Key: `9117f4bf9be717c9a90994326897f4243503accd06712162267e77f18b49c3a3`
Address: `AKYdmtzCD6DtGx16KHzSTKY8ji29sMTbEZ`

## JSON-RPC Examples

### Get Account State

```
curl -X POST \
  http://127.0.0.1:30333/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "jsonrpc": "2.0",
  "method": "getaccountstate",
  "params":["AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"],
  "id": 1
}'
```

### Get Block Info

```
curl -X POST \
  http://127.0.0.1:30333/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "jsonrpc": "2.0",
  "method": "getblock",
  "params":[2007, 1],
  "id": 1
}'

```

### Send Raw Transaction

```
curl -X POST \
  http://127.0.0.1:30333/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "jsonrpc": "2.0",
  "method": "sendrawtransaction",
 "params":["80000001ff8c509a090d440c0e3471709ef536f8e8d32caa2488ed8c64c6f7acf1d1a44b0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500e40b5402000000295f83f83fc439f56e6e1fb062d89c6f538263d79b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc5001cb51bf086230023ba2703c53263e8d6e522dc32203339dcd8eee90141400a5f1a135394d77c44391da23d119d65ecaa2ec618c69ce96daebe0386d61681ef72a5b4c1683445ce3772c0ab5a06a600e4846506e7f811c0204acc333083042321031a6c6fbbdf02ca351745fa86b9ba5a9452d785ac4f7fc2b7548ca2a46c4fcf4aac"],
  "id": 1
}'
```

