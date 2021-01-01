import base64
import random
import string
from string import printable

if __name__ == "__main__":
    btc_addresses = [
        "1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i",
        "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",
        "BC1QW508D6QEJXTDG4Y5R3ZARVARY0C5XW7KV8F3T4",
        "bc1q5s8fz9p8x0a59774jlr9cmuwf6kjdv3j5tqvxm",
        "3Fxq8ctmbr5CQEdoow189rAi64LePvxgfb",
    ]
    ips = [
        "1762:0:0:0:0:B03:1:AF18",
        "1762:0:0:0:0:B03:127.32.67.1",
        "1762::B03:1:AF18",
        "762::B03:127.32.67.15",
        "2001:0000:1234:0000:0000:C1C0:ABCD:0876",
        "fe80:0:0:0:204:61ff:fe9d:f156",
        "fe80::204:61ff:fe9d:f156",
        "fe80:0000:0000:0000:0204:61ff:254.157.241.86",
        "fe80:0:0:0:0204:61ff:254.157.241.86",
        "fe80::204:61ff:254.157.241.86",
        "::1",
        "fe80::",
        "2001::",
        "0.0.0.0",
        "255.255.255.255",
        "172.16.0.0",
    ]
    emails = ["test@example.com", "other.test@example.com"]
    md5s = [
        "d41d8cd98f00b204e9800998ecf8427e",
        "0cc175b9c0f1b6a831c399e269772661",
        "098f6bcd4621d373cade4e832627b4f6",
    ]
    urls = [
        "https://google.com",
        "http://seznam.cz",
        "https://devdocs.io/python~3.5/library/stdtypes#str.translate",
    ]

    result = [
        "".join(random.choice(printable) for _ in range(random.randint(0, 10000)))
        + random.choice(string.whitespace)
        + item
        + random.choice(string.whitespace)
        + "".join(random.choice(printable) for _ in range(random.randint(0, 30000)))
        for item in btc_addresses + ips + emails + md5s + urls
    ]

    with open("examples/gen/ex_input.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(result))

    with open("examples/gen/ex_base64", "wb") as g:
        g.write(base64.b64encode("\n".join(result).encode("utf-8")))

    with open("examples/gen/ex_base32", "wb") as g:
        g.write(base64.b32encode("\n".join(result).encode("utf-8")))

    with open("examples/gen/ex_base85", "wb") as g:
        g.write(base64.b85encode("\n".join(result).encode("utf-8")))

    with open("examples/gen/ex_ascii85", "wb") as g:
        g.write(base64.a85encode("\n".join(result).encode("utf-8")))