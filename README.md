# NEO Workshop

This git repo contains some useful material to be used in NEO workshops.

Index:

* [Requirements](#requirements)
* [Set-up a NEO Private Net](#set-up-a-neo-private-net)
* [Wallets and JSON-RPC](#wallets-and-json-rpc)
  * [Linus and Margaret](#linus-and-margaret)
  * [Global Assets](#global-assets)
  * [JSON-RPC Examples](#json-rpc-examples)
* [Smart Contracts](#smart-contracts)
  * [Context](#context)
  * [Clone this Git Repository](#clone-this-git-repository)
  * [Setting two NEO Node CLIs](#setting-two-neo-node-clis)
  * [Compile](#compile)
  * [Deploy](#deploy)
  * [Invoke](#invoke)
  * [Testing different Scenarios](#testing-different-scenarios)

## Wallets and JSON-RPC

### Requirements

1. Reasonable internet connectivity. ;-)

2. You need to install Docker.
  - Windows: [this](https://docs.docker.com/docker-for-windows/install/) and [this](https://runnable.com/docker/install-docker-on-windows-10) links can help you install it and solve pitfalls.
  - MacOS: it's pretty easy, [this](https://docs.docker.com/docker-for-mac/install/) link is all you need.
  - Linux: also pretty easy, [this](https://docs.docker.com/install/linux/docker-ce/ubuntu/) link is all you need.

3. You need to install `curl`, or use a docker container that has curl installed. If you don't want to locally install `curl`, you can get a bash with curl using the following command: `docker run -it --name test-curl --network="host" maiwj/curl`.

### Set-up a NEO Private Net

```
$ git clone git@github.com:AxLabs/neo-privatenet-openwallet-docker.git
$ cd neo-privatenet-openwallet-docker
$ docker-compose up
```

Once you executed the `docker-compose` command, just leave the terminal window opened. It's useful if you want to see some logs or other bits and bytes. If you want to run in a "detached" mode, you can run the `docker-compose` with the `-d` flag, like `docker-compose up -d`.

If you want to start from scratch (deleting all the data of docker containers), just run the following command in the same directory:

```
$ docker-compose down
```

Then you can start everything again with the `docker-compose up` command.

### Linus and Margaret

#### Linus

Public Key: `031a6c6fbbdf02ca351745fa86b9ba5a9452d785ac4f7fc2b7548ca2a46c4fcf4a`

Private Key: `1dd37fba80fec4e6a6f13fd708d8dcb3b29def768017052f6c930fa1c5d90bbb`

Address: `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`

#### Margaret

Public Key: `0265bf906bf385fbf3f777832e55a87991bcfbe19b097fb7c5ca2e4025a4d5e5d6`

Private Key: `9117f4bf9be717c9a90994326897f4243503accd06712162267e77f18b49c3a3`

Address: `AKYdmtzCD6DtGx16KHzSTKY8ji29sMTbEZ`

### Global Assets

NEO: `c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b`

GAS: `602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7`

### JSON-RPC Examples

#### Get Account State

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

#### Get Block Info

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

#### Get New Address

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

#### Send assets to address

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

#### Send Raw Transaction

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

## Smart Contracts

The first step is to have the private net up and running, as described [here](#set-up-a-neo-private-net).

Once you executed the `docker-compose up -d` command, the following output should look something like this:

```
$ docker-compose up -d
Creating network "neo-privatenet-openwallet-docker_default" with the default driver
Creating neo-privatenet-openwallet-docker_neo-privnet_1 ... done
Creating neo-privatenet-openwallet-docker_postgresql_1  ... done
Creating neo-privatenet-openwallet-docker_neo-scan-openwallet_1 ... done
```

The name of the docker container running all the nodes is `neo-privatenet-openwallet-docker_neo-privnet_1`.

### Context

For demonstration and test purposes, we should spawn two NEO CLI (Command Line Interface) in the same docker container. Each NEO node CLI will be pointing to the same NEO privatenet network -- that was previously created in the `docker-compose` command.

It's advisable that you start the NEO Node CLIs in two different terminals.

### Clone this Git Repository

We will need the `neo-ans.py` contract.

```
$ git clone https://github.com/AxLabs/neo-workshop.git
$ cd neo-workshop
```

The `neo-ans.py` is under the. `contracts` directory.

### Setting two NEO Node CLIs

#### NEO Node - CLI 1

Open a new terminal window and execute:

```
$ docker exec -it neo-privatenet-openwallet-docker_neo-privnet_1 np-prompt -c /neo-python/neo/data/protocol.privnet-2.json
```

Wait the NEO node to sync (progress bar is in the bottom).

#### NEO Node - CLI 2

Open a new terminal window and execute:

```
$ docker exec -it neo-privatenet-openwallet-docker_neo-privnet_1 np-prompt -c /neo-python/neo/data/protocol.privnet-3.json
```

Wait the NEO node to sync (progress bar is in the bottom).

### Compile

1. Copy the `contracts/neo-ans.py` file to the docker container, with the following command:

```
$ docker cp ./contracts/neo-ans.py neo-privatenet-openwallet-docker_neo-privnet_1:/
```

This will copy the `contracts/neo-ans.py` to the root directory **INSIDE** the docker container (`/neo-ans.py`).

2. Go to the terminal of "CLI 1", and compile the contract with the following command:

```
neo> sc build /neo-ans.py
Saved output to /neo-ans.avm
```

The compiled `.avm` file is then saved on `/neo-ans.avm` **INSIDE** the docker container.

### Deploy

Follow these steps on the **CLI 1 terminal**.

1. First, open a wallet. There's always a wallet with plenty of NEO and GAS for testing purposes.

```
neo> wallet open /neo-python/neo-privnet.wallet
```

The password is `coz`.

2. Then, enable the CLI to print received events:

```
neo> config sc-events on
```

3. Deploy the previously compiled contract:

```
neo> sc deploy /neo-ans.avm True False False 070705 05
```

Once contract details are requested, such as "Contract Name", "Contract Version", etc., just fill as you wish.

Description of used parameters on the `sc deploy` command:

* Path: path to the contract's `.avm`
  * In this case, the respective `.avm` is located in the root directory of the docker container.
* Storage: boolean to determine if smart contract requires storage
  * In this case, yes, the ANS contract is using storage!
* Dynamic invoke: boolean to determine if smart contract requires dynamic invoke
  * We are not using dynamic invoke!
* Payable: boolean to determine if smart contract is payable
  * The ANS contract address is not receiving payment of assets, so, it's not payable.
* Params: input parameter types of the smart contract
  * The parameter types for the ANS contract is `string`, `string`, and `byte array`. The description of types and the respective hexadecimal can be found [here](https://docs.neo.org/en-us/sc/Parameter.html).
* ReturnType: (Optional) the return type of the smart contract output
  * The ANS contract is either returning a `boolean` or a `byte array`. Thus, we set the return type as `byte array` -- which we can represent booleans, anyway.

**IMPORTANT:** Take note of the contract address, which is displayed as the output of the `sc deploy` command. You can find it as a hexadecimal string in the "hash" attribute.

### Invoke

Now that the contract is deployed, it's possible to interact with it.

In the **CLI 1 terminal**, register a name for the wallet's address:

```
neo> sc invoke 0xc4497e3f01d2efb02489be0b63072d5df8b1f8bc register test.neo AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
```

Where:

* `0xc4497e3f01d2efb02489be0b63072d5df8b1f8bc`: contract address
* `register`: the first parameter to the smart contract, which is the registration operation
* `test.neo`: the second parameter to the smart contract, which `test.neo` is the name we want to register
* `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`: the third parameter to the contract, which is the address we would like to associate with `test.neo`.

Important:

The address for the `register` operation, in this case `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`, should be the same address we have in the wallet for CLI 1 terminal. If it's not, this call will fail.

### Testing different Scenarios

#### Does the register really worked?

Just to make sure that the registration really worked and is persisted on-chain, it's possible to use JSON-RPC to perform a `query` operation on the `test.neo` name.

Open a new terminal, and execute the following `cURL` command:

```
curl -X POST \
  http://127.0.0.1:30333/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "jsonrpc": "2.0",
  "method": "invoke",
  "params":[
    "0xc4497e3f01d2efb02489be0b63072d5df8b1f8bc",
    [{"type": "String", "value": "query"},{"type": "String", "value": "test.neo"}{"type": "ByteArray", "value": ""}]
  ],
  "id": 1
}'
```

The result should be something like:

```
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "script": "0008746573742e6e656f05717565727967bcf8b1f85d2d07630bbe8924b0efd2013f7e49c4",
        "state": "HALT",
        "gas_consumed": "0.141",
        "stack": [
            {
                "type": "ByteArray",
                "value": "23ba2703c53263e8d6e522dc32203339dcd8eee9"
            }
        ]
    }
}
```

Where `23ba2703c53263e8d6e522dc32203339dcd8eee9` is the script for the address `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`.

Naturally, it's also possible to invoke the `query` in the CLI. For example:

```
neo> sc invoke 0xc4497e3f01d2efb02489be0b63072d5df8b1f8bc query test.neo ''
```

#### What if another address/wallet tries to delete `test.neo`?

1. In the **CLI 2 terminal**, create a new wallet:

```
neo> wallet create /neo-python/new.wallet
```

Set any password that you can remember for testing purposes.

An address like `AHbrpfNZGuNAeXrFwiea7CXTwqmS3imwz7` will be generated, and you will be able to see in the output of the `wallet create` command.

2. Just that the new address gets some GAS to invoke the `delete` operation successfully, go to the `CLI 1 terminal` and send 100 GAS to it:

```
neo> wallet send GAS AHbrpfNZGuNAeXrFwiea7CXTwqmS3imwz7 100
```

where `AHbrpfNZGuNAeXrFwiea7CXTwqmS3imwz7` is the new address created in the **CLI 2 terminal**.

The password, as mentioned above, is `coz`.

3. In the **CLI 2 terminal**, invoke the operation to delete `test.neo`:

```
neo> sc invoke 0xc4497e3f01d2efb02489be0b63072d5df8b1f8bc delete test.neo ''
```

The password is the one when you created the wallet.

4. Follow the steps described on [Does the register really worked?](#does-the-register-really-worked?) section to check with JSON-RPC whether the `test.neo` was deleted or not.
