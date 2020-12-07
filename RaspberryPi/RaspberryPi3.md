# RASPBERRY PI 3 - MODEL B


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
