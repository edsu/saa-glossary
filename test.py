#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrape
import unittest

class SaaTests(unittest.TestCase):

    def test_term_urls(self):
        self.assertTrue(len(list(scrape.term_urls())) > 2000)

    def atest_term(self):
        term = scrape.term("http://www.archivists.org/glossary/term_details.asp?DefinitionKey=294")
        self.assertEqual(term['pref_label'], 'arrangement')
        self.assertTrue(term['definition'].startswith('n. ~ 1. The process of organizing materials with respect to their provenance and original order, to protect their context and to achieve physical or intellectual control over the materials.'))
        self.assertEqual(len(term['notes']), 3)
        self.assertEqual(term['notes'][2], "Arrangement is distinguished from classification, which places materials in an order established by someone other than the creator.")
        self.assertEqual(len(term['citations']), 2)
        self.assertEqual(term['citations'][0]['author'], 'Holmes, Oliver W.')
        self.assertEqual(term['citations'][0]['source'], u'"Archival Arrangement \x96 Five Different Operations at Five Different Levels.," Modern Archives Reader: Basic Readings on Archival Theory and Practice. National Archives and Records Service, 1984, p. 162\x96180. Edited by Maygene F. Daniels and Timothy Walch.')
        self.assertEqual(len(term['broader']), 1)
        self.assertEqual(term['broader'][0]['pref_label'], 'processing')
        self.assertEqual(term['broader'][0]['url'], 'http://www.archivists.org/glossary/term_details.asp?DefinitionKey=431')
        self.assertEqual(len(term['related']), 2)
        self.assertEqual(term['related'][0]['pref_label'], 'original order')
        self.assertEqual(term['related'][0]['url'], 'http://www.archivists.org/glossary/term_details.asp?DefinitionKey=69')
        self.assertEqual(term['related'][1]['pref_label'], 'provenance')
        self.assertEqual(term['related'][1]['url'], 'http://www.archivists.org/glossary/term_details.asp?DefinitionKey=196')
        self.assertEqual(len(term['distinguish_from']), 1)
        self.assertEqual(term['distinguish_from'][0]['pref_label'], 'classification')
        self.assertEqual(term['distinguish_from'][0]['url'], 'http://www.archivists.org/glossary/term_details.asp?DefinitionKey=283')


    def atest_alt_label(self):
        term = scrape.term("http://www.archivists.org/glossary/term_details.asp?DefinitionKey=588")
        self.assertEqual(term['pref_label'], 'central records')
        self.assertEqual(term['definition'], u'n. ~ 1. The files of several organizational units consolidated in one location. \x96 2. The files of several individuals consolidated into a common filing system.')
        self.assertEqual(len(term['alt_label']), 2)
        self.assertEqual(term['alt_label'][0], 'central files')
        self.assertEqual(term['alt_label'][1], 'centralized files')

    def atest_no_term(self):
        term = scrape.term("http://www.archivists.org/glossary/term_details.asp?DefinitionKey=11")
        self.assertEqual(term, None)
        term = scrape.term("http://www.archivists.org/glossary/term_details.asp?DefinitionKey=480")
        self.assertEqual(term, None)

    def atest_abbreviation(self):
        term = scrape.term("http://www.archivists.org/glossary/term_details.asp?DefinitionKey=1907")
        self.assertEqual(term['pref_label'], "American Library Association")
        self.assertEqual(len(term['alt_label']), 1)
        self.assertEqual(term['alt_label'][0], 'ALA')

    def atest_another(self):
        term = scrape.term("http://www.archivists.org/glossary/term_details.asp?DefinitionKey=535")
        self.assertTrue(term)
        self.assertEqual(term['alt_label'][0], 'phonotape')

if __name__ == "__main__":
    unittest.main()
