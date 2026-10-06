def exibir_resultado(dados):
    print("JSON gerado com sucesso:")
    print("\n===== DADOS EXTRAÍDOS =====")
    print(f"Valor: {dados['valor']}")
    print(f"Data: {dados['data']}")
    print(f"Hora: {dados['hora']}")
    print(f"Protocolo: {dados['protocolo']}")
    print("\n===== TEXTO COMPLETO FORMATADO =====")
    print(dados["texto_formatado"])