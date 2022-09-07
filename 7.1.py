class Matrix:
    def __init__(self, data):
        self.data = data


    def __str__(self):
        return '\n'.join('\t'.join([f"{itm:3}" for itm in line])for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return  f'Ошибка размерностй матрицы'


m_1 = [[3, 2, 6], [2, 3, 4], [-1, -2, -3]]
m_2 = [['1', '2', '4'], ['6', '11', '24'], ['-48', '-96', '192']]

matrx1 = Matrix(m_1)
matrx2 = Matrix(m_2)
sum_m = matrx1 + matrx2