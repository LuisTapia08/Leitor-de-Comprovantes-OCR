from src.modules.salvar_json.main import salvar_json
from src.modules.tratamento.main import tratar_imagem, limpar_texto
from src.modules.extrair_dados.main import extrair_data, extrair_hora, extrair_protocolo, extrair_valor, extrair_dados, ler_texto_ocr
from src.modules.carregar_imagem.main import carregar_imagem
from src.modules.resultados.main import exibir_resultado
import easyocr
import cv2

CAMINHO_IMAGEM = "assets/payment.png"
CAMINHO_IMAGEM_TRATADA = "imagem_tratada.png"
CAMINHO_JSON = "resultado_ocr.json"


def main():
    reader = easyocr.Reader(["pt"], gpu=False)
    img = carregar_imagem(CAMINHO_IMAGEM)
    imagem_tratada = tratar_imagem(img)
    cv2.imwrite(CAMINHO_IMAGEM_TRATADA, imagem_tratada)
    texto_completo = ler_texto_ocr(reader, imagem_tratada)
    texto_limpo = limpar_texto(texto_completo)
    dados = extrair_dados(texto_limpo)
    salvar_json(dados, CAMINHO_JSON)
    exibir_resultado(dados)


if __name__ == "__main__":
    main()