import re

def logic_eval(expr: str) -> bool:
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

def dualformula(s: str) -> str:
    ret_s = s.replace('v', '|')
    ret_s = ret_s.replace('^', 'v')
    ret_s = ret_s.replace('|', '^')
    ret_s = ret_s.replace('0', 'F')
    ret_s = ret_s.replace('1', '0')
    ret_s = ret_s.replace('F', '1')
    return ret_s


print(logic_eval('(1 @ 0) -> 1'))