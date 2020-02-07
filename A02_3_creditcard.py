
card_number = input("Enter your credit card number!")
def checkSum(cardNum):
    sumOfNum = 0
    for i in cardNum:
        char = ord(i) - 48
        sumOfNum = sumOfNum + char
    if ((sumOfNum % 10) == 0):
        print('Valid credit card number')
        return True
    elif((sumOfNum % 10) != 0):
        print('Sum is not divisible by 10')
        return False

def check(card_number):
    if (len(card_number.replace(' ','')) != 16):
        print('Incorrect spacing or not 16 digits!')
        return False
    elif ((card_number[4] and card_number[9] and card_number[14]) != ' '):
        print('Incorrect spacing or not 16 digits!')
        return False
    else:
        cardNum = card_number.replace(' ','')
        checkCard = True
        for i in cardNum:
            if (ord(i) < 48 or ord(i) > 57):
                checkCard = False
        if (checkCard):
            checkSum(cardNum)
        if(checkCard == False):
            print('Incorrect spacing or not 16 digits!')
            return False
print(check(card_number))
