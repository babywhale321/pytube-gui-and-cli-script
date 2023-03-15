#tells user of what to expect
echo "This script will install wget, python3, pytube, requests, easygui."

#enter to continue from user
read -r "Press enter to continue script or press ctrl-c to exit"

#installing python3 and wget
sudo apt install python3 wget -y

#using pip to download and install pytube, requests, easygui
pip install pytube requests easygui

#end of script
echo "The required programs and packages are now installed."
