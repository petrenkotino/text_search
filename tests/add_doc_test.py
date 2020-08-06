import pytest
from ..src.search.index import Index, TokenInfo

@pytest.fixture(scope = 'function')
def index():
  return Index()

@pytest.mark.parametrize('doc_path, doc_content', [(None, None), ('some', None), (None, 'some'), ('some', '')])
def test_empty_doc_path_or_content_should_result_with_zero_elements(index, doc_path, doc_content):
  index.addDoc(doc_path, doc_content)
  assert len(index.inverted_index.root) == 0

def test_index_contains_expected_number_of_tokens_multiple_files(index, count_to_five_twice, count_to_ten):
  index.addDoc('/path/to/five', count_to_five_twice)
  index.addDoc('/path/to/ten', count_to_ten)
  assert len(index.inverted_index.root) == 10

def test_it_calculates_tf_as_expected(index, count_to_five_twice):
  index.addDoc('path/to/five', count_to_five_twice)
  index.addDoc('path/to/five_twice', count_to_five_twice + ' ' + count_to_five_twice)
  assert index.inverted_index.root.get('one') == [
    TokenInfo('path/to/five', 0.2),
    TokenInfo('path/to/five_twice', 0.2)
  ]

# This can probably be made a bit better
def test_index_contains_lowered_trimmed_stripped_tokens_with_expected_token_info(index, count_to_five_twice, count_to_ten):
  path_to_five = '/path/to/five'
  path_to_ten = '/path/to/ten'
  index.addDoc(path_to_five, count_to_five_twice)
  index.addDoc(path_to_ten, count_to_ten)
  
  zero_to_four = ['zero', 'one', 'two', 'three', 'four']
  five_to_ten = ['five', 'six', 'seven', 'eight', 'nine']

  for first, second in zip(zero_to_four, five_to_ten):
    value_first = index.inverted_index.root.get(first)
    value_second = index.inverted_index.root.get(second)
    assert value_first == [TokenInfo(path_to_five, 0.2), TokenInfo(path_to_ten, 0.1)]
    assert value_second == [TokenInfo(path_to_ten, 0.1)]