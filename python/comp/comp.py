def composition(seq):
    seq = tuple(seq)
    for i in range(int(2**(len(seq)-1))):
        result = [[seq[0]]]
        for j in range(len(seq)-1):
            if i & (1<<j):
                result.append([seq[j+1]])
            else:
                result[-1].append(seq[j+1])
        yield result

if __name__=="__main__":
    from pprint import pprint 
    pprint(list(composition('ABCD')))
    pprint(list(composition('A')))
    pprint(list(composition('')))


