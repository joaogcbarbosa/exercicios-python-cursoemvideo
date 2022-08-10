def aumentar(v=0, t=0):
    v = v + v * (t/100)
    return v


def diminuir(v=0, t=0):
    v = v - v * (t/100)
    return v


def dobro(v=0):
    v *= 2
    return v


def metade(v=0):
    v /= 2
    return v


def moeda(v=0, m='R$'):
    return f'{m}{v:.2f}'.replace('.', ',')
