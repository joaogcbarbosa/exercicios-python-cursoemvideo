def aumentar(v=0, t=0, formato=False):
    v = v + v * (t/100)
    if formato is False:
        return v
    else:
        moeda(v)


def diminuir(v=0, t=0, formato=False):
    v = v - v * (t/100)
    if formato is False:
        return v
    else:
        moeda(v)


def dobro(v=0, formato=False):
    v *= 2
    if not formato:
        return v
    else:
        moeda(v)


def metade(v=0, formato=False):
    v /= 2
    if not formato:
        return v
    else:
        moeda(v)


def moeda(v=0, m='R$', formato=False):
    return f'{m}{v:.2f}'.replace('.', ',') if formato is False else moeda(v)
