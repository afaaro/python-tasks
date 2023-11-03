
from collections import defaultdict

products = {
    'milk': 1.55,
    'egg': 2.80,
    'water': 1.10,
    'chocolate': 1.25
}


def get_orders():
    collection = []

    while True:
        user_input = input("Enter product name? ")

        if isinstance(user_input, str):
            user_input = str(user_input)

            if user_input in products.keys():
                key = user_input
                val = products[user_input]

                # add every product to the memory
                collection.append({key: val})

        if user_input == 'x':
            break
    return collection


def get_product_values():
    collections = defaultdict(list)
    for collection in get_orders():
        for key, value in collection.items():
            # Merge duplicate key and add value to the same key
            collections[key].append(value)

    rows = []
    # Get all values from the shopping data
    for product in collections.values():
        for key in product:
            # Merge all values of different key
            rows.append(key)

    return sum(rows)


def main():
    total_bought_items = get_product_values()
    print(f"your total shop is £{total_bought_items}")

    while True:
        user_cash = float(input("How much are you paying? £"))
        if user_cash >= total_bought_items:
            total_remaining = float(user_cash - total_bought_items)
            print("You have paid £{} and this is your channge £{} ".format(user_cash, total_remaining))

            break
        elif user_cash < total_bought_items:
            total_payback = total_bought_items - user_cash
            print(f"You need to pay extra {total_payback}")
        else:
            print(f"Please make a payment of {total_bought_items}")


main()
