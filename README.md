# CP423 Assignment #1

This assignment for text retrieval required a lot of concepts we learned in class around normalization and how to retrieve words when web crawling with filtering and looking out for stopwords and creating an inverted index for easy search. With this information, we can perform SQL queries with AND, OR, and NOT which is incredibly helpful when we have a large corpus we are dealing with and retrieves documents that meet a certain condition. We are going to examine this article from wikipedia called “Canadian Provinces Historical Population” and extract articles from each subsequent page we visit with a depth level of 3 and the first 5 valid articles which should amount to about 31 articles visited in total that we keep track of.

### **Part One: Web Scraping, Link Exploration, and Data Processing**

So for part one, we lay the foundation by taking a look at our web page and seeing what is needed and what needs to be excluded. We can use the requests library to retrieve the raw html with this getSoupFromLink function and just by examining the page and the parts that don’t seem necessary, we can remove the header, footer, navigation, bibliography, references and notes. This leaves us with the body text and tables for every province/territory. We also remove the respective sections that seem to repeat themselves across all articles and are not needed for our purposes such as "See also", "References", "Bibliography", "Further reading." 


After that is done, we can create a function to extract the links from a page up to a limit of 5 which is when we break and escape the loop setup set up to iterate through all tags that have a value of ‘a’ that provides the link. Once that is complete, we can build our top level function that uses all the established functions thus far to create a folder called scraped info which lets us download and write onto files with the filtering and limiting placed and works like a depth first search where we explore all the links for individual nodes in each depth up to 5 before moving on as is evident in our folder. 


The naming convention set up provides us the depth, id and article name and if we run this file, the new folder creates 31 files of all the explored pages and their text data retrieved which has us complete the first part of the project.


### **Part Two: Text Preprocessing and Inverted Index Implementation**

Moving onto part two, with this found text from each article visited, we can preprocess this information using NLTK or natural language toolkit and clean up and remove all stopwords, singly occurring letters, non alphanumeric characters and tokenize the text for use within an inverted index data structure, a concept we learned in class which is a word oriented mechanism to index vast text documentations to make searching easy.

From my code, you can see the preprocess function makes the text lower case, only accepts alphanumeric and space characters. Then we tokenize using word_tokenize from NLTK and with our downloaded stopwords, we can iterate through our word tokens and remove all stop words in a filter variable and finally remove single length tokens. 

Next we create a data structure to represent the inverted index so we initialise it with a dictionary and make a creation method that essentially iterates through our scrappedInfo folder and for each file we preprocess it and add the word into our index by name and document frequency which is why we take the id from the file name itself. We then sort this in this final loop since an inverted index has to be in ascending order. 

We can test by running this python file where we initiate an inverted index and provide it the scrapped info directory. This will give us all the words used across each document and their respective documents they appeared in. We can verify this with the VS Code search

### **Part Three: Query Support and System Evaluation** NOT SOLVED

Lastly, we need to develop generalized code to handle queries with multiple terms. Unfortunately I wasn't able to solve this but I believe we could convert the query string given to a postfix expression, something we learned in Database 1 and 2 and we can evaluate it using this function I have set up here which depending on the operation, we can perform AND, OR, and NOT to the different articles to get the documents that fulfill the condition. I set up x as Ontario and y as Quebec for the query strings so with that given approach, we could see the intersection of values between the articles in the list. I was not able to solve this but I believe that would be the approach. 