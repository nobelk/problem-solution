import hashlib
import base64


def shorten_url(url: str) -> str:
    enc_bytes = hashlib.sha256(url.encode('utf-8')).digest()
    return base64.b64encode(enc_bytes)
