from trezor.messages.LiquidBlindedOutput import LiquidBlindedOutput


async def blind_output(ctx, msg, keychain):
    return LiquidBlindedOutput(commitment=b'COMMIT',
                               nonce=b'NONCE',
                               rangeproof=b'PROOF')
