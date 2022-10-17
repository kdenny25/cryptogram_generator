import numpy as np

class encryptPhrase:
    '''Encrypts a string provided to it.'''

    def __init__(self):
        self.__phrase = ""
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.encryptedalpha = []
        self.__mostletters = []


    # encrypt the alphabet array. Uses phrase length to improve randomness
        # encrypt the alphabet array. Uses phrase length to improve randomness
    def getEncryptAlpha(self):
        """Returns shuffled alphabet list"""
        # initiate a list that will contain random numbers
        numlist = np.arange(26)
        np.random.shuffle(numlist)
        # initiate a list that will contain encrypted version of alphabet
        encalpha = []

        ix = 0

        while ix < len(numlist):
            if ix == numlist[ix]:
                #check if ix is last position
                if ix == 25:
                    numlist[ix], numlist[ix-1] = numlist[ix-1], numlist[ix]
                    if 24 == numlist[24]:
                        ix = -1
                if ix != 25:
                    #swap values

                    numlist[ix], numlist[ix+1] = numlist[ix+1], numlist[ix]
            ix +=1

        # assign random number in an array. This is in place of the new encrypted alphabet
        # for ix, j in enumerate(self.alphabet):
        #     numisused = True
        #
        #     while numisused:
        #         # generate a random umber for the length of the phrase
        #         #for i in self.__phrase:
        #         randnum = random.randint(0, 25)
        #
        #         numisused = False
        #
        #         if randnum in numlist:
        #             numisused = True
        #         if ix == randnum:
        #             numisused = True
        #         # checks if the random number has been used or is the same as the
        #         # number placement in the alphabet
        #         # for idx, k in enumerate(numlist):
        #         #     if numlist[idx] == randnum:
        #         #         numisused = True
        #         #     if ix == randnum:
        #         #         numisused = True
        #
        #     numlist.append(randnum)
        #    print(numlist)
        # generate an encrypted alphabet
        print(numlist)
        for idx, l in enumerate(self.alphabet):
            encalpha.append(self.alphabet[numlist[idx]])

        return encalpha

    # Looks for most used letters in phrase and returns a list with letters sorted from most to least
    def getMostLetters(self):
        letterCount = [0] * len(self.alphabet)
        alphaList = self.alphabet

        # Iterate through phrase and generate a list of letter counts
        for dex, i in enumerate(self.__phrase.upper()):
            # Finds character placements in the alphabet and adds to the counter
            for idx, j in enumerate(self.alphabet):
                if i == j:
                    letterCount[idx] = letterCount[idx]+1

        # Create blank list to store count of used letters in phrase
        usedLettersCount = []
        # Create blank list to store used letters in phrase
        usedLettersList = []

        # Generate list of letters only in phrase
        for inx, k in enumerate(letterCount):
            if k > 0:
                usedLettersCount.append(k)
                usedLettersList.append(alphaList[inx])

        # Sort the list from most used to least used characters in the phrase
        for idx, l in enumerate(usedLettersCount):
             for idn, p in enumerate(usedLettersCount):
                 if l > p:
                    tempCLoc = l
                    tempALoc = usedLettersList[idx]
                    # Swap letters and count if one is larger than the other
                    usedLettersCount[idx] = usedLettersCount[idn]
                    usedLettersList[idx] = usedLettersList[idn]
                    usedLettersCount[idn] = tempCLoc
                    usedLettersList[idn] = tempALoc

        return usedLettersList

    # Private Class_Checks if character is a special character and returns a boolean value
    def __isSpecialChar(self, charToCheck):
        specialChar = r"!@#$%&*()'+,-./:;<=>?\"[]^_`{|}1234567890? "

        isSpecial = False

        for i in specialChar:
            if i == charToCheck:
                isSpecial = True

        return isSpecial

    def getEncryptedPhrase(self):
        encryptedPhrase = ""
        print(self.__phrase)
        for i in self.__phrase.upper():
            if self.__isSpecialChar(i):
                encryptedPhrase += i
            else:
                for idx, j in enumerate(self.alphabet):
                    if j == i:
                        encryptedPhrase += self.encryptedalpha[idx]

        return encryptedPhrase

    def setPhrase(self, phrase):
        self.__phrase = phrase.upper()
        self.encryptedalpha = self.getEncryptAlpha()
        self.__mostletters = self.getMostLetters()

    def getNumHints(self):
        return len(self.__mostletters)

    # returns a hint specified by placement in MostLetters list
    def getHint(self, hintnum):
        for idx, i in enumerate(self.alphabet):
            if i == self.__mostletters[hintnum]:
                return (self.encryptedalpha[idx] + " = " + i)


# p = encryptPhrase()
#
# phraseList = ["It's always sunny out!", "I enjoy eating ice cream outside!"]
# for i in phraseList:
#     p.setPhrase(i)
#     print(p.encryptedalpha)
#     print(p.getEncryptedPhrase())
#     print(p.getHint(1))
