import tkinter as tk
import tkinter.filedialog
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from sklearn.cluster import KMeans

def selectFile():
    root = tk.Tk()
    root.withdraw()
    types = [ ("画像ファイル", "*.jpg; *.png")]
    target_img = tkinter.filedialog.askopenfilename( filetypes = types, title = "select the image" )
    return target_img

# 画像の選択
original_img = cv2.imread( selectFile() )
original_img =  cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
img = original_img
img = img.reshape( (img.shape[0] * img.shape[1], 3) )

# k-meansを使って、メインカラーの抽出
num = 4
cluster = KMeans(n_clusters=num, n_init=10)
cluster.fit(X=img)
cluster_centers_arr = cluster.cluster_centers_.astype(int, copy=False)

# メインカラー画像の用意
IMG_SIZE = 64
MARGIN = 15
width = IMG_SIZE * num + MARGIN * 2
height = IMG_SIZE + MARGIN * 2
tiled_color_img = Image.new(mode='RGB', size=(width, height), color='#FFF')
maincolor = []
for i, rgb_arr in enumerate(cluster_centers_arr):
    color_hex_str = "#%02x%02x%02x" % tuple(rgb_arr)
    maincolor.append(color_hex_str)
    color_img = Image.new(mode='RGB', size=(IMG_SIZE, IMG_SIZE), color=color_hex_str)
    tiled_color_img.paste(im=color_img, box=(MARGIN + IMG_SIZE * i, MARGIN))

# メインカラーの出力
for i, item in enumerate(maincolor):
    print(f"{i+1}位：{item}")

# 画像出力
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(original_img)
axs[0].set_title("Original Image")
axs[0].axis("off")

axs[1].imshow(tiled_color_img)
axs[1].set_title(f"Clustered Image (K={num})")
axs[1].axis("off")
plt.show()


"""
# Reference
- [Pythonで画像からメインカラーを抽出する](https://qiita.com/simonritchie/items/396112fb8a10702a3644)
"""

