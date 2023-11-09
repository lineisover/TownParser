from functions import load_xml
from functions import print_town
from classes import Town
from lxml import etree


def main():
    file = load_xml()
    towns = dict()
    root = etree.fromstring(bytes(file, encoding='windows-1251'))
    for folder in root.getchildren():
        folder_name = folder.get('Name')
        for prototype in folder.getchildren():
            if prototype.get('Class') == 'Town':
                town = Town(folder_name, prototype)
                towns.setdefault(prototype.get('Name'), town)
    for town in towns.values():
        print_town(town)


main()
