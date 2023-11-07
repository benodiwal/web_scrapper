from tabulate import tabulate

def make_table(prices, sources):
    data = [
        [1, sources[0], prices[0]],
        [2, sources[1], prices[1]],
        ]
    table = tabulate(data, headers=["Sr. no.", "Source" ,"Price"], tablefmt="fancy_grid")
    print(table)
    print("\n")

