saa-glossary
============

[![Build Status](https://secure.travis-ci.org/edsu/saa-glossary.png)](http://travis-ci.org/edsu/saa-glossary)

This project provides a scraper that crawls the [SAA Glossary of Archival and Records Terminology](http://www.archivists.org/glossary/) and makes the resulting thesaurus data available as JSON and (soon) SKOS RDF.

The resulting JSON is a big dictionary where the glossary term is the key, which
will resemble:

```javascript
{
  "accession": {
    "url": "http://www.archivists.org/glossary/term_details.asp?DefinitionKey=115", 
    "pref_label": "accession"
    "alt_label": [], 
    "definition": "n. ~ 1. Materials physically and legally transferred to a repository as a unit at a single time; an acquisition.\r\n\r\n", 
    "related": [
      {
        "url": "http://www.archivists.org/glossary/term_details.asp?DefinitionKey=275", 
        "pref_label": "accretion"
      }, 
      {
        "url": "http://www.archivists.org/glossary/term_details.asp?DefinitionKey=492", 
        "pref_label": "accrual"
      }, 
      {
        "url": "http://www.archivists.org/glossary/term_details.asp?DefinitionKey=655", 
        "pref_label": "deaccessioning"
      }, 
      {
        "url": "http://www.archivists.org/glossary/term_details.asp?DefinitionKey=1606", 
        "pref_label": "registration"
      }
    ], 
    "narrower": [],
    "broader": [], 
    "distinguish_from": [
      {
        "url": "http://www.archivists.org/glossary/term_details.asp?DefinitionKey=114", 
        "pref_label": "acquisition"
      }
    ], 
    "citations": [
      {
        "url": "http://www.archivists.org/glossary/source_cite.asp?SortOrder=220", 
        "source": "Keeping Archives. Australian Society of Archivists, 1987.", 
        "quotation": "Having made sure that new material has been legally transferred to your archives, the next, and vitally important, step is to gain control over it. This initial process is called accessioning."
      }
    ], 
    "notes": [
      "The materials may be acquired by gift, bequest, purchase, transfer, retention schedule, or statute. An accession may be part of a larger, existing collection.  An accession added to existing collections is sometimes called an accretion or an accrual.\r\n\r\n", 
      "'Accession' should be distinguished from 'acquisition'. As nouns, they are synonymous.  However, the verb 'accession' goes far beyond the sense of 'acquire', connoting the initial steps of processing by establishing rudimentary physical and intellectual control over the materials by entering brief information about those materials in a register, database, or other log of the repository's holdings."
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
