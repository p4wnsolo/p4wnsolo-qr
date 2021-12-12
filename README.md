# ♟️ p4wnsolo-qr
🟢 QR Code display for P4wnP1 w/OLED (SSH, VNC, any text / URL)

<img src="p4wnsolo-qr-code-ssh-display.jpg">

## Requirements:
##### 🔵 Raspberry Pi Zero W / Zero 2 (tested Dec 12, 2021 on RPi 0 W running P4wnP1 ALOA)
##### 🔵 1.3" OLED Hat (SH1106)
##### 🔵 <a href="https://osintool.com/sh1106-oled-screen/">Luma.oled drivers installed</a>
##### Install Luma & Luma OLED:
##### <a href="https://github.com/pimoroni/sh1106-python"><code>sudo pip3 install luma luma.oled</code></a>

## 🔨 Usage:
##### Clone the repo
<code>git clone https://github.com/p4wnsolo/p4wnsolo-qr.git</code>
##### Change directories
<code>cd p4wnsolo-qr</code>
##### Launch the script
<code>python3 p4wnsolo-qr.py -i spi --display sh1106</code>

### 📷 Sample QR Code:
<img src="qr.png">
See the images in this Repo (<code>p4wnsolo-qr-code-XYZ.jpg</code>) or scroll down for example display screens.

#### 🕷Extra:
The default operating mode is <code>ssh</code>, which generates a QR Code to connect to Raspberry Pi via SSH.
There's also a <code>spiderfoot</code> option, which generates a QR Code to connect to Spiderfoot server running on Raspberry Pi.
The Spiderfoot feature has not yet been implemented (doesn't check to see if Spiderfoot is running).
But if you want to see the "demo" of Spiderfoot QR Code mode, here's how:
1.  Open <code>p4wnsolo-qr.py</code> in text editor
2.  Near Line 25, you'll see something like this:  <code>##### Set mode here</code>
3.  Comment out the line that says <code>themode = 'ssh'</code>
4.  Uncomment the line that says <code>themode = 'spiderfoot'</code>
In the works:
- Add <code>themode<code> code entries for P4wnP1 WebGUI URL
  
## 📷 Screenshots
  
####Generating QR Code for SSH
<img src="p4wnsolo-qr-code-ssh-generating.jpg">
  
####Displaying QR Code for SSH
<img src="p4wnsolo-qr-code-ssh-display.jpg">
  
####Generating QR Code for Spiderfoot
<img src="p4wnsolo-qr-code-spiderfoot-generating.jpg">
     
####Displaying QR Code for Spiderfoot
<img src="p4wnsolo-qr-code-spiderfoot-display-notime.jpg">
  
####After Pressing + Button for More Time
<img src="p4wnsolo-qr-code-spiderfoot-display.jpg">  
