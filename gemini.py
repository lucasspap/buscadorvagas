import os
import google.generativeai as genai

def analisar_vaga_ia(descricao_vaga, curriculo):

    chave_api = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=chave_api)

    modelo = genai.GenerativeModel("gemini-3.5-flash") #escolhendo modelo gemini

    prompt = f"""
    Aja como um recrutador de TI. Analise a vaga abaixo e o meu currículo.
    Me dê uma nota de 0 a 100 de compatibilidade e um breve resumo do porquê.
    
    VAGA:
    {descricao_vaga}
    
    CURRÍCULO:
    {curriculo}
    """

    resposta = modelo.generate_content(prompt)

    return resposta.text
