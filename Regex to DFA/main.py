import sys
from antlr4 import *
from GrammerLexer import GrammerLexer
from GrammerParser import GrammerParser
from GrammerVisitor import GrammerVisitor
from GrammerVisitorShow import GrammerVisitorShow
from GrammerVisitorPars import GrammerVisitorPars
from typing import List, Tuple, Set, Dict
#import graphviz as graphviz

EPS = "eps"
State = int
Word = str
Configuration = Tuple[State, Word]
Transition = Tuple[State, Word, List[State]]
EPSILON = ""

#returneaza o lista cu toate configuratiile in care se 
#poate ajunge intr-un singur pas
def step( configuration: Configuration) -> List[Configuration]:
		(state,word) = configuration

		lista = []
		for (st,character) in nfa:
			if st == state:
				if word != '' and character == word[0]:
					conf = nfa[(st,character)]
					for c in conf:
						lista.append((c,word[1:]))
				elif character == "":
					conf = nfa[(st,character)]
					for c in conf:
						lista.append((c,word))
		return (lista)

#returneaza o lista cu toate configuratiile in care se poate 
#ajunge in k pasi
def kstep(configuration: Configuration, k: int) -> List[Configuration]:        
		(state,word) = configuration
		lista=step((state,word))
		for i in range(k - 1):
			li = []
			for conf in lista:
				liist = step(conf)
				li.extend(liist)
			lista.clear()
			lista.extend(li)
		return lista

#returneaza un set cu toate starile in care putem ajunge 
#din starea curenta daca ne ducem pe epsilon tranzitii
def epsilonClosure(state: State) -> Set[State]:
	st = {state}
	index = 1
	while True:
		lista = []
		for i in kstep((state,''),index):
			lista.append(i[0])
		if set(lista).issubset(st):
			break
		st = st.union(set(lista))
		index += 1
	return st
#constructie nfa
def construct_dfa(nfa,list_of_epsilon_closure,list_of_finale_states,statess):

	dfa = dict()

	list_of_dfa = []
	list_of_dfa.append(list_of_epsilon_closure[0]) 
	#pentru fiecare stare din lista
	for state in list_of_dfa:
		#pentru fiecare litera din alfabet
		for symbol in alphabet:	
			l = set()
			#pentru fiecare stare din lista adaug in set valorile
			# specifice din nfa
			for s in state:
				if (s,symbol) in nfa:
					l = l.union(nfa[(s,symbol)])
			for i in l:
				l = l.union(list_of_epsilon_closure[i])		
			#daca setul se alfa deja in list_of_dfa adaug in 
			#dfa valoarea specifica
			if list(l) in list_of_dfa:
				dfa[(list_of_dfa.index(list(state)),symbol)] = list_of_dfa.index(list(l))
			#daca setul nu exista adaug noua stare in lista
			#si adaug in dfa valoarea specifica
			else:
				list_of_dfa.append(list(l))
				dfa[(list_of_dfa.index(list(state)),symbol)] = list_of_dfa.index(list(l))
			#daca setul nu exista adaug noua stare in lista
			if list(l) not in list_of_dfa:
				list_of_dfa.append(list(l))
	#creez lista cu starile finale si in statess salvez numarul 
	#acestora
	for lista in list_of_dfa:
		for i in lista:
			if i in finalStates:
				list_of_finale_states.append(list_of_dfa.index(list(lista)))
	statess.append(len(list_of_dfa))
	return dfa
if __name__ == '__main__':

	#citesc expresia din fisier
	file1 = open(sys.argv[1],"r") 
	inpu = file1.read()
	
	#elimin *-ul duplicat verificand pe rand caracterul curent
	# si caracterul gasit anterior
	ch_aux = ""
	new_inp = ''
	for ch in inpu:
		if ch == '*' and ch_aux == '*':
			new_inp += ''
		else:
			new_inp += ch
		ch_aux = ch

	file1.close()

	#suprascriu fisierul initial cu rezultatul meu
	file1 = open(sys.argv[1], 'w') 
	file1.write(new_inp)
	file1.close()

	#trimit ca parametru inputul citit din fisier spre parsare
	inp = FileStream(sys.argv[1])
	lexer = GrammerLexer(inp)
	stream = CommonTokenStream(lexer)
	parser = GrammerParser(stream)
	tree = parser.expr()

	pars = GrammerVisitorPars()
	#rezultatul ontinut este transformarea expresiei intr-un nfa
	nfa = pars.visit(tree)

	#afisare nfa
	file1 = open(sys.argv[2],"w") 
	file1.write(str(nfa.no_stari) +"\n" )
	file1.write(str(nfa.stari_finale) +"\n" )
	final_NFA = list()
	char = ''
	state = -1
	for(stare,tranz,final) in nfa.lista:
		if (char != tranz or state!= stare	 ):
				final_NFA.append((stare,tranz,[final]))
				char = tranz
				state = stare	
		else:
			(a,c,b)= final_NFA[len(final_NFA) -  1] 
			b.append(final)
			final_NFA[len(final_NFA) -  1] = (stare,tranz,b)
	print(final_NFA	)
	for(stare,tranz,final) in final_NFA	:
		file1.write(str(stare) +" "+ str(tranz) + " ")
		for s in final:
			file1.write(str(s) + " ")
		file1.write("\n")



	file1.close()	




	#transformare nfa in dfa cu ajutorul temei 2
	lista = []
	write_file = sys.argv[3]

	#citire din fisier
	with open(sys.argv[2]) as file:
		numberOfStates = int(file.readline().rstrip())
		finalStates = set(map(int, file.readline().rstrip().split(" ")))
		nfa = dict()
		alphabet = []
		while True:
			transition = file.readline().rstrip().split(" ")
			if transition == ['']:
				break
			if transition[1] == "eps":
				transition[1] = EPSILON
			elif transition[1] not in alphabet:
				alphabet.append(transition[1])

			nfa[(int(transition[0]), transition[1])] = set(map(int, transition[2:]))

	#creez un dictionar in care cheile sunt starile iar 
	#inchiderile epsilon valorile
	list_of_epsilon_closure = dict()
	for i in range(numberOfStates):
		list_of_epsilon_closure[i] = list(epsilonClosure(i))

	#apelez functia de creare a dfa-ului
	dfa = dict()
	list_of_finale_states = []
	statess = []
	dfa = construct_dfa(nfa,list_of_epsilon_closure,list_of_finale_states,statess)

	#scrierea in fisier
	wr = open(write_file,"w")
	wr.write(str(statess[0]))
	wr.write("\n")
	for i in list_of_finale_states:
		wr.write(str(i) + ' ')
	wr.write("\n")

	for (state,symbol) in dfa:
		wr.write(str(state) + ' ' + symbol + ' ' + str(dfa[(state,symbol)]))
		wr.write("\n")