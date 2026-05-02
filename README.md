# ⚠️ This repository has moved

**This project has been superseded by [open-astro/aw-flashtool](https://github.com/open-astro/aw-flashtool).**

Please head over to the new repository for the latest code, releases, and issue tracking:

### 👉 https://github.com/open-astro/aw-flashtool

This repository is kept online in archived, read-only form for historical reference only. **No further updates, fixes, or support will be provided here.**

---

## ASIAIR Jailbreak (archived)

Original tool for gaining root SSH access to Seestar S50 / ASIAIR devices. All code was originally written by joshumax and stored here under public domain (CC0-1.0). Source material from the [Cloudy Nights thread](https://www.cloudynights.com/topic/900861-seestar-s50asiair-jailbreak-ssh/).

### FIRST OF ALL, THIS IS ALL ESSENTIALLY ONE GIANT HACK. IT HAS WORKED FOR ME BUT IT COULD BRICK YOUR DEVICE, OR WORSE. THIS IS FOR DEVELOPERS ONLY. IF YOU AREN'T FAMILIAR WITH SSH OR LINUX, DON'T USE THIS!

Hi everyone,

With the release of ZWO's new Seestar S50, I'm finally releasing a tool I've been using internally to gain root SSH access to both my Seestar and ASIAIR devices. I was originally hoping that ZWO would reduce their rampant open source software license violations and vendor lock-in, but it's only gotten worse. This has made me decide to create a completely FOSS integrated astrophotography solution that will totally replace their software while still leveraging the ASI hardware. I intend to release this project free of charge to the astronomical community shortly.

In the meantime, I am providing this jailbreak so that others can explore their ASIAIR device without the need of physically opening it and soldering on UART headers. To run it, all you need is a machine running a reasonably new Python 3 as well as the archive attached to this post.

Current jailbreak release
https://mega.nz/file/1cRQjbCL#zs6TYY8k8ycevjFhr9xV7GDWmo70hMvRt3E0ym0GGXY

### Requirements

- Python 3 (most Linux distributions ship with it)

To check if Python 3 is installed:
```
python3 --version
```

If not installed:
- **Debian/Ubuntu:** `sudo apt install python3`
- **Fedora:** `sudo dnf install python3`
- **Arch:** `sudo pacman -S python`

### Usage

**Note:** On Linux, use `python3` instead of `python`.

#### Auto-scan (recommended)
Run with no arguments to automatically scan your local network for ASIAIR devices:
```
python3 run_jailbreak.py
```
The script will:
1. Detect your local subnet
2. Scan all hosts for ASIAIR-specific ports (4350, 4030, 4400, etc.)
3. Identify each discovered device using reverse DNS, SSH banner, OTA service response, and port fingerprinting
4. Confirm whether the device is an ASIAIR (with a confidence level)
5. Estimate the firmware version based on open ports
6. If one device is found, use it automatically. If multiple are found, prompt you to choose

You can also run with `--scan` explicitly:
```
python3 run_jailbreak.py --scan
```

#### Manual IP
If you already know the IP address of your device:
```
python3 run_jailbreak.py [IP_ADDRESS_OF_DEVICE]
```
The script will still probe the device's ports, identify it as an ASIAIR, and estimate the firmware version before proceeding.

### Device Identification

The script identifies ASIAIR devices using three methods:

- **Hostname lookup** - Resolves the IP via reverse DNS and checks for "ASIAIR" or "ZWO" in the hostname
- **Service banners** - Reads the SSH banner (port 22) and OTA service response (port 4350)
- **Port fingerprinting** - Checks for ASIAIR-specific ports (4030, 4040, 4350, 4360, 4400, 4500, 4700, 4800) and reports a confidence level based on how many are open

If the device cannot be confirmed as an ASIAIR, the script will warn you and ask before proceeding.

### Firmware Detection

The script detects the approximate firmware version based on open ports:

| Firmware | Ports |
|----------|-------|
| 4.35 | 22, 139, 445, 4030, 4040, 4350, 4360, 4400, 4500, 4700, 4800, 8888 |
| 10.74+ | All of the above + **4801** |

Port 4801 is the distinguishing port added in firmware 10.74.

### Connect to Seestar/ASIAIR:
```
ssh pi@[IP_ADDRESS_OF_DEVICE]
```
The password for SSH will be `raspberry` if the jailbreak ran successfully. You can access the root account via `sudo`.
