from trezor.crypto import base58, hashlib
from trezor.messages.LiquidPublicKey import LiquidPublicKey

from apps.common import paths, seed
from apps.common.layout import address_n_to_str, show_address, show_qr


async def get_public_key(ctx, msg, keychain):
    # TODO: check path (for sanity)
    node = keychain.derive(msg.address_n, curve_name='secp256k1')
    return LiquidPublicKey(pubkey=node.public_key())
