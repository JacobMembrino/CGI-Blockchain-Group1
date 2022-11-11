from brownie import SimpleStorage, accounts


def main():
    account = accounts.load('deployment_account')
    SimpleStorage.deploy({'from': account})
