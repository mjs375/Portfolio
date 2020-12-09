# RASPBERRY PI 3 - MODEL B

## About Raspberry Pi
- **Model:** Raspberry Pi 3 Model B *(has wireless capabilities).*
  - **OS:** *Raspberry Pi OS, a version of Linux*
    - *Raspberry Pi OS Full comes with all recommended software already loaded, including office applications and games.*
  - **Desktop Applications:** *Programming, Internet, Sound & Video, Graphics, Accessories, Help, Preferences, Run, Shutdown*
- **Installing Software**
  - *On the Desktop, go to ```Preferences```, then ```Recommended Software```. Scroll the software library, install if you want. Additionally, go to ```Preferences``` => ```Add/Remove Software``` to see the entire library of programs & applications.*
- **Update Software**
  - ```Preferences``` => ```Add/Remove Software``` => ```Options``` => ```Refresh Package Lists```. Then, ```Options``` => ```Check for Updates``` => ```Install Updates```.
- **Accessing Your Files**
  - ```Desktop``` => ```Accessories``` => ```File Manager``` (or select the 'stacked folders' icon, the ```File Manager``` itself, directly from the Menu Bar. 
    - ```/home/pi```: *your Home directory to store subfolders & files, e.g. ```Documents```.*
  - *Use USB flash-drives to back-up your files, copy and take them elsewhere, &c.*
- **Terminal**
  - *Accessible in the menu bar by terminal icon. The Terminal allows you to navigate file directories and control the Raspberry Pi using commands.*
    - *Use common terminal commands like ```pwd```, ```ls```, ```cd```, ```exit```. Try using ```pinout``` to see a labelled diagram of your Raspberry Pi.*
- **Configurations**
  - ```Preferences``` => ```Raspberry Pi Configuration```
  - **System:** *set hostname, change password*
  - **Interfaces:** *turn on/off differently linked components (Bluetooth, WiFi, &c.)*
    - ```SSH```: *allow remote access to your Pi via SSH.*
    - ```VNC```: *allow remote access to your Raspberry Pi Desktop from another computer using VNC.*
  - 

- **Custom Aliases:** *you can create an ```alias```, or a custom terminal shortcut command, by running the following in a terminal session: ```$ alias new_name='command to run'.``` To permanently save the alias/shortcut, save that same bit of code in the ```pi``` directory by running ```$ nano /home/pi/.bash_aliases```, then typing and saving your alias.*
  - **```temp```**: *check CPU temperature of the Raspberry Pi (```/opt/vc/bin/vcgencmd measure_temp```)*


## SETUP
- **```$ sudo reboot```**: reboot the Raspberry Pi

### Configuring Raspberry Pi for Wifi Access
- Take out microSD card and load on computer. Access ```/boot``` Volume folder that appears. Create a file called ```wpa_supplicant.conf``` and enter the content below *(allows a computer to pick up the Raspberry Pi via WiFi instead of using an HDMI cable, monitor, keyboard & mouse).*
  - Additionally, create a file called ```ssh``` in ```/boot```. Leave it empty.
```
$ sudo iwlist wlan0 scna |more
  #--See ESSIDs...
$ ifconfig wlan0
  #--Check wlan0 (once Wifi is up, rerunning this line will display IP address, &c.)
$ sudo wpa_passphrase "WIFI_NETWORK_NAME" "password" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
  #--Will print out 'network={...}', with #psk (plaintext password commented out)
$ sudo nano -w /etc/wpa_supplicant/wpa_supplicant.conf 
  #--Open the file and remove the commented-out psk, keeping only the hashed 'psk'
  #--Save & close the file
$ ifconfig wlan0
  #--No IP Address yet...
$ sudo wpa_cli -i wlan0 reconfigure
  #--'OK'
$ reboot
  #--If necessary...

```
```
# # # wpa_supplicant.conf # # #
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=NETDEV

update_config=1

country=US

network={
  ssid="WIFI_NETWORK_NAME"
  psk="930e.............694f49" #--hashed version of Wifi Password
}

```
- *(In a terminal window, run ```arp -a``` to see a list of all devices on the WiFi Network.)*
- Go to ```Localisation``` settings and set WiFi Country.

### Connecting to a Monitor via HDMI
- Connect USB mouse/keyboard to Raspberry Pi unit. Link monitor and Pi with HDMI cable. Plug power cord into Pi unit.

### Connect to Raspberry Pi w/ Computer via VNC
- ```$ sudo apt update```
- ```$ sudo apt install realvnc-vnc-server realvnc-vnc-viewer```
- ```$ free```: *check available memory on microSD/Pi*
- Enable **VNC** in ```Preferences``` => ```R-Pi Configuration```
- ```$ hostname -I```: *get Raspberry Pi's private IP address*

