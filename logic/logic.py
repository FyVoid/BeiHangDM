import re
import collections
from collections import OrderedDict

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

def logic_eval(expr: str, vars={}) -> int:
    for var, value in vars.items():
        expr = expr.replace(var, value)
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
    ret_value = eval(expr)
    ret_value = int(ret_value)
    return ret_value

def _truthtable(vars: list, output_dict: OrderedDict, expr: str):
    truth_value = ["1", "0"]
    if len(vars) == 0:
        for key, val in output_dict.items():
            print(val, end=" ")
        print(logic_eval(expr, output_dict))
    else:
        for truth in truth_value:
            var = vars.pop(0)
            output_dict[var] = truth
            _truthtable(vars, output_dict, expr)
            vars.insert(0, var)
        #output_dict.pop(var)


def truthtable(vars: list, expr: str):
    output_dict = OrderedDict()
    for var in vars:
        print(var, end=" ")
    print(expr)
    _truthtable(vars, output_dict, expr)


def dualformula(expr: str, encode: bool) -> str:
    ret_s = Encode2Human(expr)
    ret_s = ret_s.replace('v', '|')
    ret_s = ret_s.replace('^', 'v')
    ret_s = ret_s.replace('|', '^')
    ret_s = ret_s.replace('0', 'F')
    ret_s = ret_s.replace('1', '0')
    ret_s = ret_s.replace('F', '1')
    if encode:
        ret_s = Encode2DiscreteMath(ret_s)
    return ret_s
