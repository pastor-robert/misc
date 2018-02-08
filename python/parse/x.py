import pyparsing as pp

def to_dict(*args):
    print "TO_DICT:", args

dictionary = pp.Forward()
identifier = pp.Word(pp.alphas, pp.alphanums)
number = pp.Word(pp.nums).setParseAction(lambda toks: int(toks[0]))
value = number | pp.quotedString | dictionary
pair = (identifier + pp.Suppress(':') + value).setParseAction(
    lambda toks: tuple(toks))
pairs = pp.OneOrMore(pair).setParseAction(to_dict)
dictionary << (pp.Suppress('{') + pairs + pp.Suppress('}'))

in_string =  '''name: "data dict" id: 2
v6: false
stats {
  hosts {
    cnt1: 256
    cnt2: 0
  }
  groups {
    cnt1: 1
    cnt2: 0
  }
  main_groups {
    cnt1: 1
    cnt2: 0
  }
  main_hosts {
    cnt1: 256
    cnt2: 0
  }
}
 group_id: "None"'''

out_dict = {
'name': "data dict",
'id': 2,
'v6': False,
'stats': {
    'hosts': {
        'cnt': 1, 'cnt': 2
    },
    'groups': {
        'cnt': 1, 'cnt': 2
    },
    'main': {
        'cnt': 1, 'cnt': 2
    },
  'main_hosts': {
    'cnt': 1, 'cnt': 2
    },
}
}

print pairs.parseString('a: 2 b: 3\nc: 4 d: "abc def ghi"')
print dictionary.parseString('{ a: 2 b: 3\nc: 4 d: "abc def ghi" } ')
