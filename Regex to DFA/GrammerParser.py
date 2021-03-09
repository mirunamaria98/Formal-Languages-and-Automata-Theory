# Generated from Grammer.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\3\2\3\2\3\2\3\2\3\2\5\2\26\n\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3\34\n\3\3\4\3\4\3\4\3\4\3\4\7\4#\n\4\f\4\16\4&\13")
        buf.write("\4\3\5\3\5\5\5*\n\5\3\6\3\6\5\6.\n\6\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\2\3\6\t\2\4\6\b\n\f\16\2\2\2\63\2\25\3\2\2")
        buf.write("\2\4\33\3\2\2\2\6\35\3\2\2\2\b)\3\2\2\2\n-\3\2\2\2\f/")
        buf.write("\3\2\2\2\16\61\3\2\2\2\20\21\5\4\3\2\21\22\7\3\2\2\22")
        buf.write("\23\5\2\2\2\23\26\3\2\2\2\24\26\5\4\3\2\25\20\3\2\2\2")
        buf.write("\25\24\3\2\2\2\26\3\3\2\2\2\27\30\5\6\4\2\30\31\5\4\3")
        buf.write("\2\31\34\3\2\2\2\32\34\5\6\4\2\33\27\3\2\2\2\33\32\3\2")
        buf.write("\2\2\34\5\3\2\2\2\35\36\b\4\1\2\36\37\5\b\5\2\37$\3\2")
        buf.write("\2\2 !\f\4\2\2!#\7\6\2\2\" \3\2\2\2#&\3\2\2\2$\"\3\2\2")
        buf.write("\2$%\3\2\2\2%\7\3\2\2\2&$\3\2\2\2\'*\5\16\b\2(*\5\f\7")
        buf.write("\2)\'\3\2\2\2)(\3\2\2\2*\t\3\2\2\2+.\5\f\7\2,.\5\16\b")
        buf.write("\2-+\3\2\2\2-,\3\2\2\2.\13\3\2\2\2/\60\7\b\2\2\60\r\3")
        buf.write("\2\2\2\61\62\7\4\2\2\62\63\5\2\2\2\63\64\7\5\2\2\64\17")
        buf.write("\3\2\2\2\7\25\33$)-")
        return buf.getvalue()


class GrammerParser ( Parser ):

    grammarFileName = "Grammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'('", "')'", "'*'" ]

    symbolicNames = [ "<INVALID>", "REUNIUNE", "OPEN", "CLOSED", "STAR", 
                      "WHITESPACE", "VAR" ]

    RULE_expr = 0
    RULE_m_expr = 1
    RULE_a_expr = 2
    RULE_b_expr = 3
    RULE_atom = 4
    RULE_variabila = 5
    RULE_inner_expr = 6

    ruleNames =  [ "expr", "m_expr", "a_expr", "b_expr", "atom", "variabila", 
                   "inner_expr" ]

    EOF = Token.EOF
    REUNIUNE=1
    OPEN=2
    CLOSED=3
    STAR=4
    WHITESPACE=5
    VAR=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def m_expr(self):
            return self.getTypedRuleContext(GrammerParser.M_exprContext,0)


        def REUNIUNE(self):
            return self.getToken(GrammerParser.REUNIUNE, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammerParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammerParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = GrammerParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.m_expr()
                self.state = 15
                self.match(GrammerParser.REUNIUNE)
                self.state = 16
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.m_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class M_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a_expr(self):
            return self.getTypedRuleContext(GrammerParser.A_exprContext,0)


        def m_expr(self):
            return self.getTypedRuleContext(GrammerParser.M_exprContext,0)


        def getRuleIndex(self):
            return GrammerParser.RULE_m_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitM_expr" ):
                return visitor.visitM_expr(self)
            else:
                return visitor.visitChildren(self)




    def m_expr(self):

        localctx = GrammerParser.M_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_m_expr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.a_expr(0)
                self.state = 22
                self.m_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.a_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class A_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def b_expr(self):
            return self.getTypedRuleContext(GrammerParser.B_exprContext,0)


        def a_expr(self):
            return self.getTypedRuleContext(GrammerParser.A_exprContext,0)


        def STAR(self):
            return self.getToken(GrammerParser.STAR, 0)

        def getRuleIndex(self):
            return GrammerParser.RULE_a_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_expr" ):
                return visitor.visitA_expr(self)
            else:
                return visitor.visitChildren(self)



    def a_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammerParser.A_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_a_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.b_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammerParser.A_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                    self.state = 30
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 31
                    self.match(GrammerParser.STAR) 
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class B_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inner_expr(self):
            return self.getTypedRuleContext(GrammerParser.Inner_exprContext,0)


        def variabila(self):
            return self.getTypedRuleContext(GrammerParser.VariabilaContext,0)


        def getRuleIndex(self):
            return GrammerParser.RULE_b_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitB_expr" ):
                return visitor.visitB_expr(self)
            else:
                return visitor.visitChildren(self)




    def b_expr(self):

        localctx = GrammerParser.B_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_b_expr)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammerParser.OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.inner_expr()
                pass
            elif token in [GrammerParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.variabila()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variabila(self):
            return self.getTypedRuleContext(GrammerParser.VariabilaContext,0)


        def inner_expr(self):
            return self.getTypedRuleContext(GrammerParser.Inner_exprContext,0)


        def getRuleIndex(self):
            return GrammerParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = GrammerParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammerParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.variabila()
                pass
            elif token in [GrammerParser.OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.inner_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariabilaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GrammerParser.VAR, 0)

        def getRuleIndex(self):
            return GrammerParser.RULE_variabila

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariabila" ):
                return visitor.visitVariabila(self)
            else:
                return visitor.visitChildren(self)




    def variabila(self):

        localctx = GrammerParser.VariabilaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variabila)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(GrammerParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inner_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(GrammerParser.OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammerParser.ExprContext,0)


        def CLOSED(self):
            return self.getToken(GrammerParser.CLOSED, 0)

        def getRuleIndex(self):
            return GrammerParser.RULE_inner_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInner_expr" ):
                return visitor.visitInner_expr(self)
            else:
                return visitor.visitChildren(self)




    def inner_expr(self):

        localctx = GrammerParser.Inner_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_inner_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(GrammerParser.OPEN)
            self.state = 48
            self.expr()
            self.state = 49
            self.match(GrammerParser.CLOSED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.a_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def a_expr_sempred(self, localctx:A_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




