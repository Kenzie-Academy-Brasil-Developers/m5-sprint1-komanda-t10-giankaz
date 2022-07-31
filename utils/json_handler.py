import ujson as json

def menu_reading ():
        try:
            with open('menu.json', 'r') as menu:
              data = json.load(menu)
            if (len(data) == 0):
                    return []    
            return data
        except:
            return []


def adding_item_to_menu (item):
        menu = menu_reading()
        last_item_id = menu[-1]['id']
        new_item = {'id': last_item_id + 1}
        
        for key, value in item.items():
            new_item.update({key:value})

        menu.append(new_item)

        with open('menu.json', 'w') as menu_file:
            json.dump(menu, menu_file, indent=1)

        return new_item
    
