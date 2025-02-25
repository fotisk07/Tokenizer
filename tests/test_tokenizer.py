import sys
# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import os

from minitoken import BasicTokenizer


test_strings = [
    "", # empty string
    "?", # single character
    "hello world!!!? (안녕하세요!) lol123 😉", # fun small string
      # FILE: is handled as a special string in unpack()
]

def unpack(text):
    # we do this because `pytest -v .` prints the arguments to console, and we don't
    # want to print the entire contents of the file, it creates a mess. So here we go.
    if text.startswith("FILE:"):
        dirname = os.path.dirname(os.path.abspath(__file__))
        taylorswift_file = os.path.join(dirname, text[5:])
        contents = open(taylorswift_file, "r", encoding="utf-8").read()
        return contents
    else:
        return text
    

#test the basic tokenizer with some strings
@pytest.mark.parametrize("text", test_strings)
def test_basic_tokenizer(text):
    text  = unpack(text)
    tokenizer = BasicTokenizer()
    output = tokenizer.decode(tokenizer.encode(text))

    assert output == text


