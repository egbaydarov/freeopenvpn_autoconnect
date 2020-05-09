from download import download_image
from read_captcha import Captcha_detection
import os

download_image()
detected_cap = Captcha_detection("pass.png")
with open("pass.txt", "w") as myfile:
	myfile.write('freeopenvpn\n' + detected_cap)

os.system('cmd /c "openvpn --config 1.key --auth-user-pass pass.txt"')
