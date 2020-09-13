
import unittest
import prime

class testPrime(unittest.TestCase):
    def testSinglePrime(self):
        a = 3
        result = prime.is_prime(a)
        self.assertEquals(result, "Prime")
        
    def testingDoublePrime(self):
        b = 11 
        result = prime.is_prime(b)
        self.assertEquals(result, "Prime")

if __name__ == "__main__":
    unittest.main()
