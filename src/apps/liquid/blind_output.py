from trezor.crypto.curve import secp256k1_zkp
from trezor.messages.LiquidBlindedOutput import LiquidBlindedOutput

async def blind_output(ctx, msg, keychain):
    blinding_factor = msg.script_pubkey  # TODO: derive via HMAC with BIP-32 derived private key
    amount = msg.amount
    commitment = secp256k1_zkp.pedersen_commit(amount, blinding_factor)
    return LiquidBlindedOutput(commitment=commitment,
                               nonce=b'NONCE',
                               rangeproof=b'PROOF')
