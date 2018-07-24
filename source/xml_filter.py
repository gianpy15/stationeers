import xml.etree.ElementTree as ET


world = '../resources/Stationeers/world.xml'
world_new = '../resources/Stationeers/world_new.xml'
item_to_remove = 'ItemIronOre'

if __name__ == '__main__':
    tree = ET.parse(world)
    root = tree.getroot()
    things = root.find('./Things')
    items = 0
    to_remove = 0

    for thingSaveData in things.findall('.//ThingSaveData'):
        item = thingSaveData.find('.//PrefabName').text
        items += 1
        if item == item_to_remove:
            things.remove(thingSaveData)
            to_remove += 1

    tree.write(world_new)
    print("found {} ThingSaveData, removed {} {}".format(items, to_remove, item_to_remove))
