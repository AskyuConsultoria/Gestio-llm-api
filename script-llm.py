import sys
from langchain_ollama import OllamaLLM


sys.stdout.reconfigure(encoding='utf-8')
model = OllamaLLM(model="gemma2:2b")

def processarDados(contexto, etapa, inputUsuario):
    result = model.invoke(input=f"""
    Sou um alfaiate que produz roupas e tenho reuniões, 
    tenho também provas que são reuniões onde apresento a evolução da roupa do cliente. 
    Tenho as seguintes etapas de reuniões diferentes: {etapa}. 
    Preciso que produza um diálogo considerando os dados do meu cliente: {inputUsuario}
    """)

    print(result)

def main():
    if len(sys.argv) != 4:
        print("Uso: python meu_script.py <contexto> <etapa> <inputUsuario>")
        sys.exit(1)

    contexto = sys.argv[1]
    etapa = sys.argv[2]
    inputUsuario = sys.argv[3]

    processarDados(contexto, etapa, inputUsuario)

if __name__ == "__main__":
    main()
