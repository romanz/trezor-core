
from micropython import const

# _NEM_LEVY_PERCENTILE_DIVISOR = const(4)
#
# _NEM_MAX_DIVISIBILITY = const(6)
# _NEM_MAX_SUPPLY = const(9000000000)
#
_NEM_NETWORK_MAINNET = const(0x68)
_NEM_NETWORK_TESTNET = const(0x98)
_NEM_NETWORK_MIJIN = const(0x60)

# _NEM_ADDRESS_SIZE = const(40)
# _NEM_ADDRESS_SIZE_RAW = const(25)
#
# _NEM_TRANSACTION_TYPE_TRANSFER = const(0x0101)
# _NEM_TRANSACTION_TYPE_IMPORTANCE_TRANSFER = const(0x0801)
# _NEM_TRANSACTION_TYPE_AGGREGATE_MODIFICATION = const(0x1001)
# _NEM_TRANSACTION_TYPE_MULTISIG_SIGNATURE = const(0x1002)
# _NEM_TRANSACTION_TYPE_MULTISIG = const(0x1004)
# _NEM_TRANSACTION_TYPE_PROVISION_NAMESPACE = const(0x2001)
# _NEM_TRANSACTION_TYPE_MOSAIC_CREATION = const(0x4001)
# _NEM_TRANSACTION_TYPE_MOSAIC_SUPPLY_CHANGE = const(0x4002)
#
# _NEM_SALT_SIZE = const(sizeof(ed25519_public_key))
#
# _NEM_ENCRYPTED_SIZE = const(size)         (((size) + AES_BLOCK_SIZE) / AES_BLOCK_SIZE * AES_BLOCK_SIZE))
# _NEM_ENCRYPTED_PAYLOAD_SIZE = const(size) (AES_BLOCK_SIZE + NEM_SALT_SIZE + NEM_ENCRYPTED_SIZE(size)))
#
# __NEM_PADDING_SIZE = const(buffer, size)  ((buffer)[(size) - 1]))
# _NEM_PADDING_SIZE = const(buffer, size)   (_NEM_PADDING_SIZE(buffer, size) > (size) ? (size) : _NEM_PADDING_SIZE(buffer, size)))
#
# _NEM_DECRYPTED_SIZE = const(buffer, size) ((size) - NEM_PADDING_SIZE(buffer, size)))


def nem_validate_network(network):
    if network in (_NEM_NETWORK_MAINNET, _NEM_NETWORK_TESTNET, _NEM_NETWORK_MIJIN):
        return network
    if network is None:
        return _NEM_NETWORK_MAINNET
    raise ValueError('Invalid NEM network')

#
# def nem_check_network(network):
#     if network == _NEM_NETWORK_MAINNET:
#         return "NEM Mainnet"
#     if network == _NEM_NETWORK_TESTNET:
#         return "NEM Testnet"
#     if network == _NEM_NETWORK_MIJIN:
#         return "Mijin"
#
#     raise ValueError('Invalid NEM network')
