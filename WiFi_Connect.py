import os

name_main = "Sadly_may_password_ito"

#connect to the main connection
command_connect = "netsh wlan connect ssid=" + name_main + " name=" + name_main

os.system("netsh wlan show profile")
os.system(command_connect)