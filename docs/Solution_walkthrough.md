*Disclaimer: As one of the crucial requirement of this task was to code it in Python, and given my lack of knowledge of the language, and it's eco system, I had to spend a good portion of the time allocated for solving the challenge on learning Python. Therefore the code quality, thoroughness of tests, and "production readiness" of the solution had to suffer. I tried to elaborate a bit in code comments about what can be improved, and/or done differently. Do note that writting a lot of comments in code I seldom do in practice - I preffer combination of readable code and tests as code documentation.*

# Getting to a solution

I split this problem into 3 major parts: command line interface, indexing, searching/scoring.

## 0. First learn Python
[Look at this brain dump for my learning process](./Learning_Python.md) (Do note that the text here is not edited almost at all, it is mainly notes I took during the learning process)

## 1. Working on the command line interface
Seems like Python has built in module `Cmd` that can be used for building the prompt interface. As this is a home assingment for a backend role, I'm not going to spend much time investigating options, or making it fancy (a fancy command line interface :P), so going with the first option that seems reasonable.

## 2. Indexing the data
Getting the data structure for the index right is super important, because it will affect the ease and performance of performing the search and scoring later. 
After some thinking and research I decided to use an "inverted index", which basically means a dictionary where each token extracted from the text is used as a key, and as value we store token metadata that is later used for searching. In this case the metadata is fairly simple (as this is a fairly simple and naive solution to this very complex problem).

### 2.1 Improvements in the index

Each document when indexed runs through a "pipeline" where the content is split into tokens (at the moment this is just a simple `.split(' '))` on the whole document), but this pipeline is the place where we can add different language related processing. Some examples in no particular order:
1. Finding typos in text
2. Stemming
3. Removing stop words
4. Handling of multiword tokens/terms (eg. New York)
5. Handling of contractions (eg. don't == do not)

## 3. Searching/Ranking

### 3.1 Searching
Performing the search is fairly simple given the index is structured well. The search is performed by iterating through the query terms (the query text goes through the same pipeline as the document content) and finding the documents in which at least one of the query terms appears. The ranking score is calculated in place. More on ranking later.
This implementation of searching works nothing more than fine for simple use cases, and right now it is limited to single word queries and free text queries, it won't work for phrase queries.

### 3.2 Ranking
This is probably the most challenging part for several reasons. Some of them are:
1. There isn't really a direct technical solution, we need to get creative, and adapt to our use case
2. I have almost zero experience in implementing something like this, and my knowledge on the topic is limited and mainly theoretical

After some thinking and research, I decided to go with what seemed like a simple, reasonably easy to implement approach - [tf-idf (Term Frequency - Inverse Document Frequency)](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

One of the requirements was to return 100% if all words from a query are found in a document. This implementation doesn't really return that. The excuse I have for that is that I considered it fairly trivial to implement, and wanted to focus on implementing the actual ranking algorithm :)

# Assumptions
1. Text files are files that have a `.txt` extension
2. Words are separated with a space ` `. Special chars are removed from start and end of each word.
3. Words are equal only if there is an exact match between indexed term and query term
4. Each document is considered a single blob of text. In a real world scenario we would probably want to split the text in fields or different sections, and weight them differently.

# Testing
Last but definitely not least. I prefer to write tests first, althoug for some reason I opted out of that practice in this case.
I have provided only 2 fairly simple tests (they can probably be called unit tests) for adding documents/indexing and searching.
Ideally there should be at least one acceptance test (for a project of smaller scale such as this one) where there is no or minimum mocking, and tests the "happy case" scenario end-to-end.