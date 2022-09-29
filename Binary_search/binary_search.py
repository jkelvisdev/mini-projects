def binary_search(elements, item):
    start_point = 0
    end_point = len(elements) - 1

    while start_point <= end_point:
        mid_point = (start_point + end_point) // 2 #setting mid point
        if item == elements[mid_point]:
            return mid_point   # if the element is found it will return the value
        elif item > elements[mid_point]:
            start_point = mid_point + 1 #moving the mid point if element is in the right side
        else: 
            end_point = mid_point - 1 #moving the mid point to the left if the element is in the left side
    return print("is not here")
    
elements = [2,3,4,5,6,7,8,9,10,12,14,16] #[12,15,19,25,40,62,64,200,1000,2020,3939]
item = 14

print("The index is the number: ", binary_search(elements, item))