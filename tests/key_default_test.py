# This import fixes sys.path issues
import bootstrap
import unittest
from datawrap.keydefaultdict import KeyDefaultDict

class KeyDefaultDictTest(unittest.TestCase):
    '''
    Performs basic KeyDefaultDict tests where the default function
    takes the key as an argument to generate new values.
    '''
    def test_key_defaults(self):
        inputs = { k : k*2 for k in range(100)}
        for k in inputs.keys():
            inputs[str(k)] = str(k*2)
        
        repeatkey = KeyDefaultDict(lambda k: k)
        for k in inputs:
            self.assertEquals(repeatkey[k], k)
        
        # Reset
        repeatkey = KeyDefaultDict(lambda k: k)
        for k,v in inputs.iteritems():
            repeatkey[k] = v
            
        for k in inputs:
            if isinstance(k, basestring):
                self.assertEquals(repeatkey[k], str(int(k)*2))
            else:
                self.assertEquals(repeatkey[k], k*2)
                
        for k in range(-200, 0)+range(1000, 2000):
            self.assertEquals(repeatkey[k], k)

if __name__ == "__main__":
    unittest.main()
