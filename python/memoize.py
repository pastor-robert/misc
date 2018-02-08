
results = {}
def memoize(f):
  # results = {}
  def memoize(*args):
    try:
      return results[args]
    except KeyError:
      result = f(*args)
      results[args] = result
      return result
  return memoize

@memoize
def square(j):
  print "Computing square({0})".format(j)
  return j*j

@memoize
def diff(i, j):
  print "Computing diff ({0})".format((i,j))
  return i - j

#r = (diff(100,3), diff(100,4), diff(100,5))
#print r
#r = (diff(100,3), diff(100,4), diff(100,5))
#print r
#r = (diff(100,1), diff(100,3), diff(100,7))
#print r
#print results

i = 0

@memoize
def fib(j):
  global i
  i += 1
  print "Computing fib ({0})".format(j)
  if j in (0, 1):
    return 1
  return fib(j-2)+fib(j-1)

print fib(10)
print i
