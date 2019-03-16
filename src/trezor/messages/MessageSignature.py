# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .BenchmarkResult import BenchmarkResult


class MessageSignature(p.MessageType):
    MESSAGE_WIRE_TYPE = 40

    def __init__(
        self,
        address: str = None,
        signature: bytes = None,
        benchmark: BenchmarkResult = None,
    ) -> None:
        self.address = address
        self.signature = signature
        self.benchmark = benchmark

    @classmethod
    def get_fields(cls):
        return {
            1: ('address', p.UnicodeType, 0),
            2: ('signature', p.BytesType, 0),
            3: ('benchmark', BenchmarkResult, 0),
        }
