import re

def decode_message(s: str, p: str) -> bool:
    pattern = re.sub(r'\?', '.', p)
    pattern = re.sub(r'\*', '.*', pattern)
    pattern = f"^{pattern}$"
    return bool(re.fullmatch(pattern, s))
