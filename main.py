from btsmarthub_devicelist import BTSmartHub
import os, sys, time

class Person(object):
    def __init__(self, name=None, hostname=None, home=False, sound=None, played=False):
        self.name = name
        self.hostname = hostname
        self.home = home
        self.sound = sound
        self.played = played

housemates = {
    "Adam" : Person("Adam", "Adams-iPhone", False, "Adam.mp3", False),
    "Ali" : Person("Ali", "Alis-S8", False, "Ali.mp3", False),
    "Alice" : Person("Alice", "Alices-iphone", False, "Alice.mp3", False),
    "Cox" : Person("Cox", "", False, "Cox.mp3", False),
    "Richard" : Person("Richard", "", False, "Richard.mp3", False),
}

smarthub = BTSmartHub(router_ip='192.168.1.254')

while True:
    device_list = smarthub.get_devicelist(only_active_devices=True)

    # Determine present devices
    for name in housemates:
        atHome = False
        for entry in device_list:
            if housemates[name].hostname == entry ['UserHostName']:
                atHome = True
                break
        housemates[name].home = atHome

    # Alert regarding presence
    for name in housemates:
        if housemates[name].home:
            if not housemates[name].played:
                os.system('omxplayer '+housemates[name].sound)
                housemates[name].played = True
        else:
            housemates[name].played = False
    time.sleep(1)