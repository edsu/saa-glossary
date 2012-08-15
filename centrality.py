#!/usr/bin/env python

import json
import networkx

saa = json.loads(open("saa-glossary.json").read())

g = networkx.Graph()

for term in saa.values():
    for broader in term['broader']:
        g.add_edge(term['pref_label'], broader['pref_label'], type='broader')
    for narrower in term['narrower']:
        g.add_edge(term['pref_label'], narrower['pref_label'], type='narrower')
    for related in term['related']:
        g.add_edge(term['pref_label'], related['pref_label'], type='related')

centrality = networkx.eigenvector_centrality(g, max_iter=1000)
terms = g.nodes()
terms.sort(lambda a, b: cmp(centrality[b], centrality[a]))

for label in terms:
    print ("%s\t%s" % (label, centrality[label])).encode('utf-8')
