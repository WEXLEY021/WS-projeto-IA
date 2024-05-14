import random
import datetime

class AssistenteIA:
    def cumprimentar(self):
        saudacoes = ["Olá! Como posso ajudar você hoje?", "Oi! Estou aqui para ajudar. O que você precisa?", "Olá! Em que posso ser útil?"]
        return random.choice(saudacoes)

    def obter_data_hora_atual(self):
        agora = datetime.datetime.now()
        return agora.strftime("Hoje é %d/%m/%Y e são %H:%M.")

    def contar_piada(self):
        piadas = [
            "Por que o pombo não pode ser contador? Porque ele sempre arredonda pra baixo.",
            "O que o pato disse para a pata? Vem quá!",
            "Por que o elétron foi preso? Porque roubou um próton.",
            "Por que o livro de matemática ficou de castigo? Porque só fazia problemas."
        ]
        return random.choice(piadas)

if __name__ == "__main__":
    assistente = AssistenteIA()
    print(assistente.cumprimentar())

    while True:
        comando = input("Como posso ajudar você? (Digite 'sair' para encerrar) ").lower()

        if "data" in comando:
            print(assistente.obter_data_hora_atual())
        elif "piada" in comando:
            print(assistente.contar_piada())
        elif "sair" in comando:
            print("Até mais!")
            break
        else:
            print("Desculpe, não entendi. Você pode repetir?")

