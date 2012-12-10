#!/usr/bin/env python

import json
import rdflib

glossary_uri = rdflib.URIRef("http://www2.archivists.org/glossary")
skos = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
mads = rdflib.Namespace("http://www.loc.gov/mads/rdf/v1#")
dcterms = rdflib.Namespace("http://purl.org/dc/terms/")
graph = rdflib.Graph()
glossary = json.loads(open("saa-glossary.json").read())

graph.add((glossary_uri, dcterms.title, rdflib.Literal("A Glossary of Archival and Records Terminology")))
graph.add((glossary_uri, dcterms.publisher, rdflib.Literal("Society of American Archivists")))
graph.add((glossary_uri, rdflib.RDF.type, skos.ConceptScheme))


for pref_label in glossary.keys():
    term = glossary[pref_label]
    uri = rdflib.URIRef(term["url"])
    graph.add((uri, rdflib.RDF.type, skos.Concept))
    graph.add((uri, skos.prefLabel, rdflib.Literal(pref_label)))
    graph.add((uri, skos.definition, rdflib.Literal(term["definition"])))
    graph.add((uri, skos.inScheme, glossary_uri))
    
    for alt_label in term["alt_label"]:
        graph.add((uri, skos.altLabel, rdflib.Literal(alt_label)))

    for b in term["broader"]:
        graph.add((uri, skos.broader, rdflib.URIRef(b["url"])))
    for n in term["narrower"]:
        graph.add((uri, skos.narrower, rdflib.URIRef(n["url"])))
    for r in term["related"]:
        graph.add((uri, skos.related, rdflib.URIRef(r["url"])))

    for n in term["scope_notes"]:
        graph.add((uri, skos.scopeNote, rdflib.Literal(n)))

    for n in term["citations"]:
        bnode = rdflib.BNode()
        graph.add((uri, mads.hasSource, bnode))
        graph.add((bnode, rdflib.RDF.type, mads.Source))
        graph.add((bnode, mads.citationSource, rdflib.Literal(n['source'])))
        graph.add((bnode, mads.citationNote, rdflib.Literal(n['quotation'])))
        graph.add((bnode, mads.citationStatus, rdflib.Literal('found')))

graph.bind("skos", skos)
graph.bind("mads", mads)
graph.bind("dcterms", dcterms)
graph.serialize(open("saa-glossary.rdf", "w"))
graph.serialize(open("saa-glossary.ttl", "w"), format="turtle")
