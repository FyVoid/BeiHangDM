import re

def Encode2DiscreteMath(expr: str) -> str:
    expr = expr.replace('~', '┐')
    expr = expr.replace('^', '∧')
    expr = expr.replace('v', '∨')
    expr = expr.replace('@', '⊕')
    expr = expr.replace('->', '→')
    return expr

def Encode2Human(expr: str) -> str:
    expr = expr.replace('┐', '~')
    expr = expr.replace('∧', '^')
    expr = expr.replace('∨', 'v')
    expr = expr.replace('⊕', '@')
    expr = expr.replace('→', '->')
    return expr

def logic_eval(expr: str) -> bool:
    expr = Encode2Human(expr)
    norm_pat = re.compile('(\s*)(.+)->(\s+)(.+)')
    spec_pat = re.compile('(\s*)(\(.+\))->(\s+)(.+)')
    spec_found = re.search(spec_pat, expr)
    if spec_found:
        expr = re.sub(spec_pat, r'\1~\2v\3\4', expr)
    else:
        expr = re.sub(norm_pat, r'\1~\2v\3\4', expr)
    expr = expr.replace('~', 'not ')
    expr = expr.replace('v', 'or')
    expr = expr.replace('^', 'and')
    expr = expr.replace('@', '^')
    return eval(expr)

def truthtable(vars: list):
    pass

def dualformula(expr: str, encode: bool) -> str:
    ret_s = Encode2Human(expr)
    ret_s = s.replace('v', '|')
    ret_s = ret_s.replace('^', 'v')
    ret_s = ret_s.replace('|', '^')
    ret_s = ret_s.replace('0', 'F')
    ret_s = ret_s.replace('1', '0')
    ret_s = ret_s.replace('F', '1')
    if encode:
        ret_s = Encode2DiscreteMath(ret_s)
    return ret_s
