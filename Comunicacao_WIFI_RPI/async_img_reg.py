import requests
from PIL import Image
from io import BytesIO

resp_img = requests.get('http://192.168.1.202/picture')

img = Image.open(BytesIO(resp_img.content))
img.save("recv.jpg")