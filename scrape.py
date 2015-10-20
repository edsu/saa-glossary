#!/usr/bin/env python

import re
import json
import urlparse
import lxml.html

def main():
    # set up the json-ld
    g = {
        "@id": "http://www2.archivists.org/glossary/terms/",
        "@graph": [{
            "@id": "http://www2.archivists.org/glossary/terms/",
            "@type": "ConceptScheme",
            "title": "A Glossary of Archival and Records Terminology"
        }],
        "@context": {
            "@vocab": "http://www.w3.org/2004/02/skos/core#",
            "title": "http://purl.org/dc/terms/title",
            "mads": "http://www.loc.gov/mads/rdf/v1#",
            "citation": "mads:hasSource",
            "source": "mads:citationSource",
            "quotation": "mads:citationNote",
            "status": "mads:citationStatus",
            "distinguish": "http://www2.archivists.org/glossary#distinguish"
        }
    }

    # scrape it!
    label_uris = {}
    for t in terms():
        print t['prefLabel']
        label_uris[t['prefLabel']] = t['@id']
        g["@graph"].append(t)

    # remove empty lists
    for concept in g['@graph']:
        for p in concept.keys():
            if type(concept[p]) == list and len(concept[p]) == 0:
                del concept[p]

    # all done
    open("saa-glossary.json", "w").write(json.dumps(g, indent=2))

def terms():
    for url in term_urls():
        t = term(url)
        if t: yield t

def term_urls():
    for letter in [chr(i) for i in  range(97, 123)]:
        url = 'http://www2.archivists.org/glossary/terms/' + letter
        while True:
            doc = lxml.html.parse(url)
            for a in doc.xpath('.//a'):
                href = a.attrib['href']
                if re.match(r'^/glossary/terms/./.+$', href):
                    yield urlparse.urljoin("http://www2.archivists.org", href)
            next_page = doc.xpath('string(.//li[@class="pager-next"]/a/@href)')
            if next_page:
                url = urlparse.urljoin("http://www2.archivists.org/", next_page)
            else:
                break

def term(url):
    term = {
        '@id': url, 
        '@type': 'Concept',
        'prefLabel': None, 
        'definition': None,
        'altLabel': [], 
        'broader': [],
        'narrower': [],
        'related': [],
        'distinguish': [],
        'scopeNote': [],
        'citation': []
    }
    doc = lxml.html.parse(url)
    main = doc.find('.//div/[@id="main"]')

    term['prefLabel'] = main.find('.//h1[@class="title"]').text

    term['definition'] = main.find('.//div[@class="content"]/p')
    if term['definition'] == None:
        return

    term['definition'] = term['definition'].text_content()
    term['definition'] = re.sub('^\(also.+?\), ', '', term['definition'])

    for e in main.xpath('.//div[@class="node odd full-node node-type-glossary_term"]/div/p/span[@class="sublemma"]'):
        term['altLabel'].append(e.text)
    
    for e in main.xpath(".//div[@class='field-items']//p"):
        term['scopeNote'].append(e.text_content())

    for e in main.xpath('.//div[@class="citation"]'):
        c = citation(e)
        if c: term['citation'].append(c)

    term['broader'] = syndetic_links(doc, "broader", url)
    term['related'] = syndetic_links(doc, "related", url)
    term['distinguish'] = syndetic_links(doc, "distinguish", url)
    term['narrower'] = syndetic_links(doc, "narrower", url)

    return term

def syndetic_links(doc, label, url):
    links = []
    xpath = ".//div[@class='field field-type-nodereference field-field-" + label + "-term']//a"
    for a in doc.findall(xpath):
        links.append({
            'prefLabel': a.text, 
            '@id': urlparse.urljoin(url, a.attrib['href'])
        })
    return links 

def citation(cite):
    a = cite.find('a')
    url = urlparse.urljoin('http://www2.archivists.org/', a.attrib['href'])
    doc = lxml.html.parse(url)
    e = doc.find('.//div[@class="citation-source-node"]')
    if e == None: return
    source = e.find('.//p').text_content()
    return {
      "quotation": cite.text_content().strip(),
      "source": source,
      "@id": url
    }

if __name__ == "__main__":
    main()
