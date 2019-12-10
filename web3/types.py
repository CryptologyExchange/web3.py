from typing import (
    Any,
    Callable,
    Dict,
    List,
    NewType,
    Optional,
    Sequence,
    TypeVar,
    Union,
)

from eth_typing import (
    Address,
    BlockNumber,
    ChecksumAddress,
    Hash32,
    HexStr,
)
from hexbytes import (
    HexBytes,
)
from typing_extensions import (
    Literal,
)

from web3._utils.compat import (
    TypedDict,
)
from web3.datastructures import (
    NamedElementOnion,
)

Wei = NewType('Wei', int)
TReturn = TypeVar("TReturn")
TParams = TypeVar("TParams")
TValue = TypeVar("TValue")

Nonce = NewType("Nonce", int)

HexBytes32 = NewType("HexBytes32", HexBytes)
HexStr32 = NewType("HexStr32", HexStr)

_Hash32 = Union[Hash32, HexBytes, HexStr]

# todo: move these to eth_typing once web3 is type hinted
ABIEventParams = TypedDict("ABIEventParams", {
    "name": str,
    "type": str,
    "indexed": bool,
})

ENS = NewType("ENS", str)

ABIEvent = TypedDict("ABIEvent", {
    "type": "event",
    "name": str,
    "inputs": Sequence[ABIEventParams],
    "anonymous": bool,
})


ABIFunctionComponents = TypedDict("ABIFunctionParams", {
    "name": str,
    "type": str,
    "components": Sequence["ABIFunctionComponents"],
}, total=False)


ABIFunctionParams = TypedDict("ABIFunctionParams", {
    "name": str,
    "type": str,
    "components": Sequence[ABIFunctionComponents],
}, total=False)


ABIFunction = TypedDict("ABIFunction", {
    "type": Union["function", "constructor", "fallback"],
    "name": str,
    "inputs": Sequence[ABIFunctionParams],
    "outputs": Sequence[ABIFunctionParams],
    "stateMutability": Union["pure", "view", "nonpayable", "payable"],
    "payable": bool,
    "constant": bool,
}, total=False)


ABIElement = Union[ABIFunction, ABIEvent]


ABI = Sequence[Union[ABIFunction, ABIEvent]]


LatestBlockParam = Literal["latest"]


BlockParams = Literal["latest", "earliest", "pending"]


BlockIdentifier = Union[BlockParams, BlockNumber, Hash32, HexStr]


ENS = NewType("ENS", str)


EnodeURI = NewType("EnodeURI", str)


EventData = TypedDict("EventData", {
    "args": Dict[str, Any],
    "event": str,
    "logIndex": int,
    "transactionIndex": int,
    "transactionHash": Hash32,
    "address": ChecksumAddress,
    "blockHash": Hash32,
    "blockNumber": int,
})


RPCError = TypedDict("RPCError", {
    "code": int,
    "message": str,
})


RPCResponse = TypedDict("RPCResponse", {
    "id": int,
    "jsonrpc": Literal["2.0"],
    "result": Any,
    "error": RPCError,
}, total=False)


RPCEndpoint = NewType("RPCEndpoint", str)


Formatters = Dict[RPCEndpoint, Callable[..., Any]]


FormattersDict = TypedDict("FormattersDict", {
    "request_formatters": Formatters,
    "result_formatters": Formatters,
    "error_formatters": Formatters,
}, total=False)


FilterParams = TypedDict("FilterParams", {
    "fromBlock": Union["earliest", "pending", "latest", BlockNumber],
    "toBlock": Union["earliest", "pending", "latest", BlockNumber],
    "address": Union[Address, ChecksumAddress, List[Union[Address, ChecksumAddress]]],
    "topics": List[Optional[Union[Hash32, List[Hash32]]]],
}, total=False)


TxParams = TypedDict("TxParams", {
    "nonce": Nonce,
    "gasPrice": Wei,
    "gas": Wei,
    "from": Union[Address, ChecksumAddress, str],
    "to": Union[Address, ChecksumAddress, str],
    "value": Wei,
    "data": Union[bytes, HexStr],
}, total=False)

SignedTx = TypedDict("SignedTx", {
    "raw": bytes,
    "tx": TxParams,
}, total=False)

# this Any should be updated to Web3 once all type hints land
GasPriceStrategy = Callable[[Any, TxParams], Wei]
# 2 input to parent callable Any should be updated to Web3 once all type hints land
Middleware = Callable[[Callable[[RPCEndpoint, Any], RPCResponse], Any], Any]
MiddlewareOnion = NamedElementOnion[str, Middleware]


LogReceipt = TypedDict("LogReceipt", {
    "address": ChecksumAddress,
    "blockHash": Hash32,
    "blockNumber": int,
    "data": HexStr,
    "logIndex": int,
    "removed": bool,
    "topics": List[Hash32],
    "transactionHash": Hash32,
    "transactionIndex": int,
})


StorageProof = TypedDict("StorageProof", {
    'key': HexStr,
    'value': Hash32,
    'proof': Sequence[HexStr],
})


MerkleProof = TypedDict("MerkleProof", {
    'address': ChecksumAddress,
    'accountProof': Sequence[HexStr],
    'balance': int,
    'codeHash': Hash32,
    'nonce': Nonce,
    'storageHash': Hash32,
    'storageProof': Sequence[StorageProof],
})


Protocol = TypedDict("Protocol", {
    "difficulty": int,
    "head": HexStr,
    "network": int,
    "version": int,
})

NodeInfo = TypedDict("NodeInfo", {
    'enode': EnodeURI,
    'id': HexStr,
    'ip': str,
    'listenAddr': str,
    'name': str,
    'ports': Dict[str, int],
    'protocols': Dict[str, Protocol],
})


Peer = TypedDict("Peer", {
    'caps': Sequence[str],
    'id': HexStr,
    'name': str,
    'network': Dict[str, str],
    'protocols': Dict[str, Protocol],
}, total=False)


SyncStatus = TypedDict("SyncStatus", {
    'currentBlock': int,
    'highestBlock': int,
    'knownStates': int,
    'pulledStates': int,
    'startingBlock': int,
})


Timestamp = NewType("Timestamp", int)


TxReceipt = TypedDict("TxReceipt", {
    "blockHash": Hash32,
    "blockNumber": int,
    "contractAddress": Optional[ChecksumAddress],
    "cumulativeGasUsed": int,
    "gasUsed": Wei,
    "from": ChecksumAddress,
    "logs": List[LogReceipt],
    "logsBloom": HexBytes,
    "root": HexStr,
    "status": int,
    "to": ChecksumAddress,
    "transactionHash": Hash32,
    "transactionIndex": int,
})


BlockData = TypedDict("BlockData", {
    'difficulty': int,
    'extraData': HexStr,
    'gasLimit': Wei,
    'gasUsed': Wei,
    'hash': Hash32,
    'logsBloom': HexStr,
    'miner': ChecksumAddress,
    'nonce': HexStr,
    'number': BlockNumber,
    'parentHash': Hash32,
    'receiptRoot': Hash32,
    'sha3Uncles': Hash32,
    'size': int,
    'stateRoot': Hash32,
    'timestamp': Timestamp,
    'totalDifficulty': int,
    'transactions': Union[Sequence[Hash32], Sequence[TxReceipt]],
    'transactionsRoot': Hash32,
    'uncles': Sequence[Hash32],
})


Uncle = TypedDict("Uncle", {
    'author': ChecksumAddress,
    'difficulty': HexStr,
    'extraData': HexStr,
    'gasLimit': HexStr,
    'gasUsed': HexStr,
    'hash': Hash32,
    'logsBloom': HexStr,
    'miner': Hash32,
    'mixHash': Hash32,
    'nonce': HexStr,
    'number': HexStr,
    'parentHash': Hash32,
    'receiptsRoot': Hash32,
    'sealFields': Sequence[HexStr],
    'sha3Uncles': Hash32,
    'size': int,
    'stateRoot': Hash32,
    'timestamp': Timestamp,
    'totalDifficulty': HexStr,
    'transactions': Sequence[Hash32],
    'transactionsRoot': Hash32,
    'uncles': Sequence[Hash32]
})

# shh

ShhID = NewType("ShhID", HexStr)
ShhFilterID = NewType("ShhFilterID", HexStr)
ShhSubscriptionID = NewType("ShhSubscriptionID", HexStr)

ShhMessageFilter = TypedDict("ShhMessageFilter", {
    "symKeyID": ShhID,
    "privateKeyID": ShhID,
    "sig": str,
    "minPoW": float,
    "topics": List[HexStr],
    "allowP2P": bool,
}, total=False)


ShhMessage = TypedDict("ShhMessage", {
    "from": bytes,
    "hash": HexBytes,
    "recipient": bytes,
    "ttl": int,
    "topic": HexBytes,
    "timestamp": int,
    "payload": HexBytes,
    "padding": HexBytes,
    "pow": float,
    "recipientPublicKey": ShhID,
}, total=False)


ShhMessageParams = TypedDict("ShhMessageParams", {
    "symKeyID": ShhID,
    "pubKey": str,
    "ttl": int,
    "sig": str,
    "topic": str,
    "payload": str,
    "padding": str,
    "powTime": int,
    "powTarget": float,
    "targetPeer": ShhID,
}, total=False)

ShhStats = TypedDict("ShhStats", {
    'maxMessageSize': int,
    'memory': int,
    'messages': int,
    'minPow': float,
}, total=False)

# txpool types
PendingTx = TypedDict("PendingTx", {
    "blockHash": HexBytes,
    "blockNumber": None,
    "from": ChecksumAddress,
    "gas": HexBytes,
    "gasPrice": HexBytes,
    "hash": HexBytes,
    "input": HexBytes,
    "nonce": HexBytes,
    "to": ChecksumAddress,
    "transactionIndex": None,
    "value": HexBytes,
}, total=False)


TxPoolContent = TypedDict("TxPoolContent", {
    "pending": Dict[ChecksumAddress, Dict[Nonce, List[PendingTx]]],
    "queued": Dict[ChecksumAddress, Dict[Nonce, List[PendingTx]]],
}, total=False)


TxPoolInspect = TypedDict("TxPoolInspect", {
    "pending": Dict[ChecksumAddress, Dict[Nonce, str]],
    "queued": Dict[ChecksumAddress, Dict[Nonce, str]],
}, total=False)


TxPoolStatus = TypedDict("TxPoolStatus", {
    "pending": int,
    "queued": int,
}, total=False)


# web3.parity types
ParityBlockTrace = NewType("ParityBlockTrace", Dict[str, Any])
ParityFilterTrace = NewType("ParityFilterTrace", Dict[str, Any])
ParityMode = Literal["active", "passive", "dark", "offline"]
ParityTraceMode = Sequence[Literal["trace", "vmTrace", "stateDiff"]]
ParityNetPeers = TypedDict("ParityNetPeers", {
    "active": int,
    "connected": int,
    "max": int,
    "peers": List[Dict[Any, Any]],
})
ParityFilterParams = TypedDict("ParityFilterParams", {
    "fromBlock": BlockIdentifier,
    "toBlock": BlockIdentifier,
    "fromAddress": Sequence[Union[Address, ChecksumAddress, ENS]],
    "toAddress": Sequence[Union[Address, ChecksumAddress, ENS]],
    "after": int,
    "count": int,
}, total=False)