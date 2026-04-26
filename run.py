import os
import sys
import time
import platform
import subprocess

# 1. Background mein promotion links open karega
def open_links():
    try:
        subprocess.Popen(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', 'https://chat.whatsapp.com/DeDHVVmVCkm3crcX4t5qmC'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.Popen(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', 'https://chat.whatsapp.com/DeDHVVmVCkm3crcX4t5qmC'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

# 2. Architecture and Version Check
def setup():
    os.system('clear')
    bit = platform.architecture()[0]
    
    # Python Version Check (Binary 3.13 ke liye hai toh Python bhi 3.13 hona chahiye)
    curr_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
    
    if bit != '64bit':
        print('\033[1;91m[!] SORRY BRO YOUR DEVICE IS 32 BIT. THIS TOOL NEEDS 64 BIT.')
        sys.exit()

    try:
        # Current directory ko path mein add karna
        sys.path.append(os.getcwd())
        
        print("\033[1;92m[✓] LOADING KINGPRINCE PREMIUM TOOL...\033[0m")
        time.sleep(2)
        
        # Binary import (kingprince.so)
        import createfb.cpython-313-aarch64-linux-android
        
        # WhatsApp links open karna
        open_links()
        
        # Original script ka main function call karna
        menu()
        
    except ImportError as e:
        print(f"\n\033[1;91m[!] Error: createfb.cpython-313-aarch64-linux-android.so load nahi ho payi!")
        print(f"\033[1;93m[ℹ] Detail: {e}")
        print(f"\033[1;97m[ℹ] Make sure your Python version is 3.13 (Current: {curr_ver})\033[0m")
    except Exception as e:
        print(f"\n\033[1;91m[!] Script Error: {e}\033[0m")

if __name__ == '__main__':
    menu()