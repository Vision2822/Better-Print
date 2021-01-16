import string
import random
import os

def betterprint(goal):
    result = ''
    for x in goal:
      if x.isalpha():
          if x.islower():
              chars = string.ascii_lowercase
          else:
              chars = string.ascii_uppercase
          while True:
            char = random.choice(chars)
            if char == x:
              result += char
              os.system("cls")
              print(result)
              break
      else:
          result += x
          os.system("cls")
          print(result)

if __name__ == "__main__":
    goal = "Hello World!"
    result = ''
    betterprint(goal)
