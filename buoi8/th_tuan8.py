import numpy as np
import math

docao = [[78, 72, 69, 71, 58, 49],
         [74, 67, 58, 49, 46, 50],
         [69, 53, 44, 37, 38, 48],
         [64, 58, 55, 22, 31, 24],
         [68, 61, 47, 21, 16, 19],
         [74, 53, 34, 12, 11, 12]]

sodong = len(docao)
socot = len(docao[0])
DIR = np.zeros((sodong, socot))

def Lancan(dong, cot, so_dong, so_cot):
    hang_xom = []
    for d in range(-1, 2):
        for c in range(-1, 2):
            if not ((d == 0) and (c == 0)):
                dong_hx = dong + d
                cot_hx = cot + c
                if (dong_hx >= 0) and (cot_hx >= 0) and (dong_hx < so_dong) and (cot_hx < so_cot):
                    hang_xom.append((dong_hx, cot_hx))
    return hang_xom

def getMaHuong(delta_dong, delta_cot):
    ma_huong = {
        (0, 1): 1,
        (1, 1): 2,
        (1, 0): 4,
        (1, -1): 8,
        (0, -1): 16,
        (-1, -1): 32,
        (-1, 0): 64,
        (-1, 1): 128
    }
    return ma_huong.get((delta_dong, delta_cot), 0)

def getHuong(dong, cot):
    vitrix = 0
    vitriy = 0
    chenhcao_max = 0

    danhsach_hangxom = Lancan(dong, cot, sodong, socot)

    for neighbor in danhsach_hangxom:
        deltax = neighbor[1] - cot
        deltay = neighbor[0] - dong
        heso_khoangcach = math.sqrt(deltax**2 + deltay**2)
        khoangcach = (docao[dong][cot] - docao[neighbor[0]][neighbor[1]]) / heso_khoangcach
        if chenhcao_max < khoangcach:
            chenhcao_max = khoangcach
            vitrix = deltax
            vitriy = deltay

    return vitriy, vitrix  # Chuyển đổi vị trí của dòng và cột

def FlowDirection():
    for dong in range(sodong):
        for cot in range(socot):
            huong = getHuong(dong, cot)
            DIR[dong][cot] = getMaHuong(huong[0], huong[1])

# Gọi hàm FlowDirection() để thực thi
FlowDirection()

# In ma trận DIR
print(DIR)
