import sys
# encoding: utf-8

roman_numerals = (
  (1000, u'M'),
  ( 900, u'CM'),
  ( 500, u'D'),
  ( 400, u'CD'),
  ( 100, u'C'),
  (  90, u'XC'),
  ( 50,  u'L'),
  ( 40,  u'XL'),
  ( 10,  u'X'),
  (  9,  u'IX'),
  (  5,  u'V'),
  (  4,  u'IV'),
  (  1,  u'I'),
)

roman_numerals_u = (
  (1000, u'Ⅿ'),
  ( 900, u'ⅭⅯ'),
  ( 500, u'Ⅾ'),
  ( 400, u'ⅭⅮ'),
  ( 100, u'Ⅽ'),
  (  90, u'ⅩⅭ'),
  ( 50,  u'Ⅼ'),
  ( 40,  u'ⅩL'),
  ( 10,  u'Ⅹ'),
  (  9,  u'Ⅸ'),
  (  8,  u'Ⅷ'),
  (  7,  u'Ⅶ'),
  (  6,  u'Ⅵ'),
  (  5,  u'Ⅴ'),
  (  4,  u'Ⅳ'),
  (  3,  u'Ⅲ'),
  (  2,  u'Ⅱ'),
  (  1,  u'Ⅰ'),
)


def roman(n):
  n = int(n)
  roman = u''
  for unit, symbol in roman_numerals_u:
    roman += symbol * (n / unit)
    n %= unit
  return roman

#for arg in sys.argv[1:]:
#  print roman(arg)
for arg in range(101):
  print roman(arg).encode('utf8')
