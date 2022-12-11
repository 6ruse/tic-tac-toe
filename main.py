def printPlayingField(aField):
    vNum = '  0 1 2'
    print(vNum)
    for row, i in zip(aField, vNum.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")

def getUserInput(aField):
    while True:
        vPlace = input('Введите координаты следующего хода :').split()
        if len(vPlace) != 2:
            print('Введите 2 координаты')
            continue

        if not(vPlace[0].isdigit() and vPlace[1].isdigit()):
            print('Введите числа')
            continue

        vX,vY = map(int, vPlace)
        if not(vX >= 0 and vX < 3 and vY >= 0 and vY < 3):
            print('Координаты находятся вне диапазона игрового поля')
            continue

        if aField[vX][vY] != '-':
            print('По введенным координатам уже есть значение')
            continue

        break
    return vX, vY

def isWin(aField, aCustomValue):
    vList = []
    vPosition = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for l in aField:
        vList += l
        vIdx = set([i for i, j in enumerate(vList) if j == aCustomValue])
        for p in vPosition:
            if len(vIdx.intersection(set(p))) == 3:
                return True
    return False

# - основной код программы
gPlayingField = [['-'] * 3 for _ in range(3)] # g - глобальная переменная для формирования поля игры

for i in range(0, 10):
    if i == 9:
        print('\n ничья')
        break

    if i % 2 == 0:
        vCustomValue = 'x'
    else:
        vCustomValue = 'o'

    printPlayingField(gPlayingField)
    x, y = getUserInput(gPlayingField)
    gPlayingField[x][y] = vCustomValue

    if isWin(gPlayingField, vCustomValue):
        print(f"\n Выиграл {vCustomValue}")
        break

printPlayingField(gPlayingField)