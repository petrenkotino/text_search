from cmd import Cmd

class SearchPrompt(Cmd):
  def __init__(self, searcher):
    Cmd.__init__(self)
    self.searcher = searcher

  prompt = 'search> '
  intro = "Welcome! Please enter a word or phrase you'd like me to search for"

  def do_exit(self, inp):
    '''exit the application.'''
    print("Bye")
    return True
    
  def help_exit(self):
    print('exit the application. Shorthand: Ctrl-D.')

  def default(self, inp):
    search_res = self.searcher.search(inp)

    self.printRow('FILENAME', 'SCORE')
    if len(search_res) == 0:
      self.printRow('No files match your search', '')

    for doc_path, score in search_res:
      self.printRow(doc_path, score)

  def printRow(self, doc_path, score):
      print ('{:30}'.format(doc_path) + '{:20}'.format(str(score)))

  do_EOF = do_exit
  help_EOF = help_exit
