def aumentar(v=0, t=0, formato=False):
    v = v + v * (t / 100)
    if formato is False:
        return v
    else:
        moeda(v)


def diminuir(v=0, t=0, formato=False):
    v = v - v * (t / 100)
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


def resumo(v, a, r):
    res = dict()

    res['Preço analisado'] = f'{moeda(v)}'
    res['Dobro do preço'] = f'{moeda(v * 2)}'
    res['Metade do preço'] = f'{moeda(v / 2)}'
    res[f'{a}% de aumento'] = f'{moeda(v + v * (a / 100))}'
    res[f'{r}% de redução'] = f'{moeda(v - v * (r / 100))}'

    print('=' * 33)
    print('RESUMO DO VALOR'.center(33))
    print('=' * 33)
    for k, v in res.items():
        print(f'{k:.<25}{v}')
    print('=' * 33)
