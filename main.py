import os
import requests
from dotenv import load_dotenv

load_dotenv() #carregar arquivo .env com apikeys

def ler_curriculo_local(caminho):  #ler curriculo na pasta
    try: 
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Currículo não foi encontrado"
    
def buscar_vagas(termo, local, paginas=1):
    
    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        return "Chave API não foi encontrada"
    
    vagas_totais= []

    for pagina in range(paginas):  #paginação de 10 em 10
        i_result = pagina * 10
        print(f"Buscando no Google Jobs: '{termo} {local}' (Página {pagina + 1})...")
        
        url = "https://serpapi.com/search.json"
        
        parametros = {
            "engine": "google_jobs",
            "q": f"{termo} {local}",
            "hl": "pt",               
            "gl": "br",               
            "start": i_result, # paginação 10 em 10
            "api_key": api_key
        }
        
        try:
            resposta = requests.get(url, params=parametros)
            
            if resposta.status_code == 200:
                dados = resposta.json()
                result_pagina = dados.get("jobs_results", [])
                
                if not result_pagina:
                    print("Aviso: Não há mais vagas nesta página. Parando a busca.")
                    break
                    
                vagas_totais.extend(result_pagina)
            else:
                print(f"Erro na API do Google. Código: {resposta.status_code}")
                break
                
        except Exception as e:
            print(f"Ocorreu um erro de conexão: {e}")
            break
            
    return vagas_totais
    
if __name__ == "__main__":
    print("INICIANDO PROCURA DE VAGAS NO GOOGLE JOBS")

    caminho_cv = os.path.join("dados", "curriculo.txt")  #carregar curriculo
    conteudo_cv = ler_curriculo_local(caminho_cv)
    print(f"\n Currículo foi carregado com ({len(conteudo_cv)} caracteres)")

    termos_busca = ["Estágio TI", "Estágio Dados"]
    lista_vagas = []     #pode-se usar vários termos, cada termo buscará 1 página de vagas

    for termo in termos_busca:
        vagas_encontradas = buscar_vagas(termo=termo, local="Campinas", paginas=1)

        lista_vagas.extend(vagas_encontradas)

    print(f"\n Fim da busca. Vagas encontradas: {len(lista_vagas)}")

    if lista_vagas:
        for i, vaga in enumerate(lista_vagas, 1):
            titulo = vaga.get("title", "Título não informado")
            empresa = vaga.get("company_name", "Empresa Confidencial")
            plataforma = vaga.get("via", "Desconhecida")
            
            opcoes_candidatura = vaga.get("apply_options", []) #procurar botões pra realizar candidatura
            if opcoes_candidatura:
                link = opcoes_candidatura[0].get("link", "Link indisponível")
            else:
                link = vaga.get("share_link", "Link indisponível")  
            
            descricao_bruta = vaga.get("description", "Sem descrição disponível.")
            descricao_limpa = " ".join(str(descricao_bruta).split())    #remove espaços em branco e quebras de linha desnecessárias
            
            print(f"[{i}] VAGA: {titulo}")
            print(f"    Empresa: {empresa} (via {plataforma})")
            print(f"    Resumo: {descricao_limpa[:200]}...")
            print(f"    Link: {link}")

    else:
        print("[AVISO] Nenhuma vaga foi encontrada ou erro nas chaves.")
        