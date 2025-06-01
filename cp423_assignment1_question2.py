# Question 2: Text Preprocessing and Inverted Index Implementation [40 points]
# Perform the following preprocessing steps on all collected textual content from Question 1:
# 1. Convert text to lowercase.
# 2. Tokenize text using NLTK.
# 3. Remove stop words using NLTK.
# 4. Exclude non-alphanumeric special characters.
# 5. Eliminate singly occurring characters.
# 6. Implement an inverted index data structure using this preprocessed content.

from collections import defaultdict
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

def preprocess(text):
    text = text.lower()
    text = ''.join(t for t in text if t.isalnum() or t.isspace())
    wordTokens = word_tokenize(text)
    stopWords = set(stopwords.words('english'))
    filtered = [w for w in wordTokens if w not in stopWords]
    filtered = [w for w in filtered if len(w) > 1]

    return filtered

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def createInvertedIndex(self, folder):        
        for filename in os.listdir(folder):
            filePath = os.path.join(folder, filename)
            with open(filePath, 'r', encoding='utf-8') as f:
                text = f.read()

            parts = filename.split('_')
            fileId = 0

            for i in range(len(parts)):
                if parts[i] == "id":
                    fileId = int(parts[i + 1].split('.')[0])
                    break

            words = preprocess(text)
            for word in words:
                self.index[word].add(fileId)

        for word in self.index:
            self.index[word] = sorted(list(self.index[word]))
    
invertedIndex = InvertedIndex()
invertedIndex.createInvertedIndex("scrappedInfo")

for word, fileId in invertedIndex.index.items():
    print(f"{word}: {fileId}")
