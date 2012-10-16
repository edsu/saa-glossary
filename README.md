saa-glossary
============

[![Build Status](https://secure.travis-ci.org/edsu/saa-glossary.png)](http://travis-ci.org/edsu/saa-glossary)

This project provides a scraper that crawls the [SAA Glossary of Archival and Records Terminology](http://www.archivists.org/glossary/) and makes the resulting thesaurus data available as JSON and (soon) SKOS RDF.

The resulting JSON is a big dictionary where each glossary term is a key, which
will resemble:

```javascript
{
  "Encoded Archival Description": {
    "narrower": [], 
    "related": [
      {
        "url": "http://www2.archivists.org/glossary/terms/a/archival-description", 
        "pref_label": "archival description"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/d/descriptive-standard", 
        "pref_label": "descriptive standard"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/f/finding-aid", 
        "pref_label": "finding aid"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/m/markup", 
        "pref_label": "markup"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/s/standard-generalized-markup-language", 
        "pref_label": "Standard Generalized Markup Language"
      }
    ], 
    "broader": [], 
    "pref_label": "Encoded Archival Description", 
    "definition": "n. (EAD, abbr.) ~ A standard used to mark up (encode) finding aids that reflects the hierarchical nature of archival collections and that provides a structure for describing the whole of a collection, as well as its components.", 
    "eigenvector_centrality": 9.964256228732647e-05, 
    "alt_label": [
      "EAD"
    ], 
    "url": "http://www2.archivists.org/glossary/terms/e/encoded-archival-description", 
    "notes": [
      "EAD is defined as a document type definition (DTD) that is compatible with both Standard Generalized Markup Language (SGML) and extensible markup language (XML).  See the related standards "
    ], 
    "distinguish_from": [], 
    "citations": [
      {
        "url": "http://www2.archivists.org/glossary/source/feeney-1999", 
        "source": "Feeney, Kathleen, Retrieval of Archival Finding Aids Using World-Wide-Web Search Engines. ", 
        "quotation": "\n  \u2020(Feeney 1999, p. 207\u2013208) [EAD] is intended to provide repositories with a means of establishing an effective, accessible, and stable presence for their holdings information.  EAD accommodates variations in the length and content of finding aids within and among repositories, and preserves in electronic form the complex, hierarchically structured descriptive information found in archival repositories and registers, while also enabling the documents to be navigated and searched in ways that their printed counterparts cannot.  "
      }
    ]
  }, 
  ...
}
```

If you want to update the data you'll need to:

1. sudo apt-get install pip
1. pip install -r requirements.txt
1. ./scrape.py
1. make some tea
1. cat saa-glossary.json
