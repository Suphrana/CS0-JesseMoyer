    
def piececount():
    numberOfPieces = int(input())
    piece1 = list(map(int, input().split()))
    piece1.sort(reverse = True)
    return piece1

def fallingapart(pieces):
    AliceTurn = True
    sumAlice = 0
    sumBob = 0
    for piece in pieces:
        if AliceTurn:
            sumAlice += piece
        else:
            sumBob += piece

        AliceTurn = not AliceTurn

    return sumAlice, sumBob
    

def test():
    test1 = [3, 3 ,1]
    test2 = [4, 3, 1]
    test3 = [5, 5, 5]
    assert fallingapart(test1) == (4, 3)
    assert fallingapart(test2) == (5, 3)
    assert fallingapart(test3) == (10, 5)

def main():
    pieces = piececount()
    fallingapart(pieces)
    result = fallingapart(pieces)
    print(*result, sep=" ")
    test()
main()

