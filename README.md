Project playing around with NLP inspired by a
[medium article](https://medium.com/@ageitgey/natural-language-processing-is-fun-9a0bff37854e)

Further reading:
- [spacy](https://spacy.io/api/doc)
- [textacy](http://textacy.readthedocs.io/en/latest/)

### Build
`docker build -t spacy .`

### Play
`docker run -it --rm -v $(pwd):/usr/src/app spacy bash`

### Run
`docker run -it --rm -v $DATA:/tmp spacy`
