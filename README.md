# WhoIsHome
By adding a list of device names and associated jingles when that device is detected on the network the audio will play.

## Resources
* [This repo](https://github.com/jxwolstenholme/btsmarthub_devicelist) was used as the base for the app as it could query the router to retrieve a list of connected devices.

* VirtualEnv was used for local dev ([guide](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html))
    * `virtualenv venv` used to create the environment
    * `source venv/bin/activate` to start the env
    * `pip install <package>` can then be used to add packages
    * `deactivate` leaves the env

* Using the commands provided by [this](https://janakiev.com/blog/python-background/) link the script can be run remotely and the connection closed
    * `nohup python3 main.py &` will run the process in the background - **THE `&` is important to run in the background!!**
    * `ps ax | grep main.py` will find the PID for the process
    * `kill <PID>` will kill that process
    