def set_default(prototype, attr, default='None'):
    if prototype.get(attr):
        return prototype.get(attr)
    else:
        return default


def load_xml():
    start_path = 'C:\\Games\\Hard Truck CUM'
    END_PATH = '\\data\\gamedata\\gameobjects\\towns.xml'
    with open(start_path + END_PATH, 'r', encoding='windows-1251') as file:
        towns_xml = file.read()
    return towns_xml


def print_town(town):
    print(town.folder_name, end=';')
    print(town.clss, end=';')
    print(town.name, end=';')
    print(town.model_file, end=';')
    print(town.node_scale, end=';')
    print(town.music, end=';')
    print(town.gate_model, end=';')
    print(town.n_coll, end=';')
    print(town.is_inters, end=';')
    print(town.look_radius, end=';')
    print(town.inters_radius, end=';')
    print(town.gun_gener, end=';')
    print(town.desired_guns, end=';')
    print(town.gun_affix_gener, end=';')
    print(town.gun_affix_count, end=';')
    print(town.car_affix_gener, end=';')
    print(town.car_affix_count, end=';')
    print(town.weapon_price_mult, end=';')
    print(town.weapon_price_disp, end=';')
    print(town.vehicles)
    return 'None'
