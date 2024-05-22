import qrcode
from PIL import Image

# URL = input("QRコードのURL＞")
URL = "https://note.nkmk.me/python-pillow-qrcode/"

qr_image = Image.open('qr_img.jpg')
qr_width, qr_height = qr_image.size
qr_image = qr_image.resize((qr_width, qr_height))

qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr_big.add_data(URL)
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')

desired_size = (3200, 3200)
img_qr_big = img_qr_big.resize(desired_size)

pos = ((img_qr_big.size[0] - qr_image.size[0]) // 2, (img_qr_big.size[1] - qr_image.size[1]) // 2)

img_qr_big.paste(qr_image, pos)
img_qr_big.save('qr.png')

"""
参考
- [Python, Pillow, qrcodeでQRコード画像を生成、保存](https://note.nkmk.me/python-pillow-qrcode/)
"""
