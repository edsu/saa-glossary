#!/usr/bin/env python

import json
import rdflib

skos = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
graph = rdflib.Graph()
glossary = json.loads(open("saa-glossary.json").read())

for pref_label in glossary.keys():
    term = glossary[pref_label]
    uri = rdflib.URIRef(term["url"])
    graph.add((uri, rdflib.RDF.type, skos.Concept))
    graph.add((uri, skos.prefLabel, rdflib.Literal(pref_label)))
    graph.add((uri, skos.definition, rdflib.Literal(term["definition"])))
    
    for alt_label in term["alt_label"]:
        graph.add((uri, skos.altLabel, rdflib.Literal(alt_label)))

    for b in term["broader"]:
        graph.add((uri, skos.broader, rdflib.URIRef(b["url"])))
    for n in term["narrower"]:
        graph.add((uri, skos.narrower, rdflib.URIRef(n["url"])))
    for r in term["related"]:
        graph.add((uri, skos.related, rdflib.URIRef(r["url"])))

    for n in term["notes"]:
        graph.add((uri, skos.scopeNote, rdflib.Literal(n)))

graph.bind("skos", skos)
graph.serialize(open("saa-glossary.rdf", "w"))
graph.serialize(open("saa-glossary.ttl", "w"), format="turtle")
