import unittest
import 
class TestS3Storage(unittest.TestCase):

    def test_it_allow_store_files(self):
        storage = self.there_is_s3_storage()
        file_to_be_up = self.there_is_file()
        #Acct
        storage.save(
            path='test_plik.txt',
            file_to_be_uploaded=file_to_be_up
        )
        #Assert
        assert storage.contains(path='test_plik.txt')

    def there_is_s3_storage(self):
        pass 
    
    def there_is_file(self):
        pass 
