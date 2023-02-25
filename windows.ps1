Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco install python3 -y

choco install pip -y

python.exe -m pip install --upgrade pip

pip install pytube requests easygui

echo "The required programs and packages are now installed."