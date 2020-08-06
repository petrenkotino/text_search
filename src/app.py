import sys
import os
import glob
from .search import prompt
from .search.index import Index
from .search.searching import Search

# Certainly there is a better way to perform input validation than this.
def validate_cmd_line_arguments(arguments):
  if len(arguments) < 2:
    raise ValueError('Path to directory with text files must be provided')
  if not os.path.isdir(arguments[1]):
    raise ValueError('Invalid path to directory')

def __buildIndex(txt_doc_paths):
  index = Index()
  for doc_path in txt_doc_paths:
    with open(doc_path) as f:
      doc_content = f.read()
      index.addDoc(doc_path, doc_content)
  
  return index

def run(arguments):
  validate_cmd_line_arguments(arguments)
  txt_doc_paths = glob.glob(arguments[1] + '/*.txt')
  index = __buildIndex(txt_doc_paths)
  searcher = Search(index)
  prompt.SearchPrompt(searcher).cmdloop()
