import pytest
from ..src.search.searching import Search

def test_that_it_returns_empty_result_when_index_has_no_match_for_query(index, count_to_five_twice):
  searcher = Search(index)
  index.addDoc('/path/to/five', count_to_five_twice)
  search_result = searcher.search(' no such words in index')
  assert len(search_result) == 0

def test_that_it_returns_empty_result_when_index_is_empty(index, count_to_five_twice):
  searcher = Search(index)
  search_result = searcher.search('no documents have been indexed')
  assert len(search_result) == 0

def test_that_it_ranks_docs_equally_when_appropriate(index, count_to_ten):
  searcher = Search(index)
  index.addDoc('/path/to/ten', count_to_ten)
  index.addDoc('/path/to/ten_twice', count_to_ten + ' ' + count_to_ten)
  search_result = searcher.search(' one two three')
  assert search_result[0][1] == search_result[1][1]
  
def test_that_it_ranks_documents_as_expected(index, count_to_ten):
  searcher = Search(index)
  index.addDoc('/path/to/doc1', 'hello world something else')
  index.addDoc('/path/to/doc2', 'hello something else')
  index.addDoc('/path/to/doc3', 'hello world')
  search_result = searcher.search('hello world')
  doc_path_result = [res[0] for res in search_result]
  assert doc_path_result == list(['/path/to/doc3', '/path/to/doc1', '/path/to/doc2'])