import re
from dataclasses import dataclass
from .pipeline import runPipeline

# @dataclass(eq=True, frozen=True)
# class SearchResult():
#   doc_path: str
#   score: float

class Search():
  def __init__(self, index):
    self.idx_root = index.inverted_index.root
    self.index = index

  # TODO add limit to number of results as an optional param default to 10
  # This works OK for "one word queries" or "free text queries". 
  # If we want to do something like "phrase queries" a few things need to be modified.
  def search(self, query):
    if not query:
      return

    query_terms = runPipeline(query)
    score_per_doc = dict()
    for term in query_terms:
      if self.idx_root.get(term):
        score_per_doc = self.__calculateTFIDF(score_per_doc, term)
    sorted_result = sorted(score_per_doc.items(), key=lambda entry: entry[1], reverse=True)
    return sorted_result

  # Using the simplest possible method for scoring here (Matching score). This should work fairly well for 
  # simpler (shorter queries). For more complex stuff we can look into something like Cosine Similarity
  def __calculateTFIDF(self, tf_idf_score_per_doc, term):
    idf = self.index.getIDF(term)
    for ti in self.idx_root.get(term):
      if tf_idf_score_per_doc.get(ti.doc_path):
        tf_idf_score_per_doc[ti.doc_path] += ti.term_frequency * idf
      else:
        tf_idf_score_per_doc[ti.doc_path] = ti.term_frequency * idf
    return tf_idf_score_per_doc

  def __searchOneTerm(self, term):
    if not term in self.idx_root.keys():
      return []
    return 
