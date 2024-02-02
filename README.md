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
Edit lib/Makefile (uncomment the Adafruit hat component)
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)

