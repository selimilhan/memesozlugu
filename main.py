meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "IDK": "Bilmiyorum (I Don't Know)",
    "VIBE": "Bir ortamın veya kişinin verdiği his"
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Böyle bir kelime bulunmuyor")
