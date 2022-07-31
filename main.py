from utils import adding_item_to_menu, menu_reading


if __name__ == "__main__":
    print('Reading: ')
    print(menu_reading())
    new_item = {"name": "CHURROS DO M5", "price": 5.0}
    print('Writing: ')
    print(adding_item_to_menu(new_item))

