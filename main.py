gPlayingField = [['-'] * 3 for _ in range(3)] # g - глобальная переменная для формирования поля игры

def printPlayingField():
    vNum = '  0 1 2'
    print(vNum)
    for row, i in zip(gPlayingField, vNum.split()):
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

# vCount = 0
# while True:
for i in range(0, 10):
    if i == 9:
        print('НИЧЬЯ')
        break

    if i % 2 == 0:
        vCustomValue = 'x'
    else:
        vCustomValue = 'o'

    printPlayingField()
    x, y = getUserInput(gPlayingField)
    gPlayingField[x][y] = vCustomValue

    # vCount += 1

printPlayingField()