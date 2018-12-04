from trezor.messages.TestOnlyResponse import TestOnlyResponse


def do_something(arg):
    return b'[' + arg + b']'


async def test_only(ctx, msg):
    arg1 = msg.arg1
    arg1 = do_something(arg1)
    return TestOnlyResponse(arg1=arg1)
