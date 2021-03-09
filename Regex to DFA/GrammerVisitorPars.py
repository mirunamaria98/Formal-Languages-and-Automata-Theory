# Generated from Grammer.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
	from .GrammerParser import GrammerParser
else:
	from GrammerParser import GrammerParser
from GrammerVisitor import GrammerVisitor
from GrammerVisitor import NFA
# This class defines a complete generic visitor for a parse tree produced by GrammerParser.
EPS = "eps"
class GrammerVisitorPars(GrammerVisitor):

	#OR
	# Visit a parse tree produced by GrammerParser#expr.
	def visitExpr(self, ctx:GrammerParser.ExprContext):
		e = ctx.expr()
		m = ctx.m_expr()


		if e:
			v1 = self.visit(e)
			v2 = self.visit(m)
			return union(v1,v2)
		else:
			return self.visit(m)

	#AND
	# Visit a parse tree produced by GrammerParser#m_expr.
	def visitM_expr(self, ctx:GrammerParser.M_exprContext):
		m = ctx.m_expr()
		a = ctx.a_expr()

		if m:
			v1 = self.visit(m)
			v2 = self.visit(a)
			return concatenation(v1,v2)
		else:
			return self.visit(a)

	#STAR
	# Visit a parse tree produced by GrammerParser#a_expr.
	def visitA_expr(self, ctx:GrammerParser.A_exprContext):
		a = ctx.a_expr()
		b = ctx.b_expr()

		if a:
			v1 = self.visit(a)
			return star(v1)
		else:
			return self.visit(b)


	# Visit a parse tree produced by GrammerParser#b_expr.
	def visitB_expr(self, ctx:GrammerParser.B_exprContext):
		a = ctx.inner_expr()
		b = ctx.variabila()

		if a:
			return self.visit(a)
		else:
			return self.visit(b)

	#VAR
	# Visit a parse tree produced by GrammerParser#variabila.
	def visitVariabila(self, ctx:GrammerParser.VariabilaContext):
		#cazul de baza
		a = str(ctx.VAR())
		dictionar = list()
		dictionar = [(0,a,1)]

		return NFA(dictionar,1,2)

	#INNER_EXPR
	# Visit a parse tree produced by GrammerParser#inner_expr.
	def visitInner_expr(self, ctx:GrammerParser.Inner_exprContext):
		
		return self.visit(ctx.expr())

del GrammerParser

def union(expr1,expr2):
	dictionar_aux = list()
	#parcurg listele pentru cele doua expresii primite
	#si construiesc o noua lista cu reuniunea celor doua
	#imaginea 2 din arhiva
	for(stare,tranz,final) in expr2.lista:
			dictionar_aux.append((stare + 1,tranz,final + 1))

	dictionar_aux2 = list()
	trans_nfa1 = expr2.no_stari
	for(stare,tranz,final) in expr1.lista:
			dictionar_aux2.append((stare + trans_nfa1 + 1,tranz,final + trans_nfa1 + 1))


	dictionar_aux.insert(0,(0,EPS,1))
	dictionar_aux.insert(1,(0,EPS,trans_nfa1 + 1))
	dictionar_aux.append((trans_nfa1,EPS,trans_nfa1 + expr1.no_stari + 1))
	dictionar_aux += dictionar_aux2
	dictionar_aux.append((trans_nfa1 + expr1.no_stari,EPS,trans_nfa1 + expr1.no_stari + 1))
	return NFA(dictionar_aux,trans_nfa1 + expr1.no_stari + 1,trans_nfa1 + expr1.no_stari + 2)

def concatenation(expr1,expr2):

	#parcurg cele doua liste primite si construiesc noua lista
	#in functie de imaginea 1 din arhiva 
	expr_aux = expr2.lista
	dictionar_aux2 = list()
	trans_nfa2 = expr2.no_stari
	for(stare,tranz,final) in expr1.lista:
			dictionar_aux2.append((stare + trans_nfa2 - 1,tranz,final + trans_nfa2 - 1))
	
	expr_aux += dictionar_aux2
	return NFA(expr_aux,trans_nfa2 + expr1.no_stari - 2,trans_nfa2 + expr1.no_stari - 1)


def star(expr1):
	#construiesc noua lista 
	#imaginea 3 din arhiva
	lista_aux = list()
	for(stare,tranz,final) in expr1.lista:
		lista_aux.append((stare + 1, tranz, final + 1))
	lista_aux.insert(0,(0,EPS,1))
	lista_aux.insert(1,(0,EPS,expr1.no_stari + 1))
	lista_aux.append((expr1.no_stari, EPS,1))
	lista_aux.append((expr1.no_stari,EPS,expr1.no_stari + 1))

	return(NFA(lista_aux,expr1.no_stari + 1, expr1.no_stari + 2))

