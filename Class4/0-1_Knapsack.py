# breakdown
# row of table corresponding to item from 0 to items
# column of table corresponding to weight limit from 0 to Capacity
# index of very last cell is [item][capacity]

    # [i][j] represents the maximum profit possible i as items and j as total weight limit

# to fill table started by setting the 0th row and col to 0
    # 0th row = no objects
    # 0th col = max weight possible is 0

    # to fill the cells:
        # include object [i] in final selection
            # weight limit after including object [i] !> weight limit
            # profit after including object [i] > to before including
        # don't include object [i]

def knapSack(capacity, weights, values): 
    items=len(values)
    # traverse thru the table filling entries using nested loop
    table = [[0 for x in range(capacity + 1)] for x in range(items + 1)] 
 
    for i in range(items + 1): 
        for j in range(capacity + 1): 

            # setting 0th row and col to 0 
            if i == 0 or j == 0: 
                table[i][j] = 0

            # checking weight of [i]th object is < total weight allowed    
            elif weights[i-1] <= j:

                # select max out of the two, to include or exclude
                table[i][j] = max(values[i-1]  
+ table[i-1][j-weights[i-1]],  table[i-1][j]) 
            else:

                # when weight  of object(i) > limit(j)
                table[i][j] = table[i-1][j] 
   
    # when cells filled, return last cell as the profit
    return table[items][capacity] 
 
#values = [1,2,5,6]
#weights = [2,3,4,5]
#capacity = 8

values = [int(item) for item in input("Enter the values: ").split()]
weights = [int(item) for item in input("Enter the weights: ").split()]
capacity = int(input("Enter capacity: "))
print("Total Profit: ")
print(knapSack(capacity, weights, values))
