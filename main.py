import logic.logic as ll

expr1 = 'P -> (Q v R)'
expr2 = '((Q v R) -> P)'
ll.isequation(['P', 'Q', 'R'], [expr1], expr2)
print(ll.is_equation(['P', 'Q', 'R'], expr1, expr2))