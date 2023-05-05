import logic.logic as ll

expr1 = 'P -> (Q v R)'
expr2 = '((Q v R) -> P)'
result = ll.is_equation(['P', 'Q', 'R'], expr1, expr2)
print(result)