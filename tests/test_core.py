import unittest
from systemwatch import diff
class Tests(unittest.TestCase):
 def test_diff(self): self.assertEqual(diff({'a':1,'b':2},{'a':3,'c':4}),{'added':['c'],'removed':['b'],'changed':['a']})
if __name__=='__main__': unittest.main()
