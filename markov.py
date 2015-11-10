import random
import time
import datetime
import os
import numbers

DEBUG = False

if DEBUG:
	FILENAME_PREFIX = '/home/cameron/Projects/python_poetry_generator/texts/'
else:
	FILENAME_PREFIX = '/home/cameron/python_poetry_generator/texts/'

def get_book_text(url):
	count = 0
	req = requests.get(url)
	soup = BeautifulSoup(req.text)
	pars = soup.find.all('p')
	
	with open(str(count) + ".txt", 'w') as f:
		for par in pars:
			f.write(par.string)
			count += 1

def get_urls():
	urls = []
	base_url = 'https://www.gutenberg.org'
	top_100_url = 'https://www.gutenberg.org/browse/scores/top'

	req = requests.get(top_100_url)
	soup = BeautifulSoup(req.text, parse_only=SoupStrainer('a', href=True))
	for link in soup.find_all('a')[19:119]:
		urls.append(base_url + link['href'])

	return urls

def write_file(data, filename):
	with open(filename, 'w') as f:
		f.write(data)

def get_final_urls(urls):
	final_urls = []

	for url in urls:
		time.sleep(5)
		req = requests.get(url)
		soup = BeautifulSoup(req.text, parse_only=SoupStrainer('a', href=True))

		for x in soup:
			if x.string == 'Read this book online: HTML':
				final_urls.append('https:' + x['href'])

	return final_urls


class BlogPost():
	def __init__(self, text):
		self.text = text
		self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
		self.title = self.get_title()

	def get_title(self):
		words = self.text.split(' ')
		return ' '.join(words[:2])

	def write_file(self):
		with open('/home/cameron/Projects/pelicanPoetryBlog/content/' + self.title + '.md', 'w') as f:
			f.write('Title: ' + self.title + '\n' +
					'Date: ' + self.date + '\n' +
					'Category: Poetry \n \n' +
					self.text)

	def write_file2(self):
		with open('/home/cameron/Projects/pelicanPoetryBlog/content/' + self.title + '.md', 'w') as f:
			f.write('Title: ' + self.text + '\n' +
					'Date: ' + self.date + '\n' +
					'Category: Poetry \n \n')


	
# def harvest():
# 	book_urls = get_final_urls(get_urls())
# 	for url in book_urls:
# 		time.sleep(5)
# 		get_book_text(url)

class Markov(object):
	
	def __init__(self, open_file):
		self.cache = {}
		self.words = open_file.split()
		self.word_size = len(self.words)
		self.database()
	
	def triples(self):
		""" Generates triples from the given data string. So if our string were
				"What a lovely day", we'd generate (What, a, lovely) and then
				(a, lovely, day).
		"""
		if len(self.words) < 3:
			return
		
		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])
			
	def database(self):

		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]
				
	def generate_markov_text(self, size=30):
		seed = random.randint(0, self.word_size-3)
		seed_word, next_word = self.words[seed], self.words[seed+1]
		w1, w2 = seed_word, next_word
		gen_words = []

		for i in xrange(size):
			gen_words.append(w1)
			
			w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		gen_words.append(w2)
		self.text = ' '.join(gen_words)
		return self.text

	def format_poem(self):
		# period = False
		puntc = ['.', '?', '!']
		puncts = [',', '-', ';', ':']
		illegal = ['{', '}', '"', '[', ']', '_', ')', '(', '/']
		illegal_words = ['the', 'The', 'and']
	
		# End the poem on the nearest punctuation mark. 
		# If the poem contains none, add a period to the end.
		# for x in reversed(range(len(self.text))):
		# 	if self.text[x] in puntc:
		# 		self.text = self.text[:x+1]
		# 		period = True
		# 		break
		# if not period and len(self.text.split(' ')) != 2:
		# 	self.text = self.text + '.'

		new_poem = ''
		try:
			for x in range(len(self.text)):

				if x == 0:
					new_poem += self.text[x].upper()


				# Remove bad characters and numbers
				elif self.text[x] in illegal or isinstance(self.text[x], numbers.Number):
					pass

				# Capitalize all i pronouns.
				elif len(self.text) > x > 0 and self.text[x-1] == ' ' and self.text[x+1] == ' ' and self.text[x] == 'i':
					new_poem += self.text[x].upper()
					print "OK"

				# Capitalize beginning of new sentences.
				elif len(self.text) > x > 0 and self.text[x-2] in puntc and self.text[x-1] == ' ':
					new_poem += self.text[x].upper()

				else:
					new_poem += self.text[x]

			if new_poem.split()[:-1] in illegal_words:
				new = new_poem.split()
				new_poem = new[:-1]

			# Don't end a poem on incorrect punctuation.
			if new_poem[:-1] in puncts:
				print "KK"
				new_poem = new_poem[:-1]
			if new_poem[:-1] not in puntc:
				new_poem += random.choice(puntc)

			self.text = new_poem
		except:
			self.text = "Sorry...There was an error. Please try again!"



def write(request):
	if not request:
		return "Please select at least one poet!"
	authors = ['Dickinson', 'Whitman', 'Poe', 'Cummings', 'Bukowski', 'Shakespeare']
	combined_text = ''

	for author in authors:
		if request.get(author):
			fname = FILENAME_PREFIX + author + '.txt'
			for line in open(fname):
				combined_text += line
	
	markov = Markov(combined_text)

	combined_text = ''
	markov.generate_markov_text()
	markov.format_poem()
	return markov.text
	








