from .basefunctions import *
from .generator import *
from .corruptor import *

from .attrgenfunct import *

from .contdepfunct import *

__all__ = [
    #basefunctions
    'check_is_not_none', 'check_is_string', 'check_is_unicode_string',
    'check_is_number', 'check_is_positive', 'check_is_not_negative',
    'check_is_normalised', 'check_is_integer', 'check_is_float',
    'check_is_dictionary', 'check_is_list', 'check_is_set',
    'check_is_tuple', 'check_is_flag', 'check_unicode_encoding_exists',
    'char_set_ascii', 'char_set_unicode', 'float_to_str',
    'str2comma_separated_list', 'read_csv_file', 'write_csv_file',
    
    #generator
    'GenerateAttribute', 'GenerateCateCateCompoundAttribute',
    'GenerateCateContCompoundAttribute', 'GenerateContContCompoundAttribute',
    'GenerateDataSet',
    
    #corruptor
    'CorruptDataSet', 'CorruptValue', 'CorruptCategoricalValue',
    'CorruptNumericValue',
    
    #attrgenfunct
    'generate_phone_number_australia',
    
]

import logging
logging.basicConfig(level=logging.INFO)

__version__ = 'v0.1.0-alpha'
