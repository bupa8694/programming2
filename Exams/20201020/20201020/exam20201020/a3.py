def get_balance(index):
    """This method opens the peeps.json file and
    returns the filed 'balance' of the person of the index given.
    Leave this method as is."""
    import json

    with open('peeps.json') as f:
        data = json.load(f)
        return data[index]['balance'].replace('$', '').replace(',', '')

def get_minmax_balance(indexes):
    """Run the get_balance in parallel for each of the indexes given.
    Then return the minimum and maximum balance of the given results from get_balance.
    Note that the returned field 'balance' has been stripped of the characters '$' and ',' """

    # pass  # Remove the pass statement and enter your code here

    import concurrent.futures as future
    with future.ThreadPoolExecutor() as ex:
        results = ex.map(get_balance, indexes)
    balances = list(results)

    return min(balances), max(balances)

def main():
    print(get_minmax_balance([1,4,2]))


if __name__ == '__main__':
    main()