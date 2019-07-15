words=input("Enter your message. ")
swap=int(input('Enter the key '))
code=''
characters=[chr(char) for char in range(97,123)]
for word in words:
  if word in characters:
    word=ord(word)
    word=word+swap
    if (word>122):
      word=word-26
    word=chr(word)
  code=code+word
print("The encrypted code is " + code)
decrypt=input("Would you like to decrypt the message? ")
positive_responses=['yes','yo','yup','indeed','yeah']
if decrypt.lower() in positive_responses:
    print("Here is the the decrypted message.")
    decrypted=''
    for word in code:
      if word in characters:
        word=ord(word)
        word=word-swap
        if (word<97):
          word=word+26
        word=chr(word)
      decrypted=decrypted+word
    print(decrypted)
else:
  print('ok cool')