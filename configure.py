import platform
import urllib.request
from zipfile import ZipFile
import os
import json

# System types
# 1 = Windows
# 2 = Linux
# 3 = anything else

xmrig_urls = "https://github.com/Franektoube/Fminer/raw/refs/heads/main/xmrig_urls.json"

def download(system_number):
    print("")
    
    fetched = urllib.request.urlopen(xmrig_urls)
    data = json.loads(fetched.read())
    
    if system_number == 1:
        xmrig_download_url = data['windows']['url']
    elif system_number == 2:
        xmrig_download_url = data['linux']['url']
    else:
        print("Invalid System install linux bro.")
        return
    
    file_name = xmrig_download_url.split('/')[-1]
    urllib.request.urlretrieve(xmrig_download_url, file_name)
    
    with ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(os.getcwd())

def config():
    wallet_address = input("Enter Wallet Adress ( Check 2 times ): ").strip
    temp = input("Use processor? If not click enter: ")
    if temp:
        use_cpu = True
    else:
        use_cpu = False
    
    temp = input("Use graphics card? ( Only Nvidia and Windows) If not click enter: ")
    if temp:
        use_gpu = True
        fetched = urllib.request.urlopen(xmrig_urls)
        data = json.loads(fetched.read())
        url = data["windows"]["cuda_url"]
        file_name = url.split('/')[-1]
        urllib.request.urlretrieve(url, file_name)
        with ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())


    else:
        use_gpu = False
    
    config = {
    "autosave": True,
    "donate-level": 0,
    "cpu": use_cpu,
    "opencl": False,
    "cuda": use_gpu,
    "pools": [
        {
            "url": "Your POOL adress extample: monero.pool:PORT",
            "user": "anything you want",
            "keepalive": True,
            "tls": True
        }
    ]
}
    
    config_file = "config.json"

    with open(config_file, 'w') as f:

        json.dump(config, f)

    

def main():
    download(1 if platform.system() == "Windows" else 2 if platform.system() == "Linux" else "MacOS Bruh")
    config()

if __name__ == "__main__":
    main()