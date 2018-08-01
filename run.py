#!/usr/bin/env python3

import spacy
import textacy.extract

# The text we want to examine
text = \
    """
    London is the capital and most populous city of England and
    the United Kingdom.  Standing on the River Thames in the south east
    of the island of Great Britain, London has been a major settlement
    for two millennia. It was founded by the Romans, who named it Londinium.
    """

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# Parse the text with spaCy. This runs the entire pipeline.
doc = nlp(text)

# Extract semi-structured statements
statements = textacy.extract.semistructured_statements(doc, "London")

# Extract noun chunks that appear
noun_chunks = textacy.extract.noun_chunks(doc)

# Convert noun chunks to lowercase strings
noun_chunks = map(str, noun_chunks)
noun_chunks = map(str.lower, noun_chunks)

# Replace a token with "REDACTED" if it is a name
def replace_name_with_placeholder(token):
    if token.ent_iob != 0 and token.ent_type_ == "PERSON":
        return "[REDACTED] "
    else:
        return token.string

# Loop through all the entities in a document and check if they are names
def scrub(text):
    doc = nlp(text)
    for ent in doc.ents:
        ent.merge()
    tokens = map(replace_name_with_placeholder, doc)
    return "".join(tokens)

if __name__ == '__main__':
    print("Here are the named entities that were detected (and their labels):")
    for entity in doc.ents:
        print(f"{entity.text} ({entity.label_})")

    print("Here are the names reducted/scrubbed:")
    print(scrub(text))

    print("Here are the subjects, verbs and facts:")
    for statement in statements:
        subject, verb, fact = statement
        print(f" -S {subject}")
        print(f" -V {verb}")
        print(f" -F {fact}")

    # Print out any nouns that are at least 2 words long
    print("Here are the noun chunks:")
    for noun_chunk in set(noun_chunks):
        print(f" - {noun_chunk.strip()}")
