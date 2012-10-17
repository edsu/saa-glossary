#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrape
import unittest

class SaaTests(unittest.TestCase):

    def atest_term_urls(self):
        self.assertTrue(len(list(scrape.term_urls())) > 2000)

    def test_term(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/a/arrangement")
        self.assertEqual(term['pref_label'], 'arrangement')
        self.assertTrue(term['definition'].startswith('n. ~ 1. The process of organizing materials with respect to their provenance and original order, to protect their context and to achieve physical or intellectual control over the materials.'))
        self.assertEqual(len(term['notes']), 3)
        self.assertEqual(term['notes'][2], "Arrangement is distinguished from classification, which places materials in an order established by someone other than the creator.")
        self.assertEqual(len(term['citations']), 2)
        self.assertTrue(term['citations'][0]['source'].startswith(u'Holmes, Oliver'))

        self.assertEqual(len(term['broader']), 1)
        self.assertEqual(term['broader'][0]['pref_label'], 'processing')
        self.assertEqual(term['broader'][0]['url'], 'http://www2.archivists.org/glossary/terms/p/processing')
        self.assertEqual(len(term['related']), 2)
        self.assertEqual(term['related'][0]['pref_label'], 'original order')
        self.assertEqual(term['related'][0]['url'], 'http://www2.archivists.org/glossary/terms/o/original-order')
        self.assertEqual(term['related'][1]['pref_label'], 'provenance')
        self.assertEqual(term['related'][1]['url'], 'http://www2.archivists.org/glossary/terms/p/provenance')
        self.assertEqual(len(term['distinguish_from']), 1)
        self.assertEqual(term['distinguish_from'][0]['pref_label'], 'classification')
        self.assertEqual(term['distinguish_from'][0]['url'], 'http://www2.archivists.org/glossary/terms/c/classification')


    def test_alt_label(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/c/central-records")
        self.assertEqual(term['pref_label'], 'central records')
        self.assertEqual(term['definition'], u'n. ~ 1. The files of several organizational units consolidated in one location. - 2. The files of several individuals consolidated into a common filing system.')
        self.assertEqual(len(term['alt_label']), 2)
        self.assertEqual(term['alt_label'][0], 'central files')
        self.assertEqual(term['alt_label'][1], 'centralized files')

    def test_abbreviation(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/a/american-library-association")
        self.assertEqual(term['pref_label'], "American Library Association")
        self.assertEqual(len(term['alt_label']), 1)
        self.assertEqual(term['alt_label'][0], 'ALA')

    def test_another(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/a/audiotape")
        self.assertTrue(term)
        self.assertEqual(term['alt_label'][0], 'phonotape')

    def test_alt_labels(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/p/provenance")
        print term["alt_label"]
        self.assertEqual(len(term["alt_label"]), 1)
        self.assertEqual(term["alt_label"][0], "provenancial")

    def test_note(self):
        term = scrape.term("http://www2.archivists.org/glossary/terms/r/reversibility")
        self.assertEqual(term["notes"][0], "Sometimes referred to as the principle of reversibility.  Encapsulation is considered reversible, whereas lamination is not.")




if __name__ == "__main__":
    unittest.main()
