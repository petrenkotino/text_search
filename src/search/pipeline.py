import re

# TODO: implement a way of customizing the steps for the pipeline 
# (eg. stop words filter, stemming, or user defined functions)

def runPipeline(txt):
  ''' 1. Trimms out non alpha numeric characters from text
      2. Splits text into tokens
      3. Calculates token count
      
      input('word1! word1, woRd2\n word3 word4 Word3 word3')
      output
      output ({word1: 2, word2: 1, word3: 3, word4: 1}, total_number_of_tokens_in_doc
  '''
  tokens = tokenize(txt)
  trimmed_tokens = trimNonWordCharacters(tokens)
  # This is the place where other language "operations" (like stemming, removing stop words, 
  # dealing with plurals etc.) would happen
  return trimmed_tokens

# This is a candidate to be moved into it's own module and offer some extension/modification options (eg. change separator etc)
def tokenize(txt):
  if not txt:
    return []
  if not isinstance(txt, str):
    raise ValueError('txt must be a string')
  
  separator = ' '
  tokens = txt.strip().lower().split(separator)
  return tokens

def trimNonWordCharacters(tokens):
  if not tokens:
    return ''
  # ^ asserts position at start of str; \W matches non-word chars; + one or more times
  # \W matches non-word chars; + one or more times; $ asserts position at end of str
  clean_tokens = [re.sub(r'\W+$', '', re.sub(r'^\W+', '', token)) for token in tokens]
  # Alternative that removes all non alpha-num chars (downside is that it will split contractions like I'm or don't into "I" "m" and "don" "t" ) 
  # clean_tokens = re.sub(r'[\W_]+', ' ', txt)
  return clean_tokens