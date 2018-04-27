import replit
from itertools import product
import urllib.request, urllib.error, urllib.parse
words = []
for line in urllib.request.urlopen('http://www.mieliestronk.com/corncob_lowercase.txt'):
  words.append(line)
words = [x.rstrip() for x in words]
words = [x.decode("utf-8") for x in words]
def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    pass
  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass
  return False
def rerun():
  if input("Press enter to run again!") != "stop":
    run()
def run():
  replit.clear()
  print('')
  print('---------------------------')
  to_from = input("What Is Your Code?: ")
  if is_number(to_from) == False: 
    code = to_from.lower()
    intab = "abcdefghijuvwxyz015.klmnopqrst"
    outtab = "012345678901234567890123456789"
    trans = code.maketrans(intab, outtab)
    uncoded = code.translate(trans)
    print('')
    print('---------------------------')
    print('Translated number:')
    print('')
    print(uncoded)
    rerun()
  else:
    code = to_from
    intab = "0123456789"
    outtab = "abcdefghij"
    trans = code.maketrans(intab, outtab)
    op1 = code.translate(trans)
    intab = "0123456789"
    outtab = "uvwxyz015."
    trans = code.maketrans(intab, outtab)
    op2 = code.translate(trans)
    intab = "0123456789"
    outtab = "klmnopqrst"
    trans = code.maketrans(intab, outtab)
    op3 = code.translate(trans)
    zipped = list(zip(op1, op2, op3))
    print('')
    print('---------------------------')
    print('The letter grid:')
    print('')
    for letter, row in zip(code, zipped):
      print('{} = {}'.format(letter, ' '.join(row)))
    print('')
    print('---------------------------')
    print('All possible combinations:')
    print('')
    comb = []
    for latest in product(*zipped):
        joined = ''.join(latest)
        comb.append(joined)
    listed_all = ', '.join(comb)
    print(listed_all)
    print('')
    print('---------------------------')
    print('All real words in list:')
    print('')
    real = []
    for i in range(len(comb)):
      if comb[i] in words:
        current = comb[i]
        real.append(current)
    listed_real = ', '.join(real)
    print(listed_real)
    print('')
    print('---------------------------')
    rerun()
replit.clear()
run()
