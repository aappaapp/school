import random

def swap(a, b):
  c = a
  a = b
  b = c
  return a, b

def show_list(num = -2):
  for i in range(0, 10):
    print(f"Card[{i}] = {card_list[i]}", end="")
    if i == num or i == num + 1:
      print("<-", end="")
    print()
  print(f"Swappings: {swappings}")
  print(f"Comparisons: {comp}")
  input("Press enter to continue...")
  print()

def gen_list():
  random.shuffle(card_list)

# Main
swap_flag = True
swappings = 0
comp = 0

card_list = [i for i in range(0, 10)]
print("Before shuffling:")
show_list()
gen_list()
print("After shuffling:")
show_list()

while swap_flag:
  swap_flag = False
  for i in range(0, 9):
    comp += 1
    if card_list[i] > card_list[i + 1]:
      card_list[i], card_list[i + 1] = swap(card_list[i], card_list[i + 1])
      swap_flag = True
      swappings += 1
      show_list(i)

print("After sorting:")
show_list()


