# ♟️ p4wnsolo-qr
🟢 QR Code display for P4wnP1 w/OLED (SSH, VNC, any text / URL)

<img src="p4wnsolo-qr-code-ssh-display.jpg">

## Requirements:
🔵 Raspberry Pi Zero W / Zero 2 (tested Dec 12, 2021 on RPi 0 W running P4wnP1 ALOA)&nbsp;
🔵 1.3" OLED Hat (SH1106)&nbsp;
##### 🔵 <a href="https://osintool.com/sh1106-oled-screen/">Luma.oled drivers installed</a>
<a href="https://github.com/pimoroni/sh1106-python"><code>sudo pip3 install luma luma.oled</code></a>

## 🔨 Usage:
<code>python3 p4wnsolo-qr.py -i spi --display sh1106</code>

### 📷 Screenshots / images:
See the images in this Repo (<code>p4wnsolo-qr-code-XYZ.jpg</code>) for example display screens.

#### 🕷Extra:
The default operating mode is "ssh", which generates a QR Code to connect to Raspberry Pi via SSH.
There's also a "spiderfoot" option, which generates a QR Code to connect to Spiderfoot server running on Raspberry Pi.
The Spiderfoot feature has not yet been implemented (doesn't check to see if Spiderfoot is running).
But if you want to see the "demo" of Spiderfoot QR Code mode, here's how:
1.  Open <code>p4wnsolo-qr.py</code> in text editor
2.  Near Line #25, you'll see something like this:  "##### Set mode here"
3.  Comment out the line that says <code>themode = 'ssh'</code>
4.  Uncomment the line that says <code>themode = 'spiderfoot'</code>
