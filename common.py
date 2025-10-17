def encrypt(text: str, modulus: int, public_key: int) -> list[int]:
    return [(ord(ch) ** public_key) % modulus for ch in text]


def decrypt(cipher: list[int], modulus: int, private_key: int) -> str:
    return "".join(chr((c**private_key) % modulus) for c in cipher)
