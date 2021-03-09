#STOIAN MIRUNA MARIA
#335CB
import sys

#Functia ce imi creeaza matricea delta
def delta(string1):
	matrix = [[]] 

	alphabet = [" "]
	alphabet += [chr(i) for i in range(ord('A'),ord('Z')+1)]

	state_of_empty_list = ["e"]
	state_of_empty_list += 26 * [0]


	matrix = [alphabet,state_of_empty_list]

	word = ""
	for i in range(len(string1)):
		word += string1[i]
		states = [word]
		states += 26 * [0]
		matrix += [states]
	return matrix

#functia ce imi populeaza matricea delta
#cu valori diferite de 0 pe pozitiile necesare
def populate_matrix(delta,string1):

	#pentru primul caracter din substring adaug in matrice
	#valoarea 1 pe pozitiile necesare
	for i in range(len(delta)):
		for j in range(len(delta[i])):
			if string1[0] == delta[0][j]:
				delta[1][j] = 1

	#adaug pe rand litere la cuvantul meu
	#daca acestea se potrivesc voi aduga in matrice starea in care se trece
	#daca nu se gaseste nicio potrivire atunci verific toate sufixele cuvantului
	#daca sufixul gasit se potriveste opresc cautarea 
	for i in range(2,len(delta)):
		create_word = delta[i][0]
		for j in range(1,len(delta[i])):
			create_word += delta[0][j]
			create_word_aux = create_word
			ok = 0
			for l in range(len(create_word)):
				for k in range(2,len(delta)):
					if create_word_aux == delta[k][0]:
						delta[i][j] = len(create_word_aux)
						ok = 1
						break
				if ok == 1:
					break
				#elimin prima litera din cuvant pentru a forma cuvantul
				create_word_aux = create_word_aux[-(len(create_word_aux) - 1 ):]

			#elimin ultima litera din cuvant 
			create_word = create_word[:-1]

	return delta


if __name__ == '__main__':

	#citesc argumentele
	read_file = sys.argv[1]
	write_file = sys.argv[2]

	#deschid fisierele
	file = open(read_file)
	file1 = open(write_file,'w')

	#citesc cele dous stringuri din fisier
	string1 = file.readline()
	string2 = file.readline()

	#creez matricea delta
	delta = delta(string1)

	#populez matricea delta cu stari
	delta = populate_matrix(delta,string1)

	#pentru a printa pozitiile la care se gasesc substringurile
	#am preluat algoritmul prezentat la curs
	q = 1
	for i in range(0,len(string2[:-1])):
		var = int(ord(string2[i]) - 64)
		q = delta[q + 1][var]
		if q == len(string1[:-1]):
			string1_start_position = i - (len(string1[:-1]) - 1)	
			file1.write(str(string1_start_position) + " ")

	file1.write("\n")

	file.close()
	file1.close()

