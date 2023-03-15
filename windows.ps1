#tells the user of what happens before running script
echo "This script will install chocolatey, python3, pip, pytube, requests, easygui."
Read-Host -Prompt "Press enter to continue script or press ctrl-c to exit"

#download and install chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

#install python3 with chocolatey
choco install python3 -y

#install pip with chocolatey
choco install pip -y

#upgrade pip if not most recent packages
python.exe -m pip install --upgrade pip

#using pip to download and install pytube, requests and then easygui
pip install pytube requests easygui

#end of script
echo "The required programs and packages are now installed."
