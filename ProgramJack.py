#Creating phrase variables
this = 'This is the'
house = ' house that Jack built.'
lay = 'That lay in the'
ate = 'That ate the'
kill = 'That killed the'
worry = 'That worried the'
horn = ' with the crumpled horn,'
toss = 'That tossed the'
forlorn = ' maiden all forlorn'
milk = 'That milked the cow'
conclusion = lay + house + '\n'
atemalt = ate + ' malt'
killrat = kill + ' rat,'
worrycat = worry + ' cat,'
tossdog = toss + ' dog,'
ateconclusion = atemalt + '\n' + conclusion
killconclusion = killrat + '\n' + ateconclusion
worryconclusion = worrycat + '\n' + killconclusion
tossconclusion = tossdog + '\n' + worryconclusion
hornconclusion = horn + '\n' + tossconclusion

#Stringing together the phrases
print(this + house + '\n')

print(this + ' malt' + '\n' + conclusion)

print(this + ' rat,' + '\n' + ateconclusion)

print(this + ' cat,' + '\n' + killconclusion)

print(this + ' dog,' + '\n' + worryconclusion)

print(this + ' cow' + hornconclusion)

print(this + forlorn + '\n' + milk + hornconclusion)