saa-glossary
============

[![Build Status](https://secure.travis-ci.org/edsu/saa-glossary.png)](http://travis-ci.org/edsu/saa-glossary)

This project provides a scraper that crawls the [SAA Glossary of Archival and
Records Terminology](http://www2.archivists.org/glossary) and makes the
resulting thesaurus data available as SKOS JSON-LD.

    pip install -r requirements.txt
    python scrape.py
    cat saa-glossary.json
