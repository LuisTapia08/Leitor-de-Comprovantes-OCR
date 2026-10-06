import re
from src.modules.formatar_texto.main import formatar_texto_completo


def ler_texto_ocr(reader, imagem):
    resultado = reader.readtext(imagem)
    textos = []
    for item in resultado:
        texto = item[1]
        textos.append(texto)
    return "\n".join(textos)


def extrair_valor(texto):
    valor = re.search(
        r"[VY]ALOR\s*\n?\s*(\d{1,3}\s*[,\.]\s*\d{2})",
        texto,
        re.IGNORECASE
    )
    if valor:
        return valor.group(1).replace(" ", "").replace(".", ",")
    return None


def extrair_data(texto):
    data = re.search(
        r"\b\d{1,2}\s*/\s*(?:\d{1,2}|JAN|FEV|MAR|ABR|MAI|JUN|JUL|AGO|SET|OUT|NOV|DEZ)\s*/\s*\d{4}\b",
        texto,
        re.IGNORECASE
    )
    if data:
        return data.group().upper().replace(" ", "")
    return None


def extrair_hora(texto):
    hora = re.search(
        r"\d{1,2}[:;,]\d{2}[:;,]\d{1,2}",
        texto
    )
    if not hora:
        return None
    hora_texto = hora.group().replace(",", ":").replace(";", ":")
    if len(hora_texto.split(":")[-1]) == 1:
        hora_texto += hora_texto[-1]
    return hora_texto


def extrair_protocolo(texto):
    protocolo = re.search(
        r"CONTROLE[:\s]+(\d+)",
        texto,
        re.IGNORECASE
    )
    if protocolo:
        return protocolo.group(1)
    return None



def extrair_dados(texto):
    dados = {
        "valor": extrair_valor(texto),
        "data": extrair_data(texto),
        "hora": extrair_hora(texto),
        "protocolo": extrair_protocolo(texto),
        "texto_completo": texto,
        "texto_formatado": formatar_texto_completo(texto)
    }
    return dados