import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# List of URLs where the text will be scraped from
url = ["https://www.dw.com/de/12122020-langsam-gesprochene-nachrichten/a-55914683",
       "https://www.dw.com/de/14112020-langsam-gesprochene-nachrichten/a-55599290",
       "https://www.dw.com/de/11122020-langsam-gesprochene-nachrichten/a-55902294",
       "https://www.dw.com/de/10122020-langsam-gesprochene-nachrichten/a-55891493",
       "https://www.dw.com/de/28112020-langsam-gesprochene-nachrichten/a-55757361",
       "https://www.dw.com/de/30112020-langsam-gesprochene-nachrichten/a-55768646"]

# Variables to save the date and text
date_str_f = []
texto_pro_f = []


for url in url:
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    # Retrieve the date of the news
    date = re.match("(\d\d).(\d\d).(\d+)", soup.title.text).group()
    date_str = re.sub("\n", " ", str(date))
    date_str_f.append(date_str)

    # Copy only the text of the news
    texto = []
    for div in soup.find_all('div', class_='longText'):
        for p in div.find_all('p'):
            texto.append(p.text)

    # Leave only text and delete the rest of characters
    texto_pro = re.sub("[^a-zA-Z0-9äöüÄÖÜß\s]+", " ", str(texto))
    texto_pro = re.sub("(xa0)", " ", str(texto_pro))
    texto_pro_f.append(texto_pro)


print('The number of scraped dates is: ', len(date_str_f))
print('The number of scraped texts is: ', len(texto_pro_f))


# Create a DataFrame
data={'Date': date_str_f,
      'Texto': texto_pro_f}
df_text = pd.DataFrame(data)

# Convert the dates and sort the DataFrame by date
df_text['Date'] = pd.to_datetime(df_text['Date'], format='%d.%m.%Y')
df_text = df_text.sort_values(by='Date')
print(df_text.head(6))

# Put all the text together from column 'Texto' to be analyzed
complete_text=df_text.Texto.sum()
print(complete_text)

# Text Processing: 1. Normalization, 2. Tokenization, 3. Drop Stopwords
tokens = [w for w in word_tokenize(complete_text.lower()) if w.isalpha()]
no_stops = [t for t in tokens if t not in stopwords.words('german')]


# Most repeated words using Counter function
print('+++++++++++++++++++++++++++++++++++++')
print(Counter(no_stops).most_common(20))
print('+++++++++++++++++++++++++++++++++++++')


# Create a data frame with the Text already processed
df = pd.DataFrame(no_stops)
df.columns = ['Text']

# Most repeated words using a custom-made function
counts = df.Text.value_counts().to_frame().rename(columns={'Text':'Repetitions'})
print(counts.head(10))
print(counts.tail(10))


# Other functions not used
# print the title --> print(soup.title.text)