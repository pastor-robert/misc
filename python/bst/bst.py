class BST(object):
    left = None
    right = None
    def __init__(self, key):
        self._key = key
    @property
    def key(self): return self._key

if __name__=="__main__":
    b = BST(3)
    assert b.key == b._key

