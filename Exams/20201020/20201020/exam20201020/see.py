def get_age(index):
    """This method opens the peeps.json file and
    returns the age of the person of the index given.
    Leave this method as is."""
    import json

    with open('peeps.json') as f:
        data = json.load(f)
        return data[index]['age']


def get_average_age(indexes):
    """Run the get_age in parallel (concurrently) for each of the indexes given.
    Then return the average age of the given results from get_age."""
    import concurrent.futures as future
     # Remove the pass statement and enter your code here
    with future.ThreadPoolExecutor() as ex:
        results = ex.map(get_age, indexes)
    ages = list(results)
    return sum(ages)/len(ages)


def get_balance(index):
    """This method opens the peeps.json file and
    returns the age of the person of the index given.
    Leave this method as is."""
    import json

    with open('peeps.json') as f:
        data = json.load(f)
        return data[index]['balance'].replace('$', '').replace(',', '')

def get_max_balance(indexes):
    """Run the get_age in parallel (concurrently) for each of the indexes given.
    Then return the average age of the given results from get_age."""
    import concurrent.futures as future
     # Remove the pass statement and enter your code here
    with future.ThreadPoolExecutor() as ex:
        results = ex.map(get_balance, indexes)
    balances = list(results)
    print(balances)
    return max(balances)
def main():
    print(get_max_balance([1,4,2]))
    # print(float(get_balance(0).strip('$').replace(',', '')))


if __name__ == '__main__':
    main()