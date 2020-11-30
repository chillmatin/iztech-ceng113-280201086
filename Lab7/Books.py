books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
unique = []
dictionary = {}
for book in books:

  for char in book:
    if not char in unique:
      unique.append(char)
  
  dictionary[book] = (len(book), len(unique))

print(dictionary)
  