from unittest.mock import Mock
from country_info import get_country_code, get_country_currency, transform

def test_get_country_code():
    # assemble
    
  countries =  [{'name': 'Zambia', 'topLevelDomain': ['.zm'], 'alpha2Code': 'ZM', 'alpha3Code': 'ZMB', 'callingCodes': ['260'], 'capital': 'Lusaka', 'altSpellings': ['ZM', 'Republic of Zambia'], 'subregion': 'Eastern Africa', 'region': 'Africa', 'population': 18383956, 'latlng': [-15.0, 30.0], 'demonym': 'Zambian', 'area': 752618.0, 'gini': 57.1, 'timezones': ['UTC+02:00'], 'borders': ['AGO', 'BWA', 'COD', 'MWI', 'MOZ', 'NAM', 'TZA', 'ZWE'], 'nativeName': 'Zambia', 'numericCode': '894', 'flags': {'svg': 'https://flagcdn.com/zm.svg', 'png': 'https://flagcdn.com/w320/zm.png'}, 'currencies': [{'code': 'ZMW', 'name': 'Zambian kwacha', 'symbol': 'ZK'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'br': 'Zambia', 'pt': 'Zâmbia', 'nl': 'Zambia', 'hr': 'Zambija', 'fa': 'زامبیا', 'de': 'Sambia', 'es': 'Zambia', 'fr': 'Zambie', 'ja': 'ザンビア', 'it': 'Zambia', 'hu': 'Zambia'}, 'flag': 'https://flagcdn.com/zm.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana', 'Umoja wa Afrika']}], 'cioc': 'ZAM', 'independent': True}
  , {'name': 'Zambia', 'country_code': 'ZMB', 'currency_code': 'ZMW'}]


  # act
  
  actual_result = get_country_code(countries, 'Zambia')
  expected_result = 'ZMB'
  
  # assert
  
  assert actual_result == expected_result
  
  
def test_get_country_currency():
      
      # assemble
      
      countries = [ {'name': 'Uzbekistan', 'topLevelDomain': ['.uz'], 'alpha2Code': 'UZ', 'alpha3Code': 'UZB', 'callingCodes': ['998'], 'capital': 'Tashkent', 
      'altSpellings': ['UZ', 'Republic of Uzbekistan', 'O‘zbekiston Respublikasi', 'Ўзбекистон Республикаси'], 'subregion': 'Central Asia', 'region': 'Asia', 'population': 34232050, 'latlng': [41.0, 64.0], 'demonym': 'Uzbekistani', 'area': 447400.0, 'gini': 35.3, 'timezones': ['UTC+05:00'], 'borders': ['AFG', 'KAZ', 'KGZ', 'TJK', 'TKM'], 'nativeName': 'O‘zbekiston', 'numericCode': '860', 'flags': {'svg': 'https://flagcdn.com/uz.svg', 'png': 'https://flagcdn.com/w320/uz.png'}, 'currencies': [{'code': 'UZS', 'name': "Uzbekistani so'm", 
      'symbol': "so'm"}], 'languages': [{'iso639_1': 'uz', 'iso639_2': 'uzb', 'name': 'Uzbek', 'nativeName': 'Oʻzbek'}, {'iso639_1': 'ru', 'iso639_2': 'rus', 'name': 'Russian', 'nativeName': 'Русский'}], 'translations': {'br': 'Ouzbekistan', 'pt': 'Usbequistão', 'nl': 'Oezbekistan', 'hr': 'Uzbekistan', 'fa': 'ازبکستان', 'de': 'Usbekistan', 'es': 'Uzbekistán', 
      'fr': 'Ouzbékistan', 'ja': 'ウズベキスタン', 'it': 'Uzbekistan', 'hu': 'Üzbegisztán'}, 'flag': 'https://flagcdn.com/uz.svg', 'cioc': 'UZB', 'independent': False}
      , {'name': 'Uzbekistan', 'country_code': 'UZB', 'currency_code': 'UZS'}]
          
      # act
      
      actual_result = get_country_currency(countries, 'Uzbekistan')
      expected_result = 'UZS'
      
      # assert
      assert actual_result == expected_result
      
      
def test_transform():
      
      countries_mocked = [{'name': 'Uzbekistan', 'topLevelDomain': ['.uz'], 'alpha2Code': 'UZ', 'alpha3Code': 'UZB', 'callingCodes': ['998'], 'capital': 'Tashkent', 
      'altSpellings': ['UZ', 'Republic of Uzbekistan', 'O‘zbekiston Respublikasi', 'Ўзбекистон Республикаси'], 'subregion': 'Central Asia', 'region': 'Asia', 'population': 34232050, 'latlng': [41.0, 64.0], 'demonym': 'Uzbekistani', 'area': 447400.0, 'gini': 35.3, 'timezones': ['UTC+05:00'], 'borders': ['AFG', 'KAZ', 'KGZ', 'TJK', 'TKM'], 'nativeName': 'O‘zbekiston', 'numericCode': '860', 'flags': {'svg': 'https://flagcdn.com/uz.svg', 'png': 'https://flagcdn.com/w320/uz.png'}, 'currencies': [{'code': 'UZS', 'name': "Uzbekistani so'm", 
      'symbol': "so'm"}], 'languages': [{'iso639_1': 'uz', 'iso639_2': 'uzb', 'name': 'Uzbek', 'nativeName': 'Oʻzbek'}, {'iso639_1': 'ru', 'iso639_2': 'rus', 'name': 'Russian', 'nativeName': 'Русский'}], 'translations': {'br': 'Ouzbekistan', 'pt': 'Usbequistão', 'nl': 'Oezbekistan', 'hr': 'Uzbekistan', 'fa': 'ازبکستان', 'de': 'Usbekistan', 'es': 'Uzbekistán', 
      'fr': 'Ouzbékistan', 'ja': 'ウズベキスタン', 'it': 'Uzbekistan', 'hu': 'Üzbegisztán'}, 'flag': 'https://flagcdn.com/uz.svg', 'cioc': 'UZB', 'independent': False}
      , {'name': 'Uzbekistan', 'country_code': 'UZB', 'currency_code': 'UZS'}, {'name': 'Zambia', 'topLevelDomain': ['.zm'], 'alpha2Code': 'ZM', 'alpha3Code': 'ZMB', 'callingCodes': ['260'], 'capital': 'Lusaka', 'altSpellings': ['ZM', 'Republic of Zambia'], 'subregion': 'Eastern Africa', 'region': 'Africa', 'population': 18383956, 'latlng': [-15.0, 30.0], 'demonym': 'Zambian', 'area': 752618.0, 'gini': 57.1, 'timezones': ['UTC+02:00'], 'borders': ['AGO', 'BWA', 'COD', 'MWI', 'MOZ', 'NAM', 'TZA', 'ZWE'], 'nativeName': 'Zambia', 'numericCode': '894', 'flags': {'svg': 'https://flagcdn.com/zm.svg', 'png': 'https://flagcdn.com/w320/zm.png'}, 'currencies': [{'code': 'ZMW', 'name': 'Zambian kwacha', 'symbol': 'ZK'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'br': 'Zambia', 'pt': 'Zâmbia', 'nl': 'Zambia', 'hr': 'Zambija', 'fa': 'زامبیا', 'de': 'Sambia', 'es': 'Zambia', 'fr': 'Zambie', 'ja': 'ザンビア', 'it': 'Zambia', 'hu': 'Zambia'}, 'flag': 'https://flagcdn.com/zm.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana', 'Umoja wa Afrika']}], 'cioc': 'ZAM', 'independent': True}
      , {'name': 'Zambia', 'country_code': 'ZMB', 'currency_code': 'ZMW'}]
      
      mock_get_countries_function = Mock(return_value = countries_mocked)
      
      #act 
      expected_result = {'name': 'Zambia', 'country_code': 'ZMB', 'currency_code': 'ZMW'}
      actual_result = transform('Zambia', mock_get_countries_function)
      
      #assert 
      
      assert actual_result == expected_result
      
      
      
      

  
    
      
      
  
  
  

    