#!/bin/env/python

from base64 import b64encode
from cryptography.fernet import Fernet
from eth_account.messages import encode_defunct
from hashlib import sha256

numAttributes = int(input("SoulBound NFT Generator: \nPlease enter your number of attributes: "))

attributeTypes = []
attr = 1
while attr <= numAttributes:
  attributeTypes.append(input("Enter Attribute %d Type (Int, String): " % attr))
  attr += 1

print(attributeTypes)
