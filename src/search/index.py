import math
from dataclasses import dataclass
from .pipeline import runPipeline

# Data classes seem to get rid of some boilerplate.
@dataclass(eq=True, frozen=True)
class TokenInfo():
  '''
    doc_path: absolute path to the document.
    term_frequency: Normalized: tf(t, d) = count of terms in doc / number of words in doc 
  '''
  doc_path: str
  term_frequency: int
  # position: list # This can be used for more advanced search queries and ranking
  
@dataclass
class InvertedIndex():
  number_of_docs: int
  root: dict

class Index():
  def __init__(self):
    self.fields = []
    self.inverted_index = InvertedIndex(0, dict())

  def addDoc(self, doc_path, doc_content):
    if not doc_path or not doc_content:
      return
    all_tokens = runPipeline(doc_content)
    num_tokens_in_doc = len(all_tokens)
    token_count = self.__getTokenCount(all_tokens)

    for token in token_count.keys():
      if token in self.inverted_index.root:
        token_infos = self.inverted_index.root.get(token)
        token_infos.append(TokenInfo(doc_path, token_count[token]/num_tokens_in_doc))
        self.inverted_index.root.update({token: token_infos})
      else:
        self.inverted_index.root[token] = [TokenInfo(doc_path, token_count[token] / num_tokens_in_doc)]
      self.inverted_index.number_of_docs += 1
    return

  # You can calculate idf by dividing the total number of documents you have in your corpus by the 
  # number of documents containing the term (df) and then take the logarithm of that quotient.
  # Another approach might be to keep this in memory istead of calculatig it every time
  def getIDF(self, token):
    df = self.__getDocumentFrequency(token)
    if not df == 0:
      return math.log(self.inverted_index.number_of_docs / df)
    return 0

  # I run into 2 definitions for DF, the first and more common one being the one I opted for --> How many documents contain the term
  # The other one was how many times a term occurs in the search space
  # Another approach might be to keep this in memory istead of calculatig it every time
  def __getDocumentFrequency(self, token):
    token_infos = self.inverted_index.root[token]
    if not token_infos:
      return 0
    return len(token_infos)

  def __getTokenCount(self, all_tokens_in_doc):
    token_count = dict()
    for token in all_tokens_in_doc:
      token_count[token] = all_tokens_in_doc.count(token)
    return token_count

  # The following functions (removeDoc, updateDoc) would be great to have in a real world scenario
  def removeDoc(self):
    raise NotImplementedError('Not yet implemented')

  def updateDoc(self):
    raise NotImplementedError('Not yet implemented')
  