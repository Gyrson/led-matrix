# matrix-dashboard
Code and CAD Files for Matrix Dashboard

Installation Guide
Install DietPi from Homepage
Make the installation (As minimal as possible, only activating WLAN and SSH

After installing, you can use 
sudo apt-get update 
sudo apt install build-essential
sudo apt-get install python3-dev python3-pillow -y
sudo apt-get install make
apt-get install dbus

systemctl enable dbus
systemctl start dbus


curl -L https://github.com/hzeller/rpi-rgb-led-matrix/archive/a3eea997a9254b83ab2de97ae80d83588f696387.zip -o rpi-rgb-led-matrix-a3eea997a9254b83ab2de97ae80d83588f696387.zip
unzip -q rpi-rgb-led-matrix-a3eea997a9254b83ab2de97ae80d83588f696387.zip
rm rpi-rgb-led-matrix-a3eea997a9254b83ab2de97ae80d83588f696387.zip
mv rpi-rgb-led-matrix-a3eea997a9254b83ab2de97ae80d83588f696387 rpi-rgb-led-matrix

Edit lib/Makefile (uncomment the Adafruit hat component)
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)

