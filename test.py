#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrape
import unittest

class SaaTests(unittest.TestCase):

    def test_term_urls(self):
        self.assertTrue(len(list(scrape.term_urls())) > 2000)

    def test_term(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/a/arrangement")
        self.assertEqual(term['prefLabel'], 'arrangement')
        self.assertTrue(term['definition'].startswith('n. ~ 1. The process of organizing materials with respect to their provenance and original order, to protect their context and to achieve physical or intellectual control over the materials.'))
        self.assertEqual(len(term['scopeNote']), 3)
        self.assertEqual(term['scopeNote'][2], "Arrangement is distinguished from classification, which places materials in an order established by someone other than the creator.")
        self.assertEqual(len(term['citation']), 2)
        self.assertEqual(term['citation'][0]['source'], u'Holmes, Oliver W., Archival Arrangement \u2013 Five Different Operations at Five Different Levels. Modern Archives Reader: Basic Readings on Archival Theory and Practice. National Archives and Records Service, 1984, p. 162\u2013180.')

        self.assertEqual(len(term['broader']), 1)
        self.assertEqual(term['broader'][0]['prefLabel'], 'processing')
        self.assertEqual(term['broader'][0]['@id'], 'http://www2.archivists.org/glossary/terms/p/processing')
        self.assertEqual(len(term['related']), 2)
        self.assertEqual(term['related'][0]['prefLabel'], 'original order')
        self.assertEqual(term['related'][0]['@id'], 'http://www2.archivists.org/glossary/terms/o/original-order')
        self.assertEqual(term['related'][1]['prefLabel'], 'provenance')
        self.assertEqual(term['related'][1]['@id'], 'http://www2.archivists.org/glossary/terms/p/provenance')
        self.assertEqual(len(term['distinguish']), 1)
        self.assertEqual(term['distinguish'][0]['prefLabel'], 'classification')
        self.assertEqual(term['distinguish'][0]['@id'], 'http://www2.archivists.org/glossary/terms/c/classification')


    def test_altLabel(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/c/central-records")
        self.assertEqual(term['prefLabel'], 'central records')
        self.assertEqual(term['definition'], u'n. ~ 1. The files of several organizational units consolidated in one location. - 2. The files of several individuals consolidated into a common filing system.')
        self.assertEqual(len(term['altLabel']), 2)
        self.assertEqual(term['altLabel'][0], 'central files')
        self.assertEqual(term['altLabel'][1], 'centralized files')

    def test_abbreviation(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/a/american-library-association")
        self.assertEqual(term['prefLabel'], "American Library Association")
        self.assertEqual(len(term['altLabel']), 1)
        self.assertEqual(term['altLabel'][0], 'ALA')

    def test_another(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/a/audiotape")
        self.assertTrue(term)
        self.assertEqual(term['altLabel'][0], 'phonotape')

    def test_alt_labels(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/p/provenance")
        self.assertEqual(len(term["altLabel"]), 1)
        self.assertEqual(term["altLabel"][0], "provenancial")

    def test_scope_note(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/r/reversibility")
        self.assertEqual(term["scopeNote"][0], "Sometimes referred to as the principle of reversibility.  Encapsulation is considered reversible, whereas lamination is not.")




if __name__ == "__main__":
    unittest.main()
