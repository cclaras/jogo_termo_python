import random

palavras = [
    "amigo", "banho", "casas", "dedos", "feliz",
    "grato", "hotel", "imune", "junto", "lento",
    "magro", "nuvem", "penas", "queda", "roupa",
    "susto", "tempo", "urros", "vazio", "zebra",
    "abriu", "barco", "custo", "doido", "esfri",
    "ficar", "gente", "horas", "idoso", "justo",
    "ligar", "mente", "nunca", "ossos", "parte",
    "quase", "rezar", "salas", "tapar", "uniao",
    "vozes", "zerar", "bocas", "chuva", "dados",
    "fosso", "gosto", "moeda", "tocar", "linha"
]

palavra_secreta = random.choice(palavras)

print("🎮 Bem-vindo ao Termo em Python!")
print("Tente adivinhar a palavra secreta de 5 letras.\n")

VERDE = "\033[4;32m"
AMARELO = "\033[4;33m"
CINZA = "\033[1;37m"
RESET = "\033[0m"

for tentativa in range(5):
    palpite = input(f"Tentativa {tentativa + 1}: ").lower()

    if len(palpite) != 5:
        print("❌ A palavra deve ter exatamente 5 letras.\n")
        continue

    if palpite not in palavras:
        print("❌ Palavra não reconhecida. Tente uma das disponíveis.\n")
        continue

    if palpite == palavra_secreta:
        print(f"{VERDE}🎉 Parabéns! Você acertou: {palavra_secreta.upper()}{RESET}")
        break

    dica = ""
    for i in range(5):
        if palpite[i] == palavra_secreta[i]:
            dica += VERDE + palpite[i].upper() + RESET + "  "
        elif palpite[i] in palavra_secreta:
            dica += AMARELO + palpite[i].upper() + RESET + "  "
        else:
            dica += CINZA + palpite[i].upper() + RESET + "  "


    print("Dica:", dica + "\n")

else:
    print(f"💀 Suas tentativas acabaram. A palavra era: {palavra_secreta.upper()}")
