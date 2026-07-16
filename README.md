# Buscador de Vagas

Um buscador automatizado de vagas de emprego construído em Python.

O objetivo deste projeto é otimizar a busca por oportunidades no mercado de tecnologia, extraindo dados reais de plataformas (como LinkedIn, Gupy e InfoJobs) através do Google Vagas (SerpApi). O sistema limpa, formata e exibe as vagas de forma eficiente direto no terminal.

## Status do Projeto
**Funcional e Integrado com IA.** A infraestrutura de busca, paginação de dados e o match automático de currículos utilizando a API do Gemini estão 100% implementados.

##  Tecnologias Utilizadas
* **Python 3**
* **Requests:** Para consumo de APIs RESTful e navegação via paginação.
* **Python-dotenv:** Para gerenciamento seguro de variáveis de ambiente e chaves.
* **SerpApi (Google Jobs):** Como fonte de extração de dados em tempo real.
* **Google Generative AI (Gemini):** Para processamento de linguagem natural e análise de currículos.

##  Como executar o projeto na sua máquina

### Pré-requisitos
* Python 3.x instalado.
* Conta gratuita na [SerpApi](https://serpapi.com/) para gerar a chave de busca.
* Conta gratuita no [Google AI Studio](https://aistudio.google.com/) para gerar a chave do Gemini.

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/lucasspap/buscadorvagas.git 
   ```
2. **Acesse o painel e instale:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure as chaves da API**
    
    Crie um arquivo .env no local do projeto e adicione sua chave da API.
    ```bash
    SERPAPI_KEY=sua_chave
    GEMINI_API_KEY=sua_chave
    ```
4. **Insira seu currículo no projeto**
    
    Dentro da pasta dados, troque o conteúdo do arquivo curriculo.txt pelo seu currículo escrito em texto puro, para facilitar o funcionamento do programa.

5. **Execute o script principal**
    ```bash
    python main.py
    ```
## Sobre o Projeto
Este projeto faz parte do meu portfólio prático de desenvolvimento com Python. Ele tem foco em automatizar e resolver um problema real de busca por oportunidades, criando uma solução eficiente.