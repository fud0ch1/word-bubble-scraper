## Made for Python 3.7 //
## WordCloud Graph Reference at https://python-graph-gallery.com/260-basic-wordcloud/
## Newspaper3k Article Scraping and Curation Module - https://newspaper.readthedocs.io/en/latest
import newspaper
from newspaper import Article
import tldextract
import logging
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from os import path
from PIL import Image
import matplotlib.pyplot as plt

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

## Assign Variables ##
articleText = ""


ak_mask = np.array(Image.open(path.join(d, "duck.png")))

stopwords = set(STOPWORDS)
stopwords.add("the")
## Create the wordcloud object
wordcloud = WordCloud(background_color = "black", stopwords = stopwords, mask=ak_mask, width = 1200, height = 1200, margin = 0).generate(articleText)
## other choices for WordCloud(background_color = "skyblue", colormap="Blues", max_words = 3, stopwords = ["Python", "Matplotlib"])

## Display the Image
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")  # Axis "on" turns on
plt.margins(x = 0, y = 0)
plt.show()
