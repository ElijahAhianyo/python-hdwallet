#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.symbols import BTC

import json

# Bitcoin hdwallet xprivate key
XPRIVATE_KEY = "xprvA3KRgVDh45mbQT1VmWPx73YeAWM4629Q2D9pMuqjFMnjTqDGhKiww6H" \
               "532rgYRNj37fngd4Mvp7GfUD8rKeQzUZjCWeisT92tX8FfjWx3BL"

# Initialize Bitcoin hdwallet
hdwallet = HDWallet(symbol=BTC)
# Get Bitcoin hdwallet from xprivate key
hdwallet.from_xprivate_key(xprivate_key=XPRIVATE_KEY)

# Print all hdwallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("XPrivate Key:", hdwallet.xprivate_key())
print("XPublic Key:", hdwallet.xpublic_key())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Chain Code:", hdwallet.chain_code())
print("Private Key:", hdwallet.private_key())
print("Public Key:", hdwallet.public_key())
print("Wallet Important Format:", hdwallet.wif())
print("Finger Print:", hdwallet.finger_print())
print("Address:", hdwallet.address())
