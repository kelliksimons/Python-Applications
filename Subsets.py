# Given an array of integers, print the sums of all subsets in it
# For example given the array [2, 3],
# the outputs should be 0, 2, 3 and 5. The outputs do not have to be printed in any particular order.

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf doing his work

    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

#Driver Program

print(deliver_presents_recursively(houses))
