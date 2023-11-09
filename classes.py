from functions import set_default


class Town():
    '''Class of settlements'''
    def __init__(self, folder_name, prototype):
        self.folder_name = folder_name
        self.clss = set_default(prototype, 'Class')
        self.name = set_default(prototype, 'Name')
        self.model_file = set_default(prototype, 'ModelFile')
        self.node_scale = set_default(prototype, 'NodeScale')
        self.music = set_default(prototype, 'MusicName')
        self.gate_model = set_default(prototype, 'GateModelFile')
        self.n_coll = set_default(prototype, 'NumCollisionLayersBelowVehicle')
        self.is_inters = set_default(prototype, 'IsIntersecting')
        self.look_radius = set_default(prototype, 'LookRadius')
        self.inters_radius = set_default(prototype, 'IntersectionRadius')
        self.gun_gener = set_default(prototype, 'GunGenerator')
        self.desired_guns = set_default(prototype, 'DesiredGunsInWorkshop')
        self.gun_affix_gener = set_default(prototype, 'GunAffixGenerator')
        self.gun_affix_count = set_default(prototype, 'GunAffixesCount')
        self.car_affix_gener = set_default(prototype, 'CabinsAndBasketsAffixGenerator')
        self.car_affix_count = set_default(prototype, 'CabinsAndBasketsAffixesCount')
        self.weapon_price_mult = set_default(prototype, 'WeaponPriceMultiplier')
        self.weapon_price_disp = set_default(prototype, 'WeaponPriceDispersion')
        self.vehicles = set_default(prototype, 'Vehicles')
        # self.articles = {}


# class Article():
#     def __init__(self):
#         self.parent = ''
#         self.prototype = ''
#         self.amount = ''
#         self.ext_price = ''
#         self.imprt = ''
#         self.exprt = ''
#         self.price_dyn = ''
#         self.min_count = ''
#         self.max_count = ''
#         self.regen_period = ''
