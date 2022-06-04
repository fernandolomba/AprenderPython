# Conjuntos
# No puede haber elementos repetidos
# No tienen orden(primero numeros de - a + y luego letras de a-z)
# Son heterogeneos
# Son inmutables

set1 = set([1, 2, 3, 4, 5, 6, 7])
print(set1)
print(type(set1))
set2 = {1, 2, 3, 4, 5, 6, 7}
print(set2)
print(type(set2))

set3 = {1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4}
print(set3)
print(type(set3))

# Subconjunto (<=) B de A es un conjunto que contiene alguno de los elementos de A (o quizas todos)
# Subconjunto propio (<) B de un conjunto A tiene alguno de los elementos pero no todos.
A = {0, 3, 7, 2, 5}
B = {2, 3, 0}
print( B.issubset(A))
print(B<=A)
print(B<A)
print(A<=B)
print(A<B)

# Superconjunto. Un superconjunto A de un conjunto B es un conjunto que contiene a B. Se denota por A⊇B
# Superconjunto propio. Un superconjunto propio A de un conjunto B es un conjunto que contiene a B y consta de al menos un elemento más.