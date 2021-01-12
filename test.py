from PIL import Image
import requests
from io import BytesIO

url = "https://secure.img1-fg.wfcdn.com/im/02238154/compr-r85/8470/84707680/pokemon-pikachu-wall-decal.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()