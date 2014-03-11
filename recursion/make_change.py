"""
Write a recursive function to count the possible ways to make change of 
$1.00, using quarters, dimes, nickles and pennies.
"""

def findNumChange(amount, step, changeList):
    """
    Method takes in what step it is on and 
    the changeList which is the list of
    possible denominations.
    """
    if amount == 0:
        return 1
    if amount < 0 or step < 0:
        return 0

    totalWays = 0
    for i in  range(step, len(changeList)):
        totalWays += findNumChange(amount-changeList[i], i, changeList)

    return totalWays

change = [50,25,10,5,1]
print findNumChange(200, 0, change)




