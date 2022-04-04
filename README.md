# Text normalization for TTS for Icelandic

__This repository was forked from Reykjavik University, [LVL]: https://github.com/cadia-lvl/regina_normalizer__

__regina_normalizer__ is a normalization system based on regular expressions. Its core functionality is to expand digits, symbols and abbreviations contained in an input text so that it can be converted to phoneme representation and then read by a speech synthesizer.

# Setup
* Clone the repository
* Install requirements (preferably in a virtual environment)
* Run `pip install -e .` from the root directory

To try the normalization out from the command line:

`python3 regina_normalizer/main.py {sentence-to-be-normalized}`

for example

`python3 regina_normalizer/main.py "10.010.000 kr aukalega"`

output:

`[['tíu milljónir og tíu þúsund krónur aukalega']]` 

Two additional arguments can be given to the command line interface: `-d` for __domain__ and `-f` for __format__.
The normalizer has a special processing for domain "sport", but the default domain is "other", i.e. no special treatment for the input. The default format argument is "plain", returning a list of normalized sentences from the input (see example above). Using `-f "tokens"` returns a list of tuples, where one can see how each token was normalized:

`python3 regina_normalizer/main.py "Það eru 54 km eftir. Kostar þetta 1263 kr?" -f "tokens"` 

output: 

`[[('Það', 'Það'), ('eru', 'eru'), ('54', ' fimmtíu og fjórir'), ('km', 'kílómetrar'), ('eftir', 'eftir'), ('.', '.')], [('Kostar', 'Kostar'), ('þetta', 'þetta'), ('1263', ' tólf hundruð sextíu og þrjár'), ('kr', 'krónur'), ('?', '?')]]`

# License
[MIT](LICENSE)

# Authors
- Anna Björk Nikulásdóttir [email](anna@grammatek.com) (this fork)
- Helga Svala Sigurðardóttir, Reykjavík University (original regina_normalizer)

# Acknowledgements
This project, both the original regina_normalizer and this derivative, is funded by the Language Technology Programme for Icelandic 2019-2023. The programme, which is managed and coordinated by [Almannarómur](https://almannaromur.is/), is funded by the Icelandic Ministry of Education, Science and Culture.
