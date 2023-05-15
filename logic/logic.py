import re
import collections
from collections import OrderedDict

def Encode2DiscreteMath(expr: str) -> str:
    expr = expr.replace('~', '┐')
    expr = expr.replace('^', '∧')
    expr = expr.replace('v', '∨')
    expr = expr.replace('@', '⊕')
    expr = expr.replace('<->', '⇔')
    expr = expr.replace('->', '→')
    return expr


def Encode2Human(expr: str) -> str:
    expr = expr.replace('┐', '~')
    expr = expr.replace('∧', '^')
    expr = expr.replace('∨', 'v')
    expr = expr.replace('⊕', '@')
    expr = expr.replace('⇔', '<->')
    expr = expr.replace('→', '->')
    return expr


def logic_eval(expr: str, vars={}) -> int:
    for var, value in vars.items():
        expr = expr.replace(var, value)
    expr = Encode2Human(expr)
    norm_pat = re.compile('(.*)([10]\s*)<->(.+)')
    spec_pat = re.compile('(\s*)(\(.+\)\s*)<->(.+)')
    spec_found = re.search(spec_pat, expr)
    while re.search(norm_pat, expr) or spec_found:
        if spec_found:
            expr = re.sub(spec_pat, r'\1 (\2 -> \3) ^ (\3 -> \2)', expr)
        else:
            expr = re.sub(norm_pat, r'\1 (\2 -> \3) ^ (\3 -> \2)', expr)
        spec_found = re.search(spec_pat, expr)
    print(expr)

    norm_pat = re.compile('(.*)([10]\s*)->(.+)')
    spec_pat = re.compile('(\s*)(\(.+\)\s*)->(.+)')
    spec_found = re.search(spec_pat, expr)
    while re.search(norm_pat, expr) or spec_found:
        if spec_found:
            expr = re.sub(spec_pat, r'\1~\2v\3', expr)
        else:
            expr = re.sub(norm_pat, r'\1~\2v\3', expr)
        spec_found = re.search(spec_pat, expr)
    expr = expr.replace('~', 'not ')
    expr = expr.replace('v', 'or')
    expr = expr.replace('^', 'and')
    expr = expr.replace('@', '^')
    ret_value = eval(expr)
    ret_value = int(ret_value)
    return ret_value


def _ttrec(vars: list, output_dict: OrderedDict, expr: str):
    truth_value = ["1", "0"]
    if len(vars) == 0:
        indent = ' ' * (len(expr) // 2)
        for key, val in output_dict.items():
            print(val, end=" ")
        print(indent, end="")
        print(logic_eval(expr, output_dict))
    else:
        for truth in truth_value:
            var = vars.pop(0)
            output_dict[var] = truth
            _ttrec(vars, output_dict, expr)
            vars.insert(0, var)
def truthtable(vars: list, expr: str):
    output_dict = OrderedDict()
    expr = Encode2DiscreteMath(expr)
    for var in vars:
        print(var, end=" ")
    print(expr)
    expr = Encode2Human(expr)
    _ttrec(vars, output_dict, expr)


def _iarec(vars: list, pre: list, output_dict: OrderedDict, expr: str, final: str):
    truth_value = ["1", "0"]
    if len(vars) == 0:
        for key, val in output_dict.items():
            print(val, end=" ")
        val_conditions = 1
        for condition in pre:
            val_condition = logic_eval(condition, output_dict)
            if(val_condition == 0):
                val_conditions = 0
            indent = ' ' * (len(condition) // 2)
            print(indent, end='')
            print(val_condition, end='   ')
        val_expr = logic_eval(expr, output_dict)
        indent = ' ' * (len(expr) // 2 + 1)
        print(indent, end="")
        print(val_expr, end=' ')
        indent = ' ' * (len(final) // 2 + 1)
        print(indent, end='')
        if (val_conditions == 0) and (val_expr == 1):
            print("0")
        else:
            print('1')
    else:
        for truth in truth_value:
            var = vars.pop(0)
            output_dict[var] = truth
            _iarec(vars, pre, output_dict, expr, final)
            vars.insert(0, var)
def isargument(vars: list, pre: list, expr: str):
    output_dict = OrderedDict()
    for expression in pre:
        expression = Encode2DiscreteMath(expression)
    expr = Encode2DiscreteMath(expr)
    final = ''
    for var in vars:
        print(var, end=' ')
    for i in range(len(pre)):
        print(pre[i], end=' ')
        final = final + pre[i]
        if i != len(pre) - 1:
            final = final + ', '
    print(expr, end=' ')
    final = final + ' ╞ ' + expr
    print(final)
    for expression in pre:
        expression = Encode2Human(expression)
    expr = Encode2Human(expr)
    _iarec(vars, pre, output_dict, expr, final)


def _ierec(vars: list, pre: list, output_dict: OrderedDict, expr: str, final: str):
    truth_value = ["1", "0"]
    if len(vars) == 0:
        for key, val in output_dict.items():
            print(val, end=" ")
        val_conditions = 1
        for condition in pre:
            val_condition = logic_eval(condition, output_dict)
            if(val_condition == 0):
                val_conditions = 0
            indent = ' ' * (len(condition) // 2)
            print(indent, end='')
            print(val_condition, end='   ')
        val_expr = logic_eval(expr, output_dict)
        indent = ' ' * (len(expr) // 2 + 1)
        print(indent, end="")
        print(val_expr, end=' ')
        indent = ' ' * (len(final) // 2 + 1)
        print(indent, end='')
        if val_conditions == val_expr:
            print("1")
        else:
            print('0')
    else:
        for truth in truth_value:
            var = vars.pop(0)
            output_dict[var] = truth
            _ierec(vars, pre, output_dict, expr, final)
            vars.insert(0, var)
def isequation(vars: list, pre: list, expr: str):
    output_dict = OrderedDict()
    for expression in pre:
        expression = Encode2DiscreteMath(expression)
    expr = Encode2DiscreteMath(expr)
    final = ''
    for var in vars:
        print(var, end=' ')
    for i in range(len(pre)):
        print(pre[i], end=' ')
        final = final + pre[i]
        if i != len(pre) - 1:
            final = final + ', '
    print(expr, end=' ')
    final = final + ' ⇔ ' + expr
    print(final)
    for expression in pre:
        expression = Encode2Human(expression)
    expr = Encode2Human(expr)
    _ierec(vars, pre, output_dict, expr, final)


def dualformula(expr: str, encode: bool = False) -> str:
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

def _strec(vars: list, output_dict: OrderedDict, parent: str, sub: str):
    truth_value = ['1', '0']
    if len(vars) == 0:
        indent = ' ' * (len(parent) // 2)
        for key, val in output_dict.items():
            print(val, end=' ')
        print(indent, end=" ")
        pval = logic_eval(parent, output_dict)
        sval = logic_eval(sub, output_dict)
        print(pval, end=" ")
        indent = ' ' * ((len(sub) // 2) + 4)
        print(indent, end=" ")
        print(sval, end=" ")
        indent = ' ' * ((len("equality") // 2) + 4)
        print(indent, end=" ")
        print(int(pval == sval))
    else:
        for truth in truth_value:
            var = vars.pop(0)
            output_dict[var] = truth
            _strec(vars, output_dict, parent, sub)
            vars.insert(0, var)

def substitution(parent: str, sub: str, vars: list, expr: str):
    output_dict = OrderedDict()
    expr = Encode2DiscreteMath(expr)
    parent = Encode2DiscreteMath(parent)
    sub = Encode2DiscreteMath(sub)
    for var in vars:
        print(var, end=" ")
    print(expr, end=' ')
    print(expr.replace(parent, sub), end=' ')
    print("equality")
    sub = expr.replace(parent, sub)
    parent = expr
    _strec(vars, output_dict, parent, sub)

def _ievrec(vars: list, val_dict: OrderedDict, ret: list, expr1: str, expr2: str) -> bool:
    truth_value = ['1', '0']
    if ret[0]:
        if len(vars) == 0:
            val1 = logic_eval(expr1, val_dict)
            val2 = logic_eval(expr2, val_dict)
            if val1 != val2:
                ret[0] = False
        else:
            for truth in truth_value:
                var = vars.pop(0)
                val_dict[var] = truth
                _ievrec(vars, val_dict, ret, expr1, expr2)
                vars.insert(0, var)

def is_equation(vars: list, expr1: str, expr2: str) -> bool:
    val_dict = OrderedDict()
    ret = [True]
    _ievrec(vars, val_dict, ret, expr1, expr2)
    if ret[0]:
        return True
    return False

def gen_expr(m: int, n: int) -> str:
    op = ['', 'v', '@', '']
