# Calculadora de notas
# Projeto da faculdade (Anhanguera, 2025) - roda no terminal
# Calcula a média das notas e diz se o aluno está aprovado, em recuperação ou reprovado


def ler_nota(mensagem):
    """Lê uma nota entre 0 e 10, repetindo até o valor ser válido."""
    while True:
        try:
            # replace troca vírgula por ponto, assim o usuário pode digitar 6,5
            nota = float(input(mensagem).replace(",", "."))
        except ValueError:
            # float() dá erro (ValueError) se o texto não for um número
            print("Digite um número válido.")
            continue  # volta ao início do while e pergunta de novo

        # só aceita notas dentro do intervalo de 0 a 10
        if 0 <= nota <= 10:
            return nota
        print("A nota deve estar entre 0 e 10.")


def ler_quantidade(mensagem):
    """Lê um número inteiro maior que zero, repetindo até ser válido."""
    while True:
        try:
            quantidade = int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")
            continue
        if quantidade > 0:
            return quantidade
        print("A quantidade deve ser maior que zero.")


# pergunta quantas notas serão informadas (3 trimestres, 4 provas, etc.)
quantidade = ler_quantidade("Quantas notas deseja informar? ")

# cria uma lista com todas as notas, uma pergunta para cada nota
notas = [ler_nota(f"Digite a nota {i}: ") for i in range(1, quantidade + 1)]

# média = soma das notas dividida pela quantidade de notas
media = sum(notas) / len(notas)

# define a situação (ajuste os valores 7 e 5 para a regra da sua faculdade)
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# mostra o resultado com uma casa decimal
print(f"Sua média é {media:.1f}. Situação: {situacao}")
