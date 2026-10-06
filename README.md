# Leitor de Comprovante

Este projeto em Python realiza a leitura automática de um comprovante de pagamento por meio de OCR (Reconhecimento Óptico de Caracteres) e extrai informações relevantes como valor, data, hora e protocolo.

Ele foi desenvolvido para processar imagens do tipo comprovante, melhorar a qualidade visual da imagem, reconhecer os textos e organizar os dados em um arquivo JSON para uso posterior.

## Objetivo

Automatizar a extração de dados de imagens de comprovantes, reduzindo a necessidade de digitação manual. O fluxo principal do projeto é:

1. Carregar a imagem;
2. Tratá-la para melhorar a qualidade visual;
3. Ler o texto com OCR;
4. Limpar e normalizar o texto;
5. Extrair os campos principais;
6. Salvar os resultados em JSON;
7. Exibir os dados extraídos no terminal.

## Funcionalidades

- Leitura de imagem com OpenCV;
- Pré-processamento da imagem para melhorar o OCR;
- Reconhecimento de texto em português com EasyOCR;
- Extração dos campos:
  - valor;
  - data;
  - hora;
  - protocolo;
- Ajuste/limpeza do texto extraído;
- Formatação do texto completo;
- Exportação dos resultados em JSON;
- Apresentação dos dados no console.

## Stack tecnológica

- Python 3
- OpenCV (`cv2`)
- EasyOCR
- Regex para extração de dados
- JSON para persistência

## Estrutura do projeto

```text
LEITOR_DE_COMPROVANTE/
├── main.py
├── README.md
├── imagem_tratada.png
├── resultado_ocr.json
├── assets/
│   └── payment.png
├── src/
│   └── modules/
│       ├── carregar_imagem/
│       │   └── main.py
│       ├── extrair_dados/
│       │   └── main.py
│       ├── formatar_texto/
│       │   └── main.py
│       ├── resultados/
│       │   └── main.py
│       ├── salvar_json/
│       │   └── main.py
│       └── tratamento/
│           └── main.py
└── venv/
```

## Como o projeto funciona

### 1. Carga da imagem

O módulo `carregar_imagem` usa OpenCV para abrir a imagem do comprovante.

Se o arquivo não existir, a aplicação gera uma exceção do tipo `FileNotFoundError`.

### 2. Tratamento da imagem

No módulo `tratamento`, a imagem passa por várias etapas para melhorar a leitura do OCR:

- redimensionamento;
- conversão para escala de cinza;
- normalização dos valores de pixel;
- filtro bilateral;
- equalização de contraste com CLAHE;
- suavização com blur;
- ajuste final da imagem.

Essa etapa é importante porque comprovantes muitas vezes apresentam ruído, baixa qualidade de imagem ou contraste insuficiente.

### 3. OCR

No arquivo principal, a aplicação cria um leitor EasyOCR em português:

```python
reader = easyocr.Reader(["pt"], gpu=False)
```

Em seguida, o texto da imagem tratada é lido e convertido em uma string com quebras de linha.

### 4. Limpeza do texto

A função `limpar_texto()` corrige distorções comuns geradas pelo OCR, como:

- substituição de letras parecidas;
- remoção de aspas ou caracteres estranhos;
- normalização de termos como "VALOR", "COMPROVANTE" e "CAIXA".

### 5. Extração dos dados

O módulo `extrair_dados` usa expressões regulares para localizar e capturar:

- `valor`: valor monetário;
- `data`: data do documento;
- `hora`: horário identificado;
- `protocolo`: número de controle do comprovante;
- `texto_completo`: texto bruto extraído;
- `texto_formatado`: texto limpo e organizado.

### 6. Salvar e exibir

Depois da extração, os dados são gravados em `resultado_ocr.json` e exibidos no console.

## Requisitos

Antes de executar o projeto, verifique se você tem instalado:

- Python 3.9+
- pip
- ambiente virtual (recomendado)

## Instalação com venv

A seguir estão os passos para configurar o ambiente do projeto em um ambiente virtual.

### 1. Clone ou acesse o projeto

```bash
cd C:\caminho\para\LEITOR_DE_COMPROVANTE
```

### 2. Crie o ambiente virtual

No Windows, PowerShell:

```powershell
python -m venv venv
```

### 3. Ative o ambiente virtual

```powershell
venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a execução por política de script, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```bash
pip install --upgrade pip
pip install opencv-python easyocr
```

Também é possível instalar as dependências a partir do arquivo `requirements.txt` gerado no projeto:

```bash
pip install -r requirements.txt
```

## Como executar

Na raiz do projeto, após ativar o ambiente virtual, execute:

```bash
python main.py
```

O programa utiliza a imagem padrão:

```text
assets/payment.png
```

Se a imagem estiver no caminho correto, o projeto gerará:

- `imagem_tratada.png`
- `resultado_ocr.json`

## Arquivos principais

### `main.py`

Este é o ponto de entrada da aplicação. Ele coordena o fluxo completo:

- carrega imagem;
- trata a imagem;
- extrai texto com OCR;
- converte dados;
- salva JSON;
- imprime resultado.

### `src/modules/carregar_imagem/main.py`

Responsável pela leitura da imagem usando OpenCV.

### `src/modules/tratamento/main.py`

Responsável pela melhoria da imagem para facilitar a leitura do OCR.

### `src/modules/extrair_dados/main.py`

Responsável pela extração dos campos principais por meio de regex.

### `src/modules/formatar_texto/main.py`

Responsável por limpar e formatar o texto extraído.

### `src/modules/salvar_json/main.py`

Responsável por persistir os dados em arquivo JSON.

### `src/modules/resultados/main.py`

Responsável por exibir os dados extraídos no terminal.

## Exemplo de saída

O programa gera uma estrutura semelhante a esta no JSON:

```json
{
  "valor": "R$ 1.234,56",
  "data": "10/ABR/2024",
  "hora": "10:30:45",
  "protocolo": "123456",
  "texto_completo": "...",
  "texto_formatado": "..."
}
```

A saída no console também mostra os principais campos extraídos.

## Observações importantes

- O resultado de OCR depende muito da qualidade da imagem;
- Imagens com baixa resolução, sombras ou distorções podem reduzir a precisão;
- A aplicação foi pensada para um cenário específico de comprovante e pode precisar de ajustes para outros layouts;
- A normalização das expressões regulares é essencial para melhorar a consistência da extração;
- O projeto é uma base sólida para evoluir com classificação de documentos, validação de campos e melhoria da leitura em múltiplos formatos.

## Possíveis melhorias futuras

- suporte a múltiplos tipos de comprovante;
- validação de campos antes de salvar o JSON;
- interface gráfica com Tkinter ou Streamlit;
- processamento em lote de várias imagens;
- persistência em banco de dados;
- melhor tratamento para layouts mais complexos.

## Conclusão

Este projeto demonstra uma pipeline simples e funcional de OCR para extração de dados de comprovantes. A arquitetura modular facilita a manutenção, testes e futuras expansões, tornando o código organizado e mais fácil de evoluir.
