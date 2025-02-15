import base64 as b

with open("C:/Users/jonat/Downloads/enc_flag", "r") as file:
    cipher = file.readlines()
    cipher = "".join([i.strip() for i in cipher])
    plain = b.b64decode(cipher).decode("utf-8")
    while "picoCTF" not in plain:
        plain = b.b64decode(plain).decode("utf-8")
    print(plain)