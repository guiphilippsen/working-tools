import subprocess

inter = input("Enter the interface: ")
mac = input("Enter the MAC Addr: ")

subprocess.call("ifconfig " + inter + " down", shell=True)
subprocess.call("ifconfig " + inter + " hw ether" + mac, shell=True)
subprocess.call("ifconfig " + inter + " up", shell=True)