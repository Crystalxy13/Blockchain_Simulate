"""
Python Programming (ACFI827)
Assignment 1: Simulate Access to Sensitive Account Data in Blockchain
Created on 2023/11/25


Use this template for submit assignment as a single Python file.    
"""


import json as _json
import hashlib as _hashlib
import datetime
import random
import time

# ==============================================================================
# Task A: Total Number of Accounts and Compare Dictionary Keys
# ==============================================================================

"""
This section loads loan account data from a JSON file and compares the keys in the dictionary 
of each account to check if they are identical across all accounts.
"""

jsonFilePath = r'loan_account_statement.json'    #This is path of file in your computer were you have saved your file

with open(jsonFilePath) as json_file:
    json_data = _json.load(json_file)



# Find the number of accounts in the dataset
num_accounts = len(json_data)

# Compare the keys in the dictionary of each account
# Initialize a variable to hold the keys of the first account for comparison
first_account_keys = set(json_data[0].keys())

# Variable to track if all dictionaries have identical keys
identical_keys = True

# Loop through each account and compare keys
for account in json_data:
    if set(account.keys()) != first_account_keys:
        identical_keys = False
        break

print(num_accounts, identical_keys)

"""
# Paste output here
6745 True
"""

# ==============================================================================
# Task B: Hash Creation and Comparison
# ==============================================================================
"""
This section creates hash values for selected loan account data and compares these hash values.
"""
    
# Function to create hash of a given account data
def create_hash(account_data):
    """
    Creates a hash of the given account data.
    :param account_data: The account data to be hashed.
    :return: The hash value of the account data.
    """
    encoded_block = str(account_data).encode()
    return _hashlib.sha256(encoded_block).hexdigest()

# Create hash values for the 9th and 11th accounts
hashvalue1 = create_hash(json_data[8])  # 9th account (index 8)
hashvalue2 = create_hash(json_data[8])  # 9th account (index 8) again for comparison
hashvalue3 = create_hash(json_data[10])  # 11th account (index 10)

# Function to compare hash values
def compare_hashes(hash1, hash2):
    """
    Compares two hash values and determines if they are identical or not.
    :param hash1: The first hash value.
    :param hash2: The second hash value.
    :return: A string stating whether the hash values are identical or not.
    """
    if hash1 == hash2:
        return "identical"
    else:
        return "not identical"

# Compare hashvalue1 and hashvalue2, and hashvalue1 and hashvalue3
comparison1 = compare_hashes(hashvalue1, hashvalue2)
comparison2 = compare_hashes(hashvalue1, hashvalue3)

print(f"Hash value of the 1st account (hashvalue1): {hashvalue1}")
print(f"Hash value of the 1st account again (hashvalue2): {hashvalue2}")
print(f"Hash value of the 2nd account (hashvalue3): {hashvalue3}")
print(f"Comparison of hashvalue1 and hashvalue2 (Are they identical?): {comparison1}")
print(f"Comparison of hashvalue1 and hashvalue3 (Are they identical?): {comparison2}")

"""
# Paste output here
Hash value of the 1st account (hashvalue1): 0e40f0189fb34d58741ff6135db1e4cc97f46077e1f01c21d95b336334b43926
Hash value of the 1st account again (hashvalue2): 0e40f0189fb34d58741ff6135db1e4cc97f46077e1f01c21d95b336334b43926
Hash value of the 2nd account (hashvalue3): b311789a666d0e33bbd5704c84ace08cfd32cd611cbdfcfeb52cf9a6a62e9e85
Comparison of hashvalue1 and hashvalue2 (Are they identical?): identical
Comparison of hashvalue1 and hashvalue3 (Are they identical?): not identical
"""