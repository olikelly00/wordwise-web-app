import os
import json
import requests
from datetime import datetime
from lib.word_repository import Word
from dotenv import load_dotenv

load_dotenv() 

language_menu = {
    "English": {"abbreviation": "EN", "flag_emoji": "🇬🇧"},
    "Czech": {"abbreviation": "CS", "flag_emoji": "🇨🇿"},
    "Arabic": {"abbreviation": "AR", "flag_emoji": "🇸🇦"},
    "Danish": {"abbreviation": "DA", "flag_emoji": "🇩🇰"},
    "Greek": {"abbreviation": "EL", "flag_emoji": "🇬🇷"},
    "Estonian": {"abbreviation": "ET", "flag_emoji": "🇪🇪"},
    "Finnish": {"abbreviation": "FI", "flag_emoji": "🇫🇮"},
    "Hungarian": {"abbreviation": "HU", "flag_emoji": "🇭🇺"},
    "Japanese": {"abbreviation": "JA", "flag_emoji": "🇯🇵"},
    "Korean": {"abbreviation": "KO", "flag_emoji": "🇰🇷"},
    "Dutch": {"abbreviation": "NL", "flag_emoji": "🇳🇱"},
    "Polish": {"abbreviation": "PL", "flag_emoji": "🇵🇱"},
    "Russian": {"abbreviation": "RU", "flag_emoji": "🇷🇺"},
    "French": {"abbreviation": "FR", "flag_emoji": "🇫🇷"},
    "German": {"abbreviation": "DE", "flag_emoji": "🇩🇪"},
    "Spanish": {"abbreviation": "ES", "flag_emoji": "🇪🇸"},
    "Italian": {"abbreviation": "IT", "flag_emoji": "🇮🇹"}
}

def fetch_vocab_from_api(text, target_lang):
    api_url = "https://api-free.deepl.com/v2/translate"
    auth_key = os.getenv("API_KEY")
    if not auth_key:
        return "API_KEY not found"
    params = {
        "auth_key": auth_key,
        "text": text.lower(),
        "target_lang": language_menu[target_lang]['abbreviation']
        }
        
    response = requests.get(api_url, params=params)
    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"
    payload = response.text
    vocab = json.loads(payload)
    print(vocab)
    result = convert_word_to_object(text, vocab, target_lang)
    print(result)
    return result

def convert_word_to_object(text, vocab, target_lang):
    timestamp = datetime.now().strftime('%m/%d/%y %H:%M:%S')
    word = Word(id = None, source_language = [x for x in language_menu if language_menu[x]['abbreviation'] == vocab['translations'][0]['detected_source_language']][0], target_language = target_lang, word_source_language = text, word_target_language = vocab['translations'][0]['text'], time_stamp = timestamp, user_id = 0)
    return word

def display_word_target_language(word):
    return word.word_target_language

