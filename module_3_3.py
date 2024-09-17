def  print_params(a = 1, b = 'Igor', c = True):
    print(a,b,c)
values_list = [4,'кирпич', False]
values_dict = {'a':1, 'b':'Igor', 'c':True}
values_list_2 = [54.32, 'Строка']
print_params(1,2)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)