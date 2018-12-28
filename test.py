import os
import sys
import random
from bloomy.bloom import * 
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
		line_count = 0
		f = open('./test.data/dict.txt', 'r') 
		for line in f:
			line_count += 1
			line = line.rstrip()
			if b.__contains__(line) == True: collision_count += 1 
			b.add(line) 
			if b.__contains__(line) == False: collision_count += 1
		f.close()
		
		collision_threshold = math.floor(b.calculate_p() * b.n)
		print("COLLISION_THRESHOLD: " + str(collision_threshold) + " in " + str(line_count))
		print("COLLISION_COUNT: " + str(collision_count) + " in " + str(line_count))

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
		b = bloomFilter(100,[lambda e: hash(e) % 100])
		self.assertNotEqual(None, b, 'bloom filter is none')
		self.assertEqual(0, b.bits, 'bit array is not null')
		self.assertEqual(1, b.k)
		self.assertEqual(100, b.m, "size is not 1000")
		b.addHashFunction(lambda e: (hash(e) % 50) + 2)
		self.assertEqual(2, b.k)
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


	def test_bloom_calculate_p(self): 
		b = bloomFilter()
		self.assertEqual(b.calculate_p(), 0)
		self.assertEqual(round(b.calculate_p(5,1000,100),9), 0.009430929)
		self.assertEqual(round(b.calculate_p(10,50000,50000),9), 0.999546093)
		self.assertEqual(round(b.calculate_p(200,1000000000,100),9), 0)
		self.assertEqual(round(b.calculate_p(2,1000000000,500000000),9), 0.399576401)

	def test_bloom_calculate_k(self): 
		b = bloomFilter()
		self.assertEqual(b.calculate_p(), 0)
		self.assertEqual(b.calculate_k(1000000000,500000000),1)
		self.assertEqual(b.calculate_k(1000000000,30000),23105)
		self.assertEqual(b.calculate_k(1000000000,400000),1733)
		
	def test_bloom_mask(self): 
		b = bloomFilter()
		self.assertEqual(b.mask([0,1,2,3]), 15)
		self.assertEqual(b.mask([4]), 16)
		self.assertEqual(b.mask([8]), 256)
	
if __name__ == '__main__':
	unittest.main()