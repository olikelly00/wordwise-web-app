from lib.vocab_fetcher import *
import unittest 
from unittest.mock import MagicMock, patch
import requests

vocab_url = "https://raw.githubusercontent.com/hathibelagal/German-English-JSON-Dictionary/master/english_german.json"

mock_json_template = """{
  "translations": [
    {
      "detected_source_language": "%(lang)s",
      "text": "%(word)s"
    }
  ]
}
"""



@patch('requests.get')
def test_mocked_api_call(mock_api_call):
    mock_api_call.return_value = MagicMock(status_code=200,text=mock_json_template%{"lang": "DE", "word": "Mutter"})
    test_fetch = fetch_vocab_from_api('Mother', 'German')
    assert test_fetch.word_target_language == 'Mutter'


def test_fetch_vocab_from_api_for_word_found():
    test_word = "evening"
    target_language = "German"
    test_fetch = fetch_vocab_from_api(test_word, target_language)
    assert test_fetch.word_target_language.lower() == "abend"

