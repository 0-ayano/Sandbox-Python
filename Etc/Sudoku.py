def values_from_grid(grid):
    "テキストから２次元配列のvaluesを作成する"
    values = []
    digits = "123456789"
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    grid_int = map(lambda x: int(x) if x != "." else 0, chars)

    count = 0
    row = []
    for i in grid_int:
        row.append(i)
        count += 1
        if count % 9 == 0: #行毎に分割
            values.append(row)
            row = []
    return values

def solver(values, x=0, y=0):
    "数独を解く"
    if y > 8: #ポインタが最後までいったら完成
        return True
    elif values[y][x] != 0: #空欄ではないなら飛ばす
        if x == 8: #8列までいったら次の行に移動
            if solver(values, 0, y+1):
                return True
        else:
            if solver(values, x+1, y):
                return True
    else:
        for i in range(1, 10):#1から9までの数字を全て試す
            if check(values, x, y, i): #チェックする
                values[y][x] = i #OKなら数字を入れる
                if x == 8: #8列までいったら次の行に移動
                    if solver(values, 0, y+1):
                        return True
                else:
                    if solver(values, x+1, y):
                        return True
        values[y][x] = 0 #戻ってきたら0に戻す
        return False

def check(values, x, y, i):
    if row(values, y, i) and column(values, x, i) and block(values, x, y, i):
        return True
    return False

def row(values, y, i):
    "横をチェック"
    return all(True if i != values[y][_x] else False for _x in range(9))

def column(values, x, i):
    "縦をチェック"
    return all(True if i != values[_y][x] else False for _y in range(9))

def block(values, x, y, i):
    "3x3のブロックをチェック"
    xbase = (x // 3) * 3
    ybase = (y // 3) * 3
    return all(True if i != values[_y][_x] else False
            for _y in range(ybase, ybase + 3)
                for _x in range(xbase, xbase + 3))

num = "940100008008000096026008000060001004059020700007600000670400000500200000030000020"
values = values_from_grid(num)
solver(values)
print(values)

"""
- [Pythonで数独を解く](https://qiita.com/wsldenli/items/78596c8775a0673f255e)
"""
