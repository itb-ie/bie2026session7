#s = "A man, a plan, a canal, Panama!"
s = "Yo! Banana Boy?"
# s = "a nut for a jar of tuna"

# step 1: Remove punctuation
# step 2: Remove spaces
# step 3: convert to upper/lower case
# step 4: compare with the reversed
# step 5: Profit!

punctuation = "!,.?-"
for p in punctuation:
    s = s.replace(p, "") # removing punctuation, one by one
print(s)
# now spaces
s = s.replace(" ", "")
print(s)
s = s.lower()
print(s)
if s == s[::-1]:
    print("IS palindrome")
else:
    print("NOT palindrome")
