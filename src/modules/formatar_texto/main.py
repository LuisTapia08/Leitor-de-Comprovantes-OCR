import re

def formatar_texto_completo(texto):
    linhas = texto.splitlines()
    linhas_limpas = []

    for linha in linhas:
        linha = linha.strip()

        if not linha:
            continue

        if len(linha) <= 2:
            continue

        linha = re.sub(r"\s+", " ", linha)

        linha = re.sub(
            r"(\d{1,2})/\s*([A-Z]{3})/\s*(\d{4})",
            r"\1/\2/\3",
            linha,
            flags=re.IGNORECASE
        )

        linha = re.sub(
            r"(\d+)\s*,\s*(\d{2})",
            r"\1,\2",
            linha
        )

        linhas_limpas.append(linha)

    return "\n".join(linhas_limpas)