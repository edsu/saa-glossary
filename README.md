saa-glossary
============

This project provides a scraper that crawls the [SAA Glossary of Archival and Records Terminology](http://www.archivists.org/glossary/) and makes the resulting thesaurus data available as JSON and (soon) SKOS RDF.

If you want to update the data you'll need to:

1. sudo apt-get install pip
1. pip install -r requirements.txt
1. ./scrape.py
1. make some tea
1. cat saa-glossary.json
