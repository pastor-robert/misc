# Annotation wrapper annotation method
def unimplemented(defaultval):
    print defaultval, type(defaultval)
    if(type(defaultval) == type(unimplemented)):
        return lambda: None
    else:
        # Actual annotation
        def unimp_wrapper(func):
            # What we replace the function with
            def wrapper(*arg):
                return defaultval
            return wrapper
        return unimp_wrapper

def g():
  return 9

@unimplemented(7)
def f():
  return 8

print f()
