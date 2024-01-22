import itertools as it 
import random 
import spacy

import pytest 



@pytest.mark.parametrize("a,b,c,d,e", it.product("abcdef", "123456", "XYZ", "!@#", "[]"))
def test_wait(a,b,c,d,e):
    total = sum([random.random() for i in range(1_000_000)])
    assert total > 1


def test_downloaded_model():
    # A bunch of sentences
    sentences = ['This framework generates embeddings for each input sentence',
                 'Sentences are passed as a list of string.',
                 'The quick brown fox jumps over the lazy dog.'] * 100

    nlp = spacy.load("en_core_web_md")
    for doc in nlp.pipe(sentences):
        assert doc.text
