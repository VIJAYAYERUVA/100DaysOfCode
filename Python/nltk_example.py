# https://stackoverflow.com/questions/31836058/nltk-named-entity-recognition-to-a-python-list
# https://stackoverflow.com/questions/24398536/named-entity-recognition-with-regular-expression-nltk

import nltk

nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree


def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue
    if current_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)
            current_chunk = []
    return continuous_chunk


txt = "Barack Obama is a great person and so is Michelle Obama."
print(get_continuous_chunks(txt))
