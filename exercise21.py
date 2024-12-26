#list Statics


def length(lst):
    return len(lst)

def mean(lst):
    total=0
    for a in lst:
        total=total+a
    if len(lst)!=0: return total/length(lst)
    else : return "the list is empty"
    
def range_of_list(lst):
    if len(lst)!=0:
        min=max=lst[0]
        for a in lst:
         if a>max: max=a
         if a<min: min=a
        return max-min
    else : return -1


print("normal list case:")
numbers=[4, 5, 1, 71, 88, 63]
print("length: ",length(numbers))
print("mean: ",mean(numbers)) 
print("range: ",range_of_list(numbers))

print("empty list case: ")
empty=[]
print("length: ",length(empty))
print("mean: ",mean(empty)) 
print("range: ",range_of_list(empty))

print("floating numbers list case: ")
numbers=[5.2, 5.9, 88.9]
print("length: ",length(numbers))
print("mean: ",mean(numbers)) 
print("range: ",range_of_list(numbers))