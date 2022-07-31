from utils import adding_item_to_menu, menu_reading
from management import total_calculator


if __name__ == "__main__":
    print('Reading: ')
    print(menu_reading())
    new_item = {"name": "CHURROS DO M5", "price": 5.0}
    print('Writing: ')
    print(adding_item_to_menu(new_item))

    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]

    table_2 = [
        {"id": 10, "amount": 3},
        {"id": 20, "amount": 2},
        {"id": 21, "amount": 5},
        ]
    print('Total Bill 1:')
    print(total_calculator(table_1))
    print('Total Bill 2:')
    print(total_calculator(table_2))