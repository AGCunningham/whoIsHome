from btsmarthub_devicelist import BTSmartHub
import os, sys

housemates = ['Adams-iPhone', 'Alis-S8', 'Alices-iphone']

home = {
    "Adams-iPhone" : False,
    "Alis-S8" : False,
    "Alices-iphone" : False,
}

sounds = {
    "Adams-iPhone" : "Adam.mp3",
    "Alis-S8" : "Ali.mp3",
    "Alices-iphone" : "Ali.mp3",
}

smarthub = BTSmartHub(router_ip='192.168.1.254')

while True:
    device_list = smarthub.get_devicelist(only_active_devices=True)

    for name in housemates:
        test = False
        for entry in device_list:
            if name == entry ['UserHostName']:
                test = True
                # Not 100% sure whether this will work, should check
                break
        home[name] = test

    # Check if we were previously in the house

    for name in home:
        os.system('omxplayer '+sounds[name])
    time.sleep(1)