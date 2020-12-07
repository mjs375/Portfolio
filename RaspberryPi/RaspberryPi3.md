# RASPBERRY PI 3 - MODEL B


### wpa_supplicant.conf
- File written in Raspberry Pi's microSD ```/boot``` that allows a computer to pick up the Raspberry Pi via WiFi instead of using an HDMI cable, monitor, keyboard & mouse.
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
