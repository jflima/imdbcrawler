import unittest
import crawler

class TestDownloadData(unittest.TestCase):
    def test_data_obtention(self):
        crawler.collect_movie_files()
        
