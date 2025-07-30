def palindrome():
  word = input("Enter a word: ")
  reverse = word[::-1]
  if word == reverse:
    print("It is a Palindrome")
  else:
    print("Not a Palindrome")


palindrome()