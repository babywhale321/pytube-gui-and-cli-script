import os

try:
    
    #copy script to users home dir
    os.system("cp gui-experimental.py ~/gui-experimental.py")
    
except:
    
    print("Failed to copy main file to home dir")

#if the os is linux
if os.name == "posix":
  
    os.system("gnome-terminal -e 'bash -c \"python3 gui-experimental.py; exec bash\"'")

#if the os is  windows
elif os.name == "nt":
  
    os.system("start /wait cmd /k python3 gui-experimental.py")
    
#if not windows or linux    
else:
  
    print("Sorry this OS is not supported")
