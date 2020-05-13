import requests

def download_image():
	url1 ="https://www.freeopenvpn.org/logpass/russia.php"


	with open('config', 'r') as f:
	         url1 = f.readline().split()[0]
	

	payload = {}
	headers = {
	  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
	}

	response = requests.request("GET", url1, headers=headers, data = payload)

	page_string = str(response.text.encode('utf8'))
	index = page_string.find('password.php?')

	kuka = 'par=' + page_string[index + 13:index + 13 + 18] + ';'

	url = 'https://www.freeopenvpn.org/logpass/password.php?' + page_string[index + 13:index + 13 + 18]

	payload = {}
	headers = {
	  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
	  'Referer': url1,
	  'Cookie': kuka
	}

	response = requests.request("GET", url, headers=headers, data = payload)

	with open('pass.png', 'wb') as f:
	        for chunk in response.iter_content(1024):
	            f.write(chunk)