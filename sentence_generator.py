import markov
import tools
import string
import os

class sentence_generator(markov.markov_chain):
	def __init__(self, path, level=1):
		try:
			words_list = list()
			if not os.path.isdir(path):
				raw_file = open(path)
				raw_txt = raw_file.read()
				raw_file.close()
				words_list = self.__clean_raw_file__(raw_txt).split()
			else:
				for filename in os.listdir(path):
					raw_file = open(os.path.join(path, filename))
					raw_txt = raw_file.read()
					raw_file.close()
					words_list = words_list + self.__clean_raw_file__(raw_txt).split()
			super().__init__(words_list, level)
		except IOError:
			print("IO Error: File " + filename + "does not exist!")


	#cleans up raw file by simplifying text
	#such as removing punctuation, lowercase, etc
	def __clean_raw_file__(self,raw):
		lower_str = raw.lower()
		return tools.strip_punctuation(lower_str)

	#maybe implement a recursive grammar chain
	def generate_sentence(self, length = 10):
		sentence = super().generate_obj_list(length)
		for word in sentence:
			print (word,end=" ")
