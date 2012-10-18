saa-glossary
============

[![Build Status](https://secure.travis-ci.org/edsu/saa-glossary.png)](http://travis-ci.org/edsu/saa-glossary)

This project provides a scraper that crawls the [SAA Glossary of Archival and Records Terminology](http://www.archivists.org/glossary/) and makes the resulting thesaurus data available as JSON and SKOS RDF.

Here's what the SKOS looks like for the concept appraisal:

```
<http://www2.archivists.org/glossary/terms/a/appraisal> a skos:Concept;
    skos:definition "n. ~ 1. The process of identifying materials offered to an archives that have sufficient value to be accessioned. - 2.  The process of determining the length of time records should be retained, based on legal requirements and on their current and potential usefulness. - 3. The process of determining the market value of an item; monetary appraisal.";
    skos:narrower <http://www2.archivists.org/glossary/terms/c/content-analysis>,
        <http://www2.archivists.org/glossary/terms/c/context-analysis>,
        <http://www2.archivists.org/glossary/terms/d/documentation-strategy>,
        <http://www2.archivists.org/glossary/terms/f/functional-analysis>,
        <http://www2.archivists.org/glossary/terms/m/macro-appraisal>,
        <http://www2.archivists.org/glossary/terms/u/use-analysis>;
    skos:prefLabel "appraisal";
    skos:related <http://www2.archivists.org/glossary/terms/c/collection-development>,
        <http://www2.archivists.org/glossary/terms/f/fat-file-method>,
        <http://www2.archivists.org/glossary/terms/r/reappraisal>,
        <http://www2.archivists.org/glossary/terms/s/selection>,
        <http://www2.archivists.org/glossary/terms/v/valuation>,
        <http://www2.archivists.org/glossary/terms/v/value>;
    skos:scopeNote "Appraisal is distinguished from monetary appraisal, which estimates fair market value.  Appraisal is distinguished from evaluation, which is typically used by records managers to indicate a preliminary assessment of value based on existing retention schedules.",
        """In an archival context, appraisal is the process of determining whether records and other materials have permanent (archival) value.  Appraisal may be done at the collection, creator, series, file, or item level.  Appraisal can take place prior to donation and prior to physical transfer, at or after accessioning.  The basis of appraisal decisions may include a number of factors, including the records' provenance and content, their authenticity and reliability, their order and completeness, their condition and costs to preserve them, and their intrinsic value.  Appraisal often takes place within a larger institutional collecting policy and mission statement.  """ .
```

And the resulting JSON is a big dictionary where each glossary term is a key, 
which will resemble:

```javascript
{
  "appraisal": {
    "narrower": [
      {
        "url": "http://www2.archivists.org/glossary/terms/c/content-analysis", 
        "pref_label": "content analysis"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/c/context-analysis", 
        "pref_label": "context analysis"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/d/documentation-strategy", 
        "pref_label": "documentation strategy"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/f/functional-analysis", 
        "pref_label": "functional analysis"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/m/macro-appraisal", 
        "pref_label": "macro appraisal"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/u/use-analysis", 
        "pref_label": "use analysis"
      }
    ], 
    "related": [
      {
        "url": "http://www2.archivists.org/glossary/terms/c/collection-development", 
        "pref_label": "collection development"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/f/fat-file-method", 
        "pref_label": "fat file method"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/r/reappraisal", 
        "pref_label": "reappraisal"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/s/selection", 
        "pref_label": "selection"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/v/valuation", 
        "pref_label": "valuation"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/v/value", 
        "pref_label": "value"
      }
    ], 
    "broader": [], 
    "pref_label": "appraisal", 
    "definition": "n. ~ 1. The process of identifying materials offered to an archives that have sufficient value to be accessioned. - 2.  The process of determining the length of time records should be retained, based on legal requirements and on their current and potential usefulness. - 3. The process of determining the market value of an item; monetary appraisal.", 
    "eigenvector_centrality": 0.0009875135754408087, 
    "alt_label": [], 
    "url": "http://www2.archivists.org/glossary/terms/a/appraisal", 
    "notes": [
      "In an archival context, appraisal is the process of determining whether records and other materials have permanent (archival) value.  Appraisal may be done at the collection, creator, series, file, or item level.  Appraisal can take place prior to donation and prior to physical transfer, at or after accessioning.\nThe basis of appraisal decisions may include a number of factors, including the records' provenance and content, their authenticity and reliability, their order and completeness, their condition and costs to preserve them, and their intrinsic value.  Appraisal often takes place within a larger institutional collecting policy and mission statement.  ", 
      "Appraisal is distinguished from monetary appraisal, which estimates fair market value.  Appraisal is distinguished from evaluation, which is typically used by records managers to indicate a preliminary assessment of value based on existing retention schedules."
    ], 
    "distinguish_from": [
      {
        "url": "http://www2.archivists.org/glossary/terms/e/evaluation", 
        "pref_label": "evaluation"
      }, 
      {
        "url": "http://www2.archivists.org/glossary/terms/m/monetary-appraisal", 
        "pref_label": "monetary appraisal"
      }
    ], 
    "citations": [
      {
        "url": "http://www2.archivists.org/glossary/source/brichford-1977", 
        "source": "Brichford, Maynard J., ", 
        "quotation": "\n  \u2020(Brichford 1977, p. 2) The archivists considering the records to be appraised will study their age, volume, and form, and will analyze their functional, evidential, and informational characteristics.  "
      }, 
      {
        "url": "http://www2.archivists.org/glossary/source/duranti-1998", 
        "source": "Duranti, Luciana, ", 
        "quotation": "\n  \u2020(Duranti 1998, p. 177) The principle of provenance, as applied to appraisal, leads us to evaluate records on the basis of the importance of the creator's mandate and functions, and fosters the use of a hierarchical method, a 'top-down' approach, which has proved to be unsatisfactory because it excludes the 'powerless transactions,' which might throw light on the broader social context, from the permanent record of society.  "
      }, 
      {
        "url": "http://www2.archivists.org/glossary/source/eastwood-2004", 
        "source": "Eastwood, Terry, Jenkinson's Writings on Some Enduring Archival Themes. ", 
        "quotation": "\n  \u2020(Eastwood 2004, p. 40) This idea of Jenkinson's [that archivists ought not to be in the business of destroying records] has, as might be expected, almost universal condemnation by archivists who routinely conduct appraisal, often nowadays mandated in legislation where public records are concerned. It may seem that events have passed Jenkinson by, but, in fact, as several archivists inspired by postmodernist thinking have argued, when archivists decide what to save and what to destroy, they begin to be a factor in the determination of what archives are.  "
      }, 
      {
        "url": "http://www2.archivists.org/glossary/source/ham-1993", 
        "source": "Ham, F. Gerald, ", 
        "quotation": "\n  \u2020(Ham 1993, p. 51) There are five analyses that make up the basic tools archivists need in their appraisal kits to identify and select records of enduring value. These are an analysis: of a record's functional characteristics \u2013 who made the record and for what purpose; of the information in the record to determine its significance and quality; of the record in the context of parallel or related documentary sources; of the potential uses that are likely to be made of the record and the physical, legal, and intellectual limitations on access; of the cost of preserving the record weighed against the benefit of retaining the information.  "
      }, 
      {
        "url": "http://www2.archivists.org/glossary/source/personal-communication", 
        "source": null, 
        "quotation": "\n  \u2020(Personal communication, Mark Greene, 28 May 2004) The basis on which appraisal decisions should be made has been the subject of intense professional debate.  Some archival theorists, notably Jenkinson, argue that such decisions should not be made by archivists at all, but only by records creators.  In the United States, Schellenberg believed that appraisal was not only an appropriate archival function but an absolutely necessary one, in the face of increasing masses of documentation in the 20th century.  U.S. archival theory and practice has been rooted in Schellenberg's philosophy and teaching.  "
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

And if you want to re-generate the SKOS RDF:

1. ./skos.py
1. cat saa-glossary.rdf
