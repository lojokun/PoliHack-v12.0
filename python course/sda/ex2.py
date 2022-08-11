a_list = [1,3,5,2,5,6,7,4,9,7]
for digit in a_list:
    print(digit)
print("\n")     
for digit in range(0,6):
    print(a_list[digit])
print("\n")
print("ostatnich cyfr\n")
for digit in a_list:
    if digit%2==0:
        print(digit)
print("\n")
for digit in range(1, len(a_list), 2):
    print(a_list[digit])
