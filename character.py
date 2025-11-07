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

maior_ataque = max(p.ataque for p in personagens)
maior_defesa = max(p.defesa for p in personagens)

melhor_ataque = next(p for p in personagens if p.ataque == maior_ataque)
melhor_defesa = next(p for p in personagens if p.defesa == maior_defesa)

print()
print(f"Ataque {melhor_ataque.nome} {melhor_ataque.ataque}")
print(f"Defesa {melhor_defesa.nome} {melhor_defesa.defesa}")


print()
for p in personagens:
    print(p.nome)
    print(p.ataque)
    print(p.defesa)