# instalar 'deep_translator' (pip install deep_translator)
# importa a biblioteca deep_translator
from deep_translator import GoogleTranslator
import os

tradutor = GoogleTranslator(source='auto', target='pt')

if __name__ == "__main__":
    while True:
        try:
            print("1 - Traduzir texto")
            print("2 - Sair do programa")

            opcao = input("Digite a opção desejada: ")

            os.system('cls')

            match opcao:
                case "1":
                    texto_original = input("Digite o texto que deseja traduzir: ")
                    texto_traduzido = tradutor.translate(texto_original)

                    print("\nTRDUÇÃO DE TEXTO\n")
                    print(f"Tradução: {texto_traduzido}")
                    continue
                case "2":
                    break
                case _:
                    print("Opção inválida")
                    continue    
        except Exception as e:
            print(f"Não foi possível traduzir o texto.: {e}")
            continue