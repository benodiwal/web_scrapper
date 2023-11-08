from tabulate import tabulate

def make_table(prices, sources):
    data = [
        [1, sources[0], prices[0].replace("", "")],
        [2, sources[1], prices[1].replace("", "")],
        ]
    table = tabulate(data, headers=["Sr. no.", "Source" ,"Price (Rs.)"], tablefmt="fancy_grid")
    print(table)
    print("\n")