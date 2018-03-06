def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency
def read_words(filename):
    return open(filename).read().split()
def main(filename):
	list1=[]
	list2=[]
	ls=[]
	frequency=word_frequency(read_words(filename))
	for word,count in frequency.items():
		ls = [(k,v) for (k,v) in frequency.items()]
	ls.sort(key=lambda x:x[1],reverse=True)
	for k,v in ls:
	 print k, v
	 print list2
main("a.txt")