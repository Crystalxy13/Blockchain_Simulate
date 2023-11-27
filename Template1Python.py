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