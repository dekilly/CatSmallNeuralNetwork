from PIL import Image

lst = []
print("Какого цвета кот?\nБелый(б)  Серый(с)  Рыжий(р)  Черный(ч)")
Fur_Color = (input())
if Fur_Color == "б":
    lst.append(0)
    lst.append(0)
elif Fur_Color == "с":
    lst.append(0)
    lst.append(1)
elif Fur_Color == "р":
    lst.append(1)
    lst.append(0)
elif Fur_Color == "ч":
    lst.append(1)
    lst.append(1)

print("У кота короткая(к) или длинная(д) шерсть?")
Fur_Lenght = (input())
if Fur_Lenght == "к":
    lst.append(0)
elif Fur_Lenght == "д":
    lst.append(1)

print("Шерсть однотонная(о) или пятнистая(п)?")
Fur_Pattern = (input())
if Fur_Pattern == "о":
    lst.append(0)
elif Fur_Pattern == "п":
    lst.append(1)

print("Кот по размеру средний(с) или крупный(к)?")
Cat_Size = (input())
if Cat_Size == "с":
    lst.append(0)
elif Cat_Size == "к":
    lst.append(1)

print("Какого цвета глаза у кота?\nЖелтые(ж)  Зелёный(з)  Голубой(г)  Серый(с)")
Eye_Color = (input())
if Eye_Color == "ж":
    lst.append(0)
    lst.append(0)
elif Eye_Color == "з":
    lst.append(0)
    lst.append(1)
elif Eye_Color == "г":
    lst.append(1)
    lst.append(0)
elif Eye_Color == "с":
    lst.append(1)
    lst.append(1)

print(lst)


class Neuron:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def convert(self, x):
        return [-1 if i == 0 else i for i in x]

    def solve(self, x):
        converted_x = self.convert(x)
        S = sum([xn * kn for xn, kn in zip(self.k, converted_x)]) - self.b
        self.activate(S)

    def activate(self, S):
        self.out = True if S == 0 else False


n_list = [Neuron([1, 1, 1, -1, -1, -1, 1], -3),  # 0
          Neuron([2, 1, 1, 1, 1, 1, 2], 1),      # 1
          Neuron([1, 1, 1, 1, 1, 1, 1], -5),     # 2
          Neuron([1, 2, 1, 1, 1, 1, 1], 4),      # 3
          Neuron([2, 1, 1, 1, 1, 1, 2], -5),     # 4
          Neuron([1, 1, 2, 1, -2, 2, 1], 2),     # 5
          Neuron([1, 1, 1, 2, 1, 2, 1], -5),     # 6
          Neuron([1, 2, 1, 2, 1, -1, -1], 1),    # 7
          Neuron([2, 1, 1, 1, 1, 1, 2], 5),      # 8
          Neuron([1, 1, 1, 1, 1, 1, 1], 1)       # 9
          ]

c = [[0, 0, 1, 0, 1, 1, 0],  # Рэгдолл
     [1, 0, 0, 1, 0, 0, 1],  # Бенгальская кошка
     [0, 1, 0, 0, 0, 0, 0],  # Шотландская вислоухая
     [1, 1, 1, 1, 1, 0, 0],  # Мейн-кун
     [0, 1, 0, 1, 0, 0, 0],  # Манчкин
     [1, 0, 1, 1, 0, 0, 0],  # Курильский бобтейл
     [0, 1, 0, 0, 0, 0, 1],  # Русская голубая
     [0, 1, 0, 1, 0, 0, 1],  # Канадский «сфинкс»
     [1, 0, 1, 1, 1, 0, 1],  # Сибирская кошка
     [1, 0, 0, 0, 1, 1, 1],  # Шлёпа (Русский кот) – Каракал
     [0, 0, 0, 0, 0, 0, 0]
     ]

def cat():
    global img
    if i == 0:
        cat_name = "Рэгдолл"
        img = Image.open('cat0.jpg')
    elif i == 1:
        cat_name = "Бенгальская кошка"
        img = Image.open('cat1.jpg')
    elif i == 2:
        cat_name = "Шотландская вислоухая"
        img = Image.open('cat2.jpg')
    elif i == 3:
        cat_name = "Мейн-кун"
        img = Image.open('cat3.jpg')
    elif i == 4:
        cat_name = "Манчкин"
        img = Image.open('cat4.jpg')
    elif i == 5:
        cat_name = "Курильский бобтейл"
        img = Image.open('cat5.jpg')
    elif i == 6:
        cat_name = "Русская голубая"
        img = Image.open('cat6.jpg')
    elif i == 7:
        cat_name = "Канадский «сфинкс»"
        img = Image.open('cat7.jpg')
    elif i == 8:
        cat_name = "Сибирская кошка"
        img = Image.open('cat8.jpg')
    elif i == 9:
        cat_name = "Шлёпа (Русский кот) – Каракал"
        img = Image.open('cat9.jpg')
    return cat_name

flag = 0
for j in range(len(c)):
    for i in range(len(n_list)):
        n_list[i].solve(c[j])
        if (n_list[i].out):
            if lst == c[j]:
                print(cat())
                flag = 1
                break

if flag == 1:
    img.show()
if flag == 0:
    print("Кот не распознан")


