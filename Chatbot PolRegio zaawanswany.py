import random
keywords = ["music", "pet", "book", "dumbwords", "skibiditojlet"]
responses = ["music is bad", "pets are dumb", "only pkp books", "uyffwwwwwsaygsuadgayutdguAFDGSfvrg764rtywcrewgr6etcuagfccvabfhdjsgc","dumb skibiditoiljiet"]

greetings = ["welcome on board this lka service", "welcome on board this Polregio service"]
goodbyes = ["we wish you a good stay, goodbye", "we wish you a good loot, trainspotters"]

print("bot: " + random.choice(greetings))

while True:
    text = input("say sth to me: ") .lower()
    if (text == "terminus station"):
        break

    exists = False
    for index  in range(len(keywords)):
        if (keywords[index] in text):
            print("Bot: " + responses[index])
            exist = True
    if (exists == False):
        newKeyword = input("I don't know how to response, type keword: ")
        keywords.append(newKeyword)
        newResponse = input("How should I respond it: ")
        responses.append(newResponse)

print(random.choice(goodbyes))