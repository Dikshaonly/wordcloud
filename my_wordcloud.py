#Importing Libraries
import os,sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
#Importing Dataset
text=open('Restaurant_Reviews.tsv',mode='r',encoding='utf-8').read()
stopwords=STOPWORDS
#generating word cloud
word_cloud = WordCloud(
    width=3000,
    height=2000,
    random_state=1,
    background_color="salmon",
    colormap="BuPu",
    collocations=False,
    stopwords=stopwords    
)
word_cloud.generate(text)
word_cloud.to_file('wordcloud_output.png')
#Display the generated Word Cloud
plt.imshow(word_cloud)
plt.axis("off")
plt.show()