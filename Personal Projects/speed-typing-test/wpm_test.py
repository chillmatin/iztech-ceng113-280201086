import timeit

string = 'addition nervous fetch reminiscent heal agonizing warn board sulky desk mass one committee outrageous public loss peck thoughtful mushy luxuriant satisfying possessive previous hook memorize shake grandmother spare economic air splendid rapid calendar supply gifted arrogant fold two marble common wicked zippy increase naive pat treatment adjustment legal bubble friction sweet bare hellish wall valuable near synonymous colorful spiritual dreary organic illustrious lamp flight afternoon comb limping veil collect odd stem frame bewildered scandalous story want tour mindless twist thunder hissing coil abortive berry lackadaisical border womanly ultra wave spray baseball angle panicky adorable ants star day winter position reaction measure snotty ahead attack sidewalk harm stimulating future daughter violet birth responsible race aloof spurious ask north abounding dry worm bell wobble horrible juicy heat combative silver gorgeous toe jump handsomely dock aware alleged observe shivering famous applaud defiant unaccountable volleyball puncture thirsty slimy agreement delay invent tender scary aboard exciting caption sedate mask electric aggressive left hurried gratis soup productive order nosy boiling savory cause green fumbling milky ship spot loving pale science shave planes scene grape eager machine staking frightened private program blind cruel possible chess tawdry stay real overrated wound scintillating flagrant debt stroke miss skin fail'

wordizer = string.split(' ')
choice = True
while choice:
    print("You will be given some words and you should write the same word beneath")

    key = ''
    while True:
        key = input("Type 'go' to start or 'stop' to leave! ")
        if key == 'stop':
            quit()
        elif key == 'go':
            break
        else:
            print("Invalid Input")

    t = timeit.default_timer()
    correct = 0
    wrong = 0
    for word in wordizer:
        print('\n'+word)
        typer = input("-> ")
        if typer == word:
            correct += 1
        else:
            wrong += 1
    elapsed_time = timeit.default_timer() - t
    speed = correct * 60 / elapsed_time

    print("You typed {:.0f} words per minute. Out of {} words, you misspelled {} words!".format(
        speed, correct + wrong, wrong))

    choice = input("Wanna play again?\ny/n -> ")
    if choice.lower() == 'y':
        choice = True
    elif choice.lower() == 'n':
        choice = False
    else:
        print("WHAT?")

print("Goodbye, winner!")
