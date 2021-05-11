def contar_caracteres(s):
    """
        Descricao da Funcao 
    """
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    
    return resultado

if __name__ == "__main__":
    print(contar_caracteres('walter'))
    print()
    print(contar_caracteres('banana'))
