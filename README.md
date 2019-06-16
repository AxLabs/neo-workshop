# NEO Workshop

This git repo contains some useful material to be used in NEO workshops.

Index:

1. [Wallets: Linus and Margaret](#wallets-linus-and-margaret)
2. [Global Assets](#global-assets)
3. [JSON-RPC Examples](#json-rpc-examples)

## Requirements

1. Reasonable internet connectivity. ;-)

2. You need to install Docker.
  - Windows: [this](https://docs.docker.com/docker-for-windows/install/) and [this](https://runnable.com/docker/install-docker-on-windows-10) links can help you install it and solve pitfalls.
  - MacOS: it's pretty easy, [this](https://docs.docker.com/docker-for-mac/install/) link is all you need.
  - Linux: also pretty easy, [this](https://docs.docker.com/install/linux/docker-ce/ubuntu/) link is all you need.

3. You need to install `curl`, or use a docker container that has curl installed. If you don't want to locally install `curl`, you can get a bash with curl using the following command: `docker run -it --name test-curl --network="host" maiwj/curl`.

## Set-up a NEO Private Net

```
$ git clone git@github.com:AxLabs/neo-privatenet-openwallet-docker.git
$ cd neo-privatenet-openwallet-docker
$ docker-compose up
```

Once you executed the `docker-compose` command, just leave the terminal window opened. It's useful if you want to see some logs or other bits and bytes. If you want to run in a "detached" mode, you can run the `docker-compose` with the `-d` flag, like `docker-compose up -d`.

If you want to start from scratch (deleting all the data of docker containers), just run the following command in the same direcotry:

```
$ docker-compose down
```

Then you can start everything again with the `docker-compose up` command.

## Wallets: Linus and Margaret

### Linus

Public Key: `031a6c6fbbdf02ca351745fa86b9ba5a9452d785ac4f7fc2b7548ca2a46c4fcf4a`

Private Key: `1dd37fba80fec4e6a6f13fd708d8dcb3b29def768017052f6c930fa1c5d90bbb`

Address: `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`

### Margaret

Public Key: `0265bf906bf385fbf3f777832e55a87991bcfbe19b097fb7c5ca2e4025a4d5e5d6`

Private Key: `9117f4bf9be717c9a90994326897f4243503accd06712162267e77f18b49c3a3`

Address: `AKYdmtzCD6DtGx16KHzSTKY8ji29sMTbEZ`

## Global Assets

NEO: `c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b`

GAS: `602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7`

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

### Get New Address

```
curl -X POST \
  http://127.0.0.1:30333/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "jsonrpc": "2.0",
  "method": "getnewaddress",
  "params":[],
  "id": 1
}'
```

### Send assets to address

```
curl -X POST \
  http://127.0.0.1:30333/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "jsonrpc": "2.0",
  "method": "sendtoaddress",
  "params":["c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b", "ARanVBAy27qR9NPmxJfwEw16fzqXEDV9em", "10.0"],
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

