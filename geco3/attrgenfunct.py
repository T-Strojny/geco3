# Functions that can generate attribute values.
#
# These are functions that can be used in the GenerateFuncAttribute() class
# (see module generator.py). They generate values according to some internal
# functionality.
#
# The requirement of any such functions are:
# 1) that it must return a string
# 2) it can have been 0 and 5 parameters
# 
#
# Examples of such functions are:
# - Australian telephone numbers
# - Japanese telephone numbers
# - Credit card numbers
# - US social security numbers
# - Japanese social security numbers
# - Uniformly distributed age values between 0 and 100
# - Normally distributed age values between 0 and 110
# etc.

# Original work:
# Peter Christen and Dinusha Vatsalan, January-March 2012
#
# Modified work:
# Tymoteusz Strojny, August 2024
# - Converted from Python 2 to Python 3
# - Added generate_phone_number_poland and generate_birthdate functions
#
# =============================================================================
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# =============================================================================
#
#  Modifications:
#  The original code has been modified from its original form.
#  It was initially written for Python 2 and has been converted to Python 3.
#
#  The modified code remains subject to the terms of the Mozilla Public
#  License, v. 2.0.
# =============================================================================

import random
from datetime import datetime
import geco3.basefunctions as basefunctions

# -----------------------------------------------------------------------------
#
def generate_phone_number_australia():
  """Randomly generate an Australian telephone number made of a two-digit area
     code and an eight-digit number made of two blocks of four digits (with a
     space between). For example: `02 1234 5678'

     For details see: http://en.wikipedia.org/wiki/ \
                      Telephone_numbers_in_Australia#Personal_numbers_.2805.29
  """
  
  area_code = random.choice(['02', '03', '04', '07', '08'])

  number1 = random.randint(1,9999)
  number2 = random.randint(1,9999)

  oz_phone_str = str(area_code)+' '+str(number1).zfill(4)+' '+ \
                 str(number2).zfill(4)
  assert len(oz_phone_str) == 12
  assert oz_phone_str[0] == '0'

  return oz_phone_str

# -----------------------------------------------------------------------------
#
def generate_phone_number_poland():
  """Randomly generate a Polish telephone number made of a two-digit prefix and seven-digit number."""
  num = []

  prefix = random.choice(["45","50", "51", "53", "57", "60", "66", "69", "72", "73", "78", "79", "88"] )
  num.append(prefix)

  for _ in range(7):
    number1 = random.randint(0, 9)
    num.append(str(number1))
  return "".join(num)

# -----------------------------------------------------------------------------
#

def generate_birthdate(mode_age=35, distribution="triangular", year_only=True, format=None):
  """Generate birthdate as a String, depending on year_only generate either year of birth or date of birth
  params:
    mode_age : int : mode age in a population, used for triangular distribution, must be less than 100.
  
    distribution : String : distribution from which birthyears will be generated.
      Options -> ["normal", "triangular", "uniform"]
    year_only : bool : decide if function should retrun birthyear or birthdate.

    format : String : format in which birthdate should be generated.
      Options -> ["MM/DD/YYYY", "DD/MM/YYYY", "YYYY/MM/DD"] 

  return : String : birthdate or birthyear"""
  
  current_year = datetime.now().year
  min_year = current_year - 100
  mode_year = current_year - mode_age

  if distribution == 'uniform':
    return_year = random.randint(min_year, current_year)
      
  elif distribution == 'triangular':
    return_year = int(random.triangular(min_year, current_year, mode_year))
      
  elif distribution == 'normal':
    mean = current_year - 40
    std_dev = 15
    year = int(random.gauss(mean, std_dev))
    return_year =  max(min_year, min(year, current_year))

  else:
    raise ValueError("Invalid distribution. Choose 'uniform', 'triangular' or 'normal'")
  
  #----------------------------------------------------------------------------

  if year_only:
    return str(return_year)
  
  elif year_only == False:
    is_leap = (return_year % 4 == 0 and return_year % 100 != 0) or (return_year % 400 == 0)

    days_in_month = {
        1: 31, 2: 29 if is_leap else 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    month = random.randint(1, 12)
    day = random.randint(1, days_in_month[month])

    if format == 'MM/DD/YYYY':
      return f"{month:02d}/{day:02d}/{return_year}"
    elif format == 'DD/MM/YYYY':
      return f"{day:02d}/{month:02d}/{return_year}"
    elif format == "YYYY/MM/DD":
      return f"{return_year}/{month:02d}/{day:02d}"
    else:
      raise ValueError("Invalid format. Use 'MM/DD/YYYY' or 'DD/MM/YYYY' or 'YYYY/MM/DD'.")
  
  else:
    raise ValueError("Incorrect year_only value. Select True or False")
  
# -----------------------------------------------------------------------------
#
def generate_credit_card_number():
  """Randomly generate a credit card made of four four-digit numbers (with a
     space between each number group). For example: '1234 5678 9012 3456'

     For details see: http://en.wikipedia.org/wiki/Bank_card_number
  """

  number1 = random.randint(1,9999)
  assert number1 > 0

  number2 = random.randint(1,9999)
  assert number2 > 0

  number3 = random.randint(1,9999)
  assert number3 > 0

  number4 = random.randint(1,9999)
  assert number4 > 0

  cc_str = str(number1).zfill(4)+' '+str(number2).zfill(4)+' '+ \
           str(number3).zfill(4)+' '+str(number4).zfill(4)

  assert len(cc_str) == 19

  return cc_str

# -----------------------------------------------------------------------------
#
def generate_uniform_value(min_val, max_val, val_type):
  """Randomly generate a numerical value according to a uniform distribution
     between the minimum and maximum values given.

     The value type can be set as 'int', so a string formatted as an integer
     value is returned; or as 'float1' to 'float9', in which case a string
     formatted as floating-point value with the specified number of digits
     behind the comma is returned.

     Note that for certain situations and string formats a value outside the
     set range might be returned. For example, if min_val=100.25 and
     val_type='float1' the rounding can result in a string value '100.2' to
     be returned.

     Suitable minimum and maximum values need to be selected to prevent such a
     situation.
  """

  basefunctions.check_is_number('min_val', min_val)
  basefunctions.check_is_number('max_val', max_val)
  assert min_val < max_val

  r = random.uniform(min_val, max_val)

  return basefunctions.float_to_str(r, val_type)

# -----------------------------------------------------------------------------
#
def generate_uniform_age(min_val, max_val):
  """Randomly generate an age value (returned as integer) according to a
     uniform distribution between the minimum and maximum values given.

     This function is simple a shorthand for:

       generate_uniform_value(min_val, max_val, 'int')
  """

  assert min_val >= 0
  assert max_val <= 130

  return generate_uniform_value(min_val, max_val, 'int')

# -----------------------------------------------------------------------------

def generate_normal_value(mu, sigma, min_val, max_val, val_type):
  """Randomly generate a numerical value according to a normal distribution
     with the mean (mu) and standard deviation (sigma) given.

     A minimum and maximum allowed value can given as additional parameters,
     if set to None then no minimum and/or maximum limit is set.

     The value type can be set as 'int', so a string formatted as an integer
     value is returned; or as 'float1' to 'float9', in which case a string
     formatted as floating-point value with the specified number of digits
     behind the comma is returned.
  """

  basefunctions.check_is_number('mu', mu)
  basefunctions.check_is_number('sigma', sigma)
  assert sigma > 0.0

  if (min_val != None):
    basefunctions.check_is_number('min_val', min_val)
    assert min_val <= mu

  if (max_val != None):
    basefunctions.check_is_number('max_val', max_val)
    assert max_val >= mu

  if ((min_val != None) and (max_val != None)):
    assert min_val < max_val

  if (min_val != None) or (max_val != None):
    in_range = False  # For testing if the random value is with the range
  else:
    in_range = True

  r = random.normalvariate(mu, sigma)

  while (in_range == False):
    if ((min_val == None) or ((min_val != None) and (r >= min_val))):
      in_range = True

    if ((max_val != None) and (r > max_val)):
      in_range = False

    if (in_range == True):
      r_str = basefunctions.float_to_str(r, val_type)
      r_test = float(r_str)
      if (min_val != None) and (r_test < min_val):
        in_range = False
      if (max_val != None) and (r_test > max_val):
        in_range = False

    if (in_range == False):
      r = random.normalvariate(mu, sigma)

  if (min_val != None):
    assert r >= min_val
  if (max_val != None):
    assert r <= max_val

  return basefunctions.float_to_str(r, val_type)

# -----------------------------------------------------------------------------
#
def generate_normal_age(mu, sigma, min_val, max_val):
  """Randomly generate an age value (returned as integer) according to a
     normal distribution following the mean and standard deviation values
     given, and limited to age values between (including) the minimum and
     maximum values given.

     This function is simple a shorthand for:

       generate_normal_value(mu, sigma, min_val, max_val, 'int')
  """

  assert min_val >= 0
  assert max_val <= 130

  age = generate_normal_value(mu, sigma, min_val, max_val, 'int')

  while ((int(age) < min_val) or (int(age) > max_val)):
    age = generate_normal_value(mu, sigma, min_val, max_val, 'int')

  return age

# =============================================================================

# If called from command line perform some examples: Generate values
#
if (__name__ == '__main__'):

  num_test = 20

  print(f'Generate {num_test} Australian telephone numbers:')
  for i in range(num_test):
    print(' ', generate_phone_number_australia())
  print()

  print(f"Generate {num_test} Polish telephone numbers:")
  for i in range(num_test):
    print(" ", generate_phone_number_poland())
  print()

  print('Generate %d credit card numbers:' % (num_test))
  for i in range(num_test):
    print(' ', generate_credit_card_number())
  print()

  print(f'Generate {num_test} uniformly distributed integer numbers between -100 and -5:')
  for i in range(num_test):
    print(' ', generate_uniform_value(-100, -5, 'int'), end=' ')
  print()

  print(f'Generate {num_test} uniformly distributed floating-point numbers with 3 digits between -55 and 55:')
  for i in range(num_test):
    print(' ', generate_uniform_value(-55, 55, 'float3'))
  print()

  print(f'Generate {num_test} uniformly distributed floating-point numbers with 7 digits between 147 and 9843:')
  for i in range(num_test):
    print(' ', generate_uniform_value(147, 9843, 'float7'))
  print()

  print(f'Generate {num_test} uniformly distributed age values between 0 and 120:')
  for i in range(num_test):
    print(' ', generate_uniform_age(0, 120))
  print()

  print(f'Generate {num_test} uniformly distributed age values between 18 and 65:')
  for i in range(num_test):
    print(' ', generate_uniform_age(18, 65))
  print()

  print(
    f'Generate {num_test} normally distributed integer numbers between -200 and -3 with mean -50 and standard deviation 44:')
  for i in range(num_test):
    print(' ', generate_normal_value(-50, 44, -200, -3, 'int'))
  print()

  print(
    f'Generate {num_test} normally distributed floating-point numbers with 5 digits between -100 and 100 and with mean 22 and standard deviation 74:')
  for i in range(num_test):
    print(' ', generate_normal_value(22, 74, -100, 100, 'float5'))
  print()

  print(
    f'Generate {num_test} normally distributed floating-point numbers with 9 digits with mean 22 and standard deviation 74:')
  for i in range(num_test):
    print(' ', generate_normal_value(22, 74, min_val=None, max_val=None, val_type='float9'))
  print()

  print(
    f'Generate {num_test} normally distributed floating-point numbers with 2 digits with mean 22 and standard deviation 24 that are larger than 10:')
  for i in range(num_test):
    print(' ', generate_normal_value(22, 74, min_val=10, max_val=None, val_type='float2'))
  print()

  print(
    f'Generate {num_test} normally distributed floating-point numbers with 4 digits with mean 22 and standard deviation 24 that are smaller than 30:')
  for i in range(num_test):
    print(' ', generate_normal_value(22, 74, min_val=None, max_val=40, val_type='float4'))
  print()

  print(
    f'Generate {num_test} normally distributed age values between 0 and 120 with mean 45 and standard deviation 22:')
  for i in range(num_test):
    print(' ', generate_normal_age(45, 22, 0, 120))
  print()

  print(
    f'Generate {num_test} normally distributed age values between 18 and 65 with mean 30 and standard deviation 10:')
  for i in range(num_test):
    print(' ', generate_normal_age(30, 10, 18, 65))
  print()