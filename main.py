# Projeto Final: Quiz de Conhecimentos em Python
# Aluno: Gerson Junior
# Curso: Análise e Desenvolvimento de Sistemas - SENAC-DF

import random


perguntas = {
    1: {
        "id": 1,
        "enunciado": "Qual é a capital do Brasil?",
        "alternativas": ["São Paulo", "Brasília", "Rio de Janeiro", "Salvador"],
        "resposta_correta": 2
    },
    2: {
        "id": 2,
        "enunciado": "Quantos planetas existem no Sistema Solar?",
        "alternativas": ["7", "9", "8", "10"],
        "resposta_correta": 3
    },
    3: {
        "id": 3,
        "enunciado": "Qual é o maior oceano do planeta?",
        "alternativas": ["Atlântico", "Índico", "Ártico", "Pacífico"],
        "resposta_correta": 4
    },
    4: {
        "id": 4,
        "enunciado": "Quem escreveu Dom Casmurro?",
        "alternativas": ["Machado de Assis", "José de Alencar", "Clarice Lispector", "Carlos Drummond de Andrade"],
        "resposta_correta": 1
    },
    5: {
        "id": 5,
        "enunciado": "Quanto é 12 x 8?",
        "alternativas": ["88", "96", "108", "120"],
        "resposta_correta": 2
    },
    6: {
        "id": 6,
        "enunciado": "Em que ano foi proclamada a Independência do Brasil?",
        "alternativas": ["1889", "1500", "1822", "1922"],
        "resposta_correta": 3
    },
    7: {
        "id": 7,
        "enunciado": "Qual elemento químico é representado pela letra O?",
        "alternativas": ["Ouro", "Oxigênio", "Ósmio", "Prata"],
        "resposta_correta": 2
    },
    8: {
        "id": 8,
        "enunciado": "Qual destes mamíferos põe ovos?",
        "alternativas": ["Leão", "Golfinho", "Ornitorrinco", "Cavalo"],
        "resposta_correta": 3
    },
    9: {
        "id": 9,
        "enunciado": "Qual é o menor número primo?",
        "alternativas": ["1", "3", "0", "2"],
        "resposta_correta": 4
    },
    10: {
        "id": 10,
        "enunciado": "Qual civilização construiu Machu Picchu?",
        "alternativas": ["Maia", "Inca", "Asteca", "Egípcia"],
        "resposta_correta": 2
    }
}

LETRAS = ("a", "b", "c", "d")
PERGUNTAS_POR_PARTIDA = (5, 10)


def exibir_boas_vindas():
    print("=" * 50)
    print("       QUIZ DE CONHECIMENTOS GERAIS")
    print("=" * 50)
    print("Responda com a, b, c, d ou com o número da alternativa.")
    print("A cada resposta você verá seu resultado. Boa sorte!")
    print("=" * 50)


def obter_nome():
    while True:
        nome = input("Como podemos chamar você? ").strip()
        if nome:
            return nome
        print("Digite seu nome ou um apelido para continuar.")


def obter_quantidade_perguntas():
    opcoes = " ou ".join(str(opcao) for opcao in PERGUNTAS_POR_PARTIDA)
    while True:
        escolha = input(
            f"Quantas perguntas quer responder? ({opcoes}; "
            f"Enter para {PERGUNTAS_POR_PARTIDA[0]}): "
        ).strip()
        if not escolha:
            return PERGUNTAS_POR_PARTIDA[0]
        if escolha.isdigit() and int(escolha) in PERGUNTAS_POR_PARTIDA:
            return int(escolha)
        print(f"Escolha {opcoes} perguntas.")


def exibir_pergunta(pergunta, numero, total):
    respondidas = numero - 1
    barra = "#" * respondidas + "-" * (total - respondidas)
    print(f"\n[{barra}] Pergunta {numero}/{total}")
    print(pergunta["enunciado"])

    for letra, alternativa in zip(LETRAS, pergunta["alternativas"]):
        print(f"  {letra}) {alternativa}")


def obter_resposta():
    while True:
        resposta = input("Sua resposta (a/b/c/d ou 1/2/3/4): ").strip().lower()
        if resposta in LETRAS:
            return LETRAS.index(resposta) + 1
        if resposta in ("1", "2", "3", "4"):
            return int(resposta)
        print("Resposta inválida. Digite a, b, c, d ou um número de 1 a 4.")


def verificar_resposta(pergunta, resposta):
    return resposta == pergunta["resposta_correta"]


def exibir_resultado(nome, acertos, total):
    erros = total - acertos
    percentual = acertos / total * 100

    print("\n" + "=" * 50)
    print(f"             RESULTADO DE {nome.upper()}")
    print("=" * 50)
    print(f"Respostas corretas: {acertos}")
    print(f"Respostas incorretas: {erros}")
    print(f"Pontuação final: {acertos}/{total} ({percentual:.0f}%)")

    if acertos == total:
        print("Incrível! Você gabaritou. Mestre do conhecimento!")
    elif percentual >= 60:
        print("Muito bem! Você mandou bem demais.")
    else:
        print("Boa! Cada partida é uma chance de aprender e superar seu recorde.")
    print("=" * 50)


def executar_quiz(nome, total):
    acertos = 0
    perguntas_sorteadas = random.sample(list(perguntas.values()), total)

    for numero, pergunta in enumerate(perguntas_sorteadas, start=1):
        exibir_pergunta(pergunta, numero, total)
        resposta = obter_resposta()

        if verificar_resposta(pergunta, resposta):
            print("Acertou! +1 ponto.")
            acertos += 1
        else:
            indice_correto = pergunta["resposta_correta"] - 1
            resposta_correta = pergunta["alternativas"][indice_correto]
            print(f"Quase! A resposta certa era: {resposta_correta}.")

    exibir_resultado(nome, acertos, total)


def jogar_novamente():
    while True:
        resposta = input("\nQuer jogar outra partida? (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "não", "nao"):
            return False
        print("Digite s para jogar novamente ou n para sair.")


def main():
    exibir_boas_vindas()
    nome = obter_nome()
    total = obter_quantidade_perguntas()

    while True:
        executar_quiz(nome, total)
        if not jogar_novamente():
            print(f"\nValeu por jogar, {nome}! Até a próxima.")
            break


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\n\nJogo encerrado. Até a próxima!")
