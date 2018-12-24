import os
import sys
import random
from adt.bloom import * 
import unittest


"""
Unit test class to measure the rate of collisions in the default parameters of the bloom filter
"""
class MeasureCollision(unittest.TestCase):
	
	"""
	Measuring preemptive false positves on  a m = 1,000,000, 
	k = 10 filter against 58,000 uniqie strings 
	"""
	def test_dictionary_collision(self):
		
		b = bloomFilter()
		collision_count = 0; 
		f = open('./test.data/dict.txt', 'r') 
		for line in f:
			line = line.rstrip()
			if b.__contains__(line) == True: collision_count += 1 
			b.add(line) 
			if b.__contains__(line) == False: collision_count += 1
		f.close()
		
		collision_threshold = math.floor(b.calculate_p() * b.n)
		print("COLLISION_THRESHOLD: " + str(collision_threshold))

		self.assertLess(collision_count,collision_threshold, 'collision count has reached beyond the threshold')
		
"""
This is the unit testing class to test the functionality of the bloom filter
module. This measures for regression and ensures working functionality. 	
"""		
class bloomFilterTest(unittest.TestCase):	
	
	def test_bloom_init_default(self): 
		b = bloomFilter()
		self.assertNotEqual(None, b, 'bloom filter is none')
		self.assertEqual(0, b.bits, 'bit array is not null')
		self.assertEqual(1000000, b.m, "size is not 1000")
		self.assertEqual(10, b.k)	
		for f in b.hashFunctions: 
			self.assertTrue(callable(f), "b.hashFunction cont. non function ")	
			
	def test_bloom_init_param(self): 
		b = bloomFilter(100,[lambda e,size: hash(e) % size])
		self.assertNotEqual(None, b, 'bloom filter is none')
		self.assertEqual(0, b.bits, 'bit array is not null')
		self.assertEqual(1, b.k)
		self.assertEqual(100, b.m, "size is not 1000")
		for f in b.hashFunctions: 
			self.assertTrue(callable(f), "b.hashFunction cont. non function ")
		b.add("j")
		self.assertNotEqual(0, b.bits)
		
	def test_bloom_contians(self): 
		b = bloomFilter()
		self.assertNotEqual(None, b, 'bloom filter is none')
		self.assertFalse(b.__contains__("apple"))
		self.assertFalse(b.__contains__("bee"))
		self.assertFalse(b.__contains__("cucumber"))
		b.add("apple")
		b.add("bee")
		b.add("cucumber")
		self.assertTrue(b.__contains__("apple"))
		self.assertTrue(b.__contains__("bee"))
		self.assertTrue(b.__contains__("cucumber"))
		
		fingerprint1 = b.fingerprint("apple")
		self.assertEqual(fingerprint1, b.fingerprint("apple"))

	def test_bloom_add(self):
		b1 = bloomFilter()
		b2 = bloomFilter()
		self.assertEqual(0, b1.bits, 'bit array is not null')
		self.assertEqual(0, b2.bits, 'bit array is not null')
		
		b1.add("abcdefghijklmnopqrstuvwxyz")
		b2.add("abcdefghijklmnopqrstuvwxyz")
		self.assertEqual(b1.bits, b2.bits)
		self.assertTrue(b1.__contains__("abcdefghijklmnopqrstuvwxyz"))
		self.assertTrue(b2.__contains__("abcdefghijklmnopqrstuvwxyz"))





	
	
if __name__ == '__main__':
	unittest.main()