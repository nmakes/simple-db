'''
	Copyright (c) 2017 Naveen Venkat
	nav.naveenvenkat@gmail.com
	https://github.com/nmakes/simple-db
'''

class Beautifier:

	indent = "    "

	str_begin = "'"
	str_end = "'"

	dict_sep = " : "
	dict_begin = "{"
	dict_end = "}"

	list_sep = ", "
	list_begin = "["
	list_end = "]"

	tuple_begin = "("
	tuple_end = ")"

	@staticmethod
	def beautify(val, indent_level=1):
		t = type(val)

		# string
		if t==str:
			
			return Beautifier.str_begin + str(val) + Beautifier.str_end

		# basic numeric types
		elif t==int or t==float or t==long:

			return str(val)

		# complex number
		elif t==complex:
			return "(" + str(Beautifier.beautify(val.real)) + "+" + str(Beautifier.beautify(val.imag)) + "J)"

		# list
		elif t==list:
			
			s = Beautifier.list_begin
			l = len(val)

			for i in xrange(l):
				if i<l-1:
					s += str(Beautifier.beautify(val[i])) + Beautifier.list_sep
				else:
					s += str(Beautifier.beautify(val[i]))

			s += Beautifier.list_end

			return s

		# dictionary
		elif t==dict:

			if indent_level > 1:
				s = "\n"
			else:
				s = ""

			for i in range(indent_level-1):
				s += Beautifier.indent
			s += Beautifier.dict_begin
			s += "\n"

			keys = val.keys()
			l = len(keys)

			for i in range(l):

				key = keys[i]

				if i<l-1:
					key_a = str(Beautifier.beautify(key, indent_level+1))
					val_a = str(Beautifier.beautify(val[key], indent_level+1))
					for i in range(indent_level):
						s += Beautifier.indent
					s += key_a + Beautifier.dict_sep + val_a + Beautifier.list_sep + "\n"
				else:
					key_a = str(Beautifier.beautify(key, indent_level+1))
					val_a = str(Beautifier.beautify(val[key], indent_level+1))
					for i in range(indent_level):
						s += Beautifier.indent
					s += key_a + Beautifier.dict_sep + val_a + "\n"

			for i in range(indent_level-1):
				s += Beautifier.indent
			s += Beautifier.dict_end

			return s

		# tuple
		elif t==tuple:

			s = "("
			l = len(val)

			for i in xrange(l):
				if i<l-1:
					s += str(Beautifier.beautify(val[i])) + Beautifier.list_sep
				else:
					s += str(Beautifier.beautify(val[i]))

			s += ")"

			return s


	@staticmethod
	def removeEmptyLines(Lines):

		lines = list(Lines)

		for line in lines:
			if line=='\n' or line=='':
				lines.remove(line)

		return lines

	@staticmethod
	def readFile(file_object):

		lines = list(file_object.readlines())
		lines = Beautifier.removeEmptyLines(lines)

		file_string = ""

		for line in lines:
			file_string += str(line)

		return file_string

	@staticmethod
	def load(file_object):
		return eval(Beautifier.readFile(file_object))

	@staticmethod
	def dump(obj, file_object):
		bObj = Beautifier.beautify(obj)
		file_object.write(bObj)


a = Beautifier.beautify(1)
b = Beautifier.beautify("asg")
c = Beautifier.beautify([1,6,7])
d = Beautifier.beautify({1:3, "asd":93, 64:[1,6]})
d2 = {"monkey":36, "banana":42}
d3 = {'name':'naveen', 'age':21, 'profession':'student', 'organization':'BITS Pilani'}
e = Beautifier.beautify((8+9J))
f = Beautifier.beautify((1,5,76))

L = eval(Beautifier.beautify([1,5,7]))

parsedObjects = [a,b,c,d,e,f]

A = {'age': 27,
 'name': 'Joe',
 'numbers': [1,
             2, 
             3,
             4,
             5],
 'subdict': {
             'first': 1, 
             'second': 2,
             'd': {1:3, "asd":93, 64:[1,6]},
              'third': 3
             }
}

# fil = open("demo.sdb", 'w+')
# Beautifier.write(A, fil)
# fil.close()

sdb = Beautifier.load(open("demo.sdb"))
print sdb
print type(sdb)

Beautifier.dump(sdb, open("demo2.sdb",'w'))