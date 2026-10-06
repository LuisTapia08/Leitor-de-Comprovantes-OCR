import cv2

def tratar_imagem(img):
    img = cv2.resize(
        img,
        None,
        fx=2.5,
        fy=2.5,
        interpolation=cv2.INTER_CUBIC
    )

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.normalize(
        gray,
        None,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX
    )

    denoise = cv2.bilateralFilter(gray, 7, 45, 45)

    clahe = cv2.createCLAHE(
        clipLimit=1.8,
        tileGridSize=(8, 8)
    )

    tratada = clahe.apply(denoise)

    blur = cv2.GaussianBlur(tratada, (0, 0), 1.0)

    tratada = cv2.addWeighted(
        tratada,
        1.5,
        blur,
        -0.5,
        0
    )
    return tratada



def limpar_texto(texto):
    texto = texto.replace("'", "")
    texto = texto.replace("YALOR", "VALOR")
    texto = texto.replace("YINCULADA", "VINCULADA")
    texto = texto.replace("COMPROYANTE", "COMPROVANTE")
    texto = texto.replace("cOMPRtVANTE", "COMPROVANTE")
    texto = texto.replace("OUYIDORIA", "OUVIDORIA")
    texto = texto.replace("DINHEiRo", "DINHEIRO")
    texto = texto.replace("DEPOSITo", "DEPOSITO")
    texto = texto.replace("GAIXA", "CAIXA")
    texto = texto.replace("CAIxA", "CAIXA")
    texto = texto.replace("LOCAL IDADE", "LOCALIDADE")

    return texto