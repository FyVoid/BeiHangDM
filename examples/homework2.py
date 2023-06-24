import logic.logic as ll
# 1. 3-7
expr = 'Q -> (R ->(Q ^ R))'
ll.truthtable(['Q', 'R'], expr)

'''
output:
Q R Q → (R →(Q ∧ R))
1 1          1
1 0          1
0 1          1
0 0          1
'''

# 2. 3-4
pre = ['P', 'Q -> (P -> R)']
expr = 'Q -> R'
ll.isargument(['P', 'Q', 'R'], pre, expr)

'''
output:
P Q R P Q -> (P -> R) Q → R P, Q -> (P -> R) ╞ Q → R
1 1 1 1         1       1              1
1 1 0 1         0       0              1
1 0 1 1         1       1              1
1 0 0 1         1       1              1
0 1 1 0         1       1              0
0 1 0 0         1       0              1
0 0 1 0         1       1              0
0 0 0 0         1       1              0
'''

# 3. 3-3
expr = '(Q ^ (Q -> R)) -> R'
ll.truthtable(['Q', 'R'], expr)

'''
output:
Q R (Q ∧ (Q → R)) → R
1 1          1
1 0          1
0 1          1
0 0          1
'''