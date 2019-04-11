# Automatically generated by pb2py
# fmt: off
import protobuf as p


class LiquidBlindedOutput(p.MessageType):
    MESSAGE_WIRE_TYPE = 802

    def __init__(
        self,
        commitment: bytes = None,
        nonce: bytes = None,
        rangeproof: bytes = None,
    ) -> None:
        self.commitment = commitment
        self.nonce = nonce
        self.rangeproof = rangeproof

    @classmethod
    def get_fields(cls):
        return {
            1: ('commitment', p.BytesType, 0),
            2: ('nonce', p.BytesType, 0),
            3: ('rangeproof', p.BytesType, 0),
        }
