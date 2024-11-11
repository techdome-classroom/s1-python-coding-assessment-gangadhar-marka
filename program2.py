import re

def decode_message(s: str, p: str) -> bool:
    pattern = p.replace('?', '.').replace('*', '.*')
    pattern = f"^{pattern}$"
    return bool(re.match(pattern, s))
