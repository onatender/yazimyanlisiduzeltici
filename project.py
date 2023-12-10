from textblob import Word  # gerekli kütüphane import edilir.
text = input('Bir yazı yazınız:') # kullanıcıdan doğru veya yanlış kelimeler içeren bir cümle alınır.

words = text.split() #girdi kelimelerine ayrılır.
words = list(map(lambda word: Word(word).spellcheck()[0][0],words)) #cümledeki her kelime tek tek en olası doğru kelime ile değiştirilir.

#Inputun düzeltilmiş hali ekrana yazdırılır:
print(" ".join(words))