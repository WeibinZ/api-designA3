import unittest
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/..')
sys.path.append(os.path.dirname(__file__) +'/../service')

from unittest.mock import Mock

import service.objects_pb2 as objects_pb2
import objects_pb2
from inventory_client import InventoryClient
from get_book_titles import get_bookTitles

class TestGetBookTitles(unittest.TestCase):
    def test_get_book_title_withMock(self):
        client1 = Mock(spec=InventoryClient)
        client1.get_book.return_value = objects_pb2.Book(title="Book101")
        
        
        titles = get_bookTitles(client=client1,isbnList=["000-0-00000-000-0"])
        
        #get called
        client1.get_book.assert_called_with("000-0-00000-000-0")
        
        #return value
        self.assertEqual(len(titles),1)
        self.assertEqual(titles[0],"Book101")
        
    def test_get_book_title_onServer(self):
        client2 = InventoryClient("localhost","8080")
        
        titles = get_bookTitles(client=client2,isbnList=["978-1-56619-909-4"])
        
        self.assertEqual("Coding bootcamp", titles[0])
        
        
if __name__ == "__main__":
    unittest.main()
