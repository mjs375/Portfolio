# RASPBERRY PI 3 - MODEL B
- Raspberry Pi password: M*!?


## SETUP

### Configuring Raspberry Pi for Wifi Access
- Take out microSD card and load on computer. Access ```/boot``` Volume folder that appears. Create a file called ```wpa_supplicant.conf``` and enter the content below *(allows a computer to pick up the Raspberry Pi via WiFi instead of using an HDMI cable, monitor, keyboard & mouse).*
  - Additionally, create a file called ```ssh``` in ```/boot```. Leave it empty.
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=NETDEV

update_config=1

country=US

network={

  ssid="WIFI_NAME"

  psk="WIFI_PASSWORD"

  scan_ssid=1

}
```
- In a terminal window, run ```arp -a``` to see a list of all devices on the WiFi Network.
- Run ```ssh pi@[IP NUMBER]```.
https://spin.atomicobject.com/2019/06/09/raspberry-pi-laptop-display/

### Connecting to a Monitor via HDMI
- Connect USB mouse/keyboard to Raspberry Pi unit. Link monitor and Pi with HDMI cable. Plug power cord into Pi unit.
