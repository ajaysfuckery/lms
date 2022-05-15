import os
import time

# define some stuff
x = True


def banner():

	print("")
	print("███████ ███████ ████████ ██    ██ ██████")
	time.sleep(0.05)
	print("██      ██         ██    ██    ██ ██   ██")
	time.sleep(0.05)
	print("███████ █████      ██    ██    ██ ██████")
	time.sleep(0.05)
	print("     ██ ██         ██    ██    ██ ██")
	time.sleep(0.05)
	print("███████ ███████    ██     ██████  ██")
	time.sleep(0.05)
	print("")

def menu():
	print("========================================================")
	time.sleep(0.05)
	print("1) Install git & wget & curl")
	time.sleep(0.05)
	print("2) Download theming packages")
	time.sleep(0.05)
	print("3) Show installation instructions for packages")
	time.sleep(0.05)
	print("4) Show website for downloading linux .deb files")
	time.sleep(0.05)
	print("5) Show Distributions using .deb for https://pkgs.org")
	time.sleep(0.05)
	print("6) How to download packages from pkgs.org (the fast way)")
	time.sleep(0.05)
	print("7) Show the most used commands in Linux Distros (All)")
	time.sleep(0.05)
	print("8) Show apt commands")
	time.sleep(0.05)
	print("========================================================")
	print("")

def main():
	while x:
		banner()
		menu()

		choice = input("Enter a number: ")

		if choice == "1":
			os.system("clear")
			print("\n\n\n")
			print("Run the following commands as root user (sudo): ")
			print("sudo apt install wget git curl")
			print("\n\n\n")

		elif choice == "2":
			print("\n\n\n")
			print("This script will download the theming packages!")
			os.system("wget -c https://github.com/ajaysfuckery/xdp/blob/main/arcolinux-candy-beauty_22.02-4.deb")
			os.system("wget -c https://github.com/ajaysfuckery/xdp/blob/main/cpunk_1.0-1.deb")
			os.system("wget -c https://github.com/ajaysfuckery/xdp/blob/main/sweet-dark_1.0-1.deb")
			print("\n\n\n")
			print("The packages have been downloaded! Please enter 3 to learn how to install them!!")
			print("\n\n\n")

		elif choice == "3":
			print("\n\n\n")
			print("1) Open a terminal where the files have been downloaded")
			print("2) Type the following commands:")
			print("	- sudo apt-get install ./filename.deb")
			print("\n\n\n")

		elif choice == "4":
			print("\n\n\n")
			print("Website for downloading .deb packages: https://www.pkgs.org")
			print("\n\n\n")

		elif choice == "5":
			print("\n\n\n")
			print("========== Distros using .deb package archive ==========")
			print(" --> Ubuntu")
			print(" --> Debian")
			print(" --> Linux Mint")
			print(" --> All other distros based on Debian and Ubuntu")
			print("\n\n\n")

		elif choice == "6":
			os.system("clear")
			print("\n\n\n")
			print("Visit https://pkgs.org and search for the package you want")
			print("Click on the package you want to download")
			print("Scroll down and look for a .deb link")
			print("Copy the link")
			print("Open the terminal")
			print("Type the following command:")
			print("wget -c <pasted link>")
			print("\n\n\n")
		else:
			print("Please enter a number!!")
main()
