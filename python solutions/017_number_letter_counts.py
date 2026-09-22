    #
    # Solved by mang-s
    # Date: 06/04/25
    #
    # https://projecteuler.net/problem=17
    # https://github.com/mang-s/Project-Euler-Solutions
    #
    
def nunmber_letter_counts(rangemax: int = 1000) -> int:
      
    words = { 0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
        6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
        11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
        15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
        19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 
        50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
        
    storage = []
        
    for i in range(1, rangemax + 1):
        if i == 1000:
            storage.append(words[1] + " thousand")
            
        elif i in range(1, 21): # From 1 to 20
            storage.append(words[i])
            
        elif i == 100 or i == 200 or i == 300 or i == 400 or i == 500 or i == 600 or i == 700 or i == 800 or i == 900: # Case for the round hundreds

            storage.append(words[i // 100] + " hundred")
            
        elif i in range(21, 100): # From 21 to 99

            storage.append(words[ int(str(i)[0] + '0') ] + " " + words[ int(str(i)[1]) ])
            
        elif i in range(101, 121) or i in range(201, 221) or i in range(301, 321) or i in range(401, 421) or i in range(501, 521) or i in range(601, 621) or i in range(701, 721) or i in range(801, 821) or i in range(901, 921): # From x00 to x20
            storage.append(words[ int(str(i)[0]) ] + " hundred and " + words[ int(str(i)[1] + str(i)[2])])
            
        elif i in range(121, 1000) or i in range(221, 300) or i in range(321, 400) or i in range(421, 500) or i in range(521, 600) or i in range(621, 700) or i in range(721, 800) or i in range(821, 900): # From x21 to 999
            storage.append(words[ int(str(i)[0]) ] + " hundred and " + words[ int(str(i)[1] + '0') ] + "-" + words[ int(str(i)[2]) ])
        
    chara_counter = 0
    for word in storage:
        word = word.replace(' ', '').replace('-', '')
        for _ in word:
            chara_counter += 1
    
    return chara_counter
    
if __name__ == "__main__":
    
    print(nunmber_letter_counts())