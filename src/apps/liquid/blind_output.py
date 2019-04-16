from trezor.crypto.curve import secp256k1_zkp
from trezor.messages.LiquidBlindedOutput import LiquidBlindedOutput

async def blind_output(ctx, msg, keychain):
    blinding_factor = msg.script_pubkey  # TODO: derive via HMAC with BIP-32 derived private key
    value = msg.amount
    commitment = secp256k1_zkp.pedersen_commit(value, blinding_factor)
    nonce = commitment[:32] # TODO: derive via ECDH with BIP-32 derived private key
    message = b"My tears are like the quiet drift / Of petals from some magic rose;"
    extra_commit = b"And all my grief flows from the rift / Of unremembered skies and snows."
    rangeproof = secp256k1_zkp.rangeproof_sign(value, commitment, blinding_factor, nonce, message, extra_commit)
    return LiquidBlindedOutput(commitment=commitment,
                               nonce=nonce,
                               rangeproof=rangeproof)
