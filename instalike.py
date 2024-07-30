from flask import Flask, render_template, request
import requests
import random
import string
from getuseragent import UserAgent
import pyfiglet

app = Flask(__name__)

red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'

def generate_username():
    letters = string.ascii_letters
    digits = string.digits
    
    username_letters = ''.join(random.choices(letters, k=10))
    username_digits = ''.join(random.choices(digits, k=5))
    
    return username_letters + username_digits

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        link = request.form['link']
        
        try:
            ua = UserAgent('ios').Random()
        except:
            ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

        User = generate_username()
        
        res = requests.post('https://api.likesjet.com/freeboost/7', json={
            'email': f'hackyourdata{random.randint(100000, 999999)}@gmail.com',
            'link': link,
            'instagram_username': User
        }, headers={
            'accept-language': 'en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'referer': 'https://likesjet.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'origin': 'https://likesjet.com',
            'sec-ch-ua-platform': '"Android"',
            'user-agent': ua,
            'sec-ch-ua-mobile': '?1',
            'content-type': 'application/json',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'content-length': '137',
            'Host': 'api.likesjet.com'
        }).json()

        message = res['message']
        
        return render_template('result2.html', message=message)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
