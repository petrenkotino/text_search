import pytest
from ..src.search.index import Index, TokenInfo

@pytest.fixture(scope = 'function')
def index():
  return Index()

@pytest.fixture(scope = 'function')
def count_to_ten():
  return 'zero. one, two, three. Four. FIVE. six. seven eight! nine?'

@pytest.fixture(scope = 'function')
def count_to_five_twice():
  return 'zero, ZeRo. one, one. two, two. three, three. four, Four!?'    
