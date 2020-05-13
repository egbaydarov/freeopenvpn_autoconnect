from download import download_image
from read_captcha import Captcha_detection
import os

download_image()
detected_cap = Captcha_detection("pass.png")
with open("pass.txt", "w") as myfile:
	myfile.write('freeopenvpn\n' + detected_cap)
keypath = ''
with open('config', 'r') as f:
	keypath = f.readline().split()[1]

os.system('cmd /c "openvpn --config ' + keypath + ' --auth-user-pass pass.txt"')
