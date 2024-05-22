#დავალება 2
# def manual_index(numbers_list , search_value):
#     for i in range (len(numbers_list)):
#         if numbers_list[i] == search_value:
#             return i
        
# result = manual_index([1,2,3,4,5,6,7,8,9,],3)
# print (result)

#დავალება 3   
def manual_max_(number_list):
    max_value = number_list[0]

    for i in number_list [1:]:
        if i > max_value:
            max_value=i
        return i
        
result = manual_max([1,3,6,8,99]) 
print(result)