import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

import matplotlib.pyplot as plt

    

df = pd.read_csv("Conhecimentos.csv")
df = df.dropna()
df_w = df[df["Language"] == "English"]
ww = dict(zip(df_w['Palavras'], df_w['Pesos']))
plt.figure(dpi=600)

mask_p = np.array(Image.open("python_logo_2.png"))
#t_mask = np.ndarray((mask.shape[0], mask.shape[1]), np.int32)
img_colors = ImageColorGenerator(mask_p)


wc = WordCloud(
    background_color="white",
    contour_color="gray",
    mode="RGBA",
    mask=mask_p,
    ).generate_from_frequencies(ww)


plt.imshow(wc.recolor(color_func=img_colors), interpolation='bilinear')
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file('wc_python2.png')
