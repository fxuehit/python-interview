a = range(5)

print(type(a))
print(list(a))

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
gen = infinite_sequence()
for i in infinite_sequence():
    print(i, end= ",")
    
print(next(gen))  
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 

    
