class Atomizer:

	indent = "    "

	str_begin = "'"
	str_end = "'"

	dict_sep = " : "
	dict_begin = "{"
	dict_end = "}"

	list_sep = ", "
	list_begin = "["
	list_end = "]"

	@staticmethod
	def atomize(val, indent_level=1):
		t = type(val)

		# string
		if t==str:
			
			return Atomizer.str_begin + str(val) + Atomizer.str_end

		# basic numeric types
		elif t==int or t==float or t==long:

			return val

		# complex number
		elif t==complex:
			return "(" + str(Atomizer.atomize(val.real)) + "+" + str(Atomizer.atomize(val.imag)) + "J)"

		# list
		elif t==list:
			
			s = Atomizer.list_begin
			l = len(val)

			for i in xrange(l):
				if i<l-1:
					s += str(Atomizer.atomize(val[i])) + Atomizer.list_sep
				else:
					s += str(Atomizer.atomize(val[i]))

			s += Atomizer.list_end

			return s

		# dictionary
		elif t==dict:

			if indent_level > 1:
				s = "\n"
			else:
				s = ""

			for i in range(indent_level-1):
				s += Atomizer.indent
			s += Atomizer.dict_begin
			s += "\n"

			keys = val.keys()
			l = len(keys)

			for i in range(l):

				key = keys[i]

				if i<l-1:
					key_a = str(Atomizer.atomize(key, indent_level+1))
					val_a = str(Atomizer.atomize(val[key], indent_level+1))
					for i in range(indent_level):
						s += Atomizer.indent
					s += key_a + Atomizer.dict_sep + val_a + Atomizer.list_sep + "\n"
				else:
					key_a = str(Atomizer.atomize(key, indent_level+1))
					val_a = str(Atomizer.atomize(val[key], indent_level+1))
					for i in range(indent_level):
						s += Atomizer.indent
					s += key_a + Atomizer.dict_sep + val_a + "\n"

			for i in range(indent_level-1):
				s += Atomizer.indent
			s += Atomizer.dict_end

			return s

		# tuple
		elif t==tuple:

			s = "("
			l = len(val)

			for i in xrange(l):
				if i<l-1:
					s += str(Atomizer.atomize(val[i])) + Atomizer.list_sep
				else:
					s += str(Atomizer.atomize(val[i]))

			s += ")"

			return s

	@staticmethod
	def order_dict(d, *keys): # incomplete

		if type(d)!=dict:
			print "ERROR [Atomizer.order_dict()]: d is not a dictionary"
		else:
			
			if indent_level > 1:
				s = "\n"
			else:
				s = ""

			for i in range(indent_level-1):
				s += "  "
			s += Atomizer.dict_begin
			s += "\n"

			keys = val.keys()
			l = len(keys)

			for i in range(l):

				key = keys[i]

				if i<l-1:
					key_a = Atomizer.atomize(key, indent_level+1)
					val_a = Atomizer.atomize(val[key], indent_level+1)
					for i in range(indent_level):
						s += Atomizer.indent
					s += key_a + Atomizer.dict_sep + val_a + Atomizer.list_sep + "\n"
				else:
					key_a = Atomizer.atomize(key, indent_level+1)
					val_a = Atomizer.atomize(val[key], indent_level+1)
					for i in range(indent_level):
						s += Atomizer.indent
					s += key_a + Atomizer.dict_sep + val_a + "\n"

			for i in range(indent_level-1):
				s += Atomizer.indent
			s += Atomizer.dict_end

			return s


class Parser:

	@staticmethod
	def parse(lines):

		currentObject = None
		objects = []

		for line in lines:

			atom = line.strip()
			
			if atom[0] == Atomizer.dict_begin:
				currentObject = 'dict'
				d = atom[0]

			elif atom[0] == Atomizer.dict_end:
				currentObject = None
				d += atom[0]
				d = eval(d)
				objects.append(d)

			if currentObject=='dict':
				d += line + "\n"
			elif currentObject==None:
				objects.append(eval(line))


	@staticmethod
	def make(*objects):

		str_lines = ""

		for obj in objects:
			print type(obj), obj
			str_lines += str(Atomizer.atomize(obj)) + "\n"

		return str_lines


a = Atomizer.atomize(1)
b = Atomizer.atomize("asg")
c = Atomizer.atomize([1,6,7])
d = {1:3, "asd":93, 64:[1,6]}
d2 = {"monkey":36, "banana":42}
d['hey'] = d2
d3 = {'name':'naveen', 'age':21, 'profession':'student', 'organization':'BITS Pilani'}
e = Atomizer.atomize((8,9,'jhfg'))

D = eval(Atomizer.atomize(d))
L = eval(Atomizer.atomize([1,5,7]))


strlines = Parser.make(a,b,c,d,e)
print "------------------------"
print strlines