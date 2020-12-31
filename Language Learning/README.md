# Program to count word repetitions from a web text

The program will count the number of times a word appears on several texts from a specific website. 
This is useful for language learners that wants to study the meaning of common words before reading a text in a foreign language. Then when the texts are read, there is a higher possibility that it will be understood without the necessity of searching for the meaning of not known words

### Prerequisites

The program will required the following libraries to be installed:
+ requests 
+ pandas
+ re
+ BeautifulSoup
+ stopwords
+ word_tokenize
+ Counter

### Inputs

Url or list of urls with the text from the website DW

```
url = ["https://www.dw.com/de/12122020-langsam-gesprochene-nachrichten/a-55914683"]
```


Number of words to be shown (20,10,10 by default)

```
print(Counter(no_stops).most_common(20))
print(counts.head(10))
print(counts.tail(10))
```