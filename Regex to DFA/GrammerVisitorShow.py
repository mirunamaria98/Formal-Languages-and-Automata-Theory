# Generated from Grammer.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammerParser import GrammerParser
else:
    from GrammerParser import GrammerParser
from GrammerVisitor import GrammerVisitor
# This class defines a complete generic visitor for a parse tree produced by GrammerParser.

class GrammerVisitorShow(GrammerVisitor):

    # Visit a parse tree produced by GrammerParser#expr.
    def visitExpr(self, ctx:GrammerParser.ExprContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#m_expr.
    def visitM_expr(self, ctx:GrammerParser.M_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#a_expr.
    def visitA_expr(self, ctx:GrammerParser.A_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#b_expr.
    def visitB_expr(self, ctx:GrammerParser.B_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#atom.
    def visitAtom(self, ctx:GrammerParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#variabila.
    def visitVariabila(self, ctx:GrammerParser.VariabilaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#inner_expr.
    def visitInner_expr(self, ctx:GrammerParser.Inner_exprContext):
        return self.visitChildren(ctx)



del GrammerParser