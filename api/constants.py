from types import SimpleNamespace

MAX_NUM_TO_INT = 10**21
ERROR_RESPONSE = SimpleNamespace(
    INVALID_INPUT="Please enter a valid whole number. Example: '123'",
    NUM_OUT_OF_RANGE="Input out of range. Please use whole numbers between -10^21 to 10^21"
)
STATUS_RESPONSE = SimpleNamespace(
    OK="ok",
    ERROR="error"
)
