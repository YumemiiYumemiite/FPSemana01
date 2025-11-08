class Personagem:
    def __init__(self, nome, ataque, defesa):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa

def criar_personagem():
    nome = input()
    ataque = int(input())
    defesa = int(input())
    return Personagem(nome, ataque, defesa)

personagens = [criar_personagem() for _ in range(3)]

print()
print([
    [personagens[0].nome, (personagens[0].ataque, personagens[0].defesa)],
    [personagens[1].nome, (personagens[1].ataque, personagens[1].defesa)],
    [personagens[2].nome, (personagens[2].ataque, personagens[2].defesa)]
])

maior_ataque = max(p.ataque for p in personagens)
maior_defesa = max(p.defesa for p in personagens)

melhor_ataque = next(p for p in personagens if p.ataque == maior_ataque)
melhor_defesa = next(p for p in personagens if p.defesa == maior_defesa)


print(f"Ataque {melhor_ataque.nome} {melhor_ataque.ataque}")
print(f"Defesa {melhor_defesa.nome} {melhor_defesa.defesa}")