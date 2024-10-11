from simpleai.search import CspProblem, backtrack, min_conflicts
variables = ('WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T') 
domains = {v: ['red', 'green', 'blue'] for v in variables} 
constraints = [ 
 (('WA', 'NT'), lambda variables, values: values[0] != values[1]), 
 (('WA', 'SA'), lambda variables, values: values[0] != values[1]), 
 (('SA', 'NT'), lambda variables, values: values[0] != values[1]), 
 (('SA', 'Q'), lambda variables, values: values[0] != values[1]), 
 (('NT', 'Q'), lambda variables, values: values[0] != values[1]), 
 (('SA', 'NSW'), lambda variables, values: values[0] != values[1]), 
 (('Q', 'NSW'), lambda variables, values: values[0] != values[1]), 
 (('SA', 'V'), lambda variables, values: values[0] != values[1]), 
 (('NSW', 'V'), lambda variables, values: values[0] != values[1]), 
] 
my_problem = CspProblem(variables, domains, constraints) 
print(backtrack(my_problem)) 
print(backtrack(my_problem))  
print(backtrack(my_problem))  
print(backtrack(my_problem))  
print(backtrack(my_problem))  
print(backtrack(my_problem))  
print(min_conflicts(my_problem))
