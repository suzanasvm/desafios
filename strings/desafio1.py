import re,textwrap


################### DESAFIO PARTE 1 - LIMITA O TEXTO A X CARACTERES POR LINHA ################################################## 
def cutText(text,textSize):
	#Limita o texto a textSize caracteres por linha
	formated_text = '\n'.join(textwrap.wrap(text, textSize))
	return formated_text


################### DESAFIO PARTE 2 - JUSTIFICA O TEXTO  ######################################################################## 
def countItens(l):
    return sum([ len(x) for x in l] )

lead_re = re.compile(r'(^\s+)(.*)$')

def alinhaTexto(text, larguraLinha, ultimaLinhaParagrafo=0):
    m = lead_re.match(text)    
    if m is None:
        esquerda, direita, largura = '', text, larguraLinha
    else:
        esquerda, direita, largura = m.group(1), m.group(2), larguraLinha - len(m.group(1))
    itens = direita.split()
    for i in range(len(itens) - 1): # add required space to each words, exclude last item
        itens[i] += ' '
    if not ultimaLinhaParagrafo: # number of spaces to add
        ContaEsquerda = largura - countItens(itens)
        while ContaEsquerda > 0 and len(itens) > 1:
            for i in range(len(itens) - 1):
                itens[i] += ' '
                ContaEsquerda -= 1
                if ContaEsquerda < 1:  
                    break
    resultado = esquerda + ''.join(itens)
    return resultado

def justify(text, larguraLinha):
    palavras = text.split()
    totalPalavras = len(palavras)
    espacoVazio = [[0] * totalPalavras for i in range(totalPalavras)]
    for i in range(totalPalavras):
        espacoVazio[i][i] = larguraLinha - len(palavras[i])
        for j in range(i + 1, totalPalavras):
            espacoVazio[i][j] = espacoVazio[i][j - 1] - len(palavras[j]) - 1
    minima = [0] + [10 ** 20] * totalPalavras
    quebras = [0] * totalPalavras
    for j in range(totalPalavras):
        i = j
        while i >= 0:
            if espacoVazio[i][j] < 0:
                custo = 10 ** 10
            else:
                custo = minima[i] + espacoVazio[i][j] ** 2
            if minima[j + 1] > custo:
                minima[j + 1] = custo
                quebras[j] = i
            i -= 1
    linhas = []
    j = totalPalavras
    while j > 0:
        i = quebras[j - 1]
        linhas.append(' '.join(palavras[i:j]))
        j = i
    linhas.reverse()
    for linha in linhas:
        print alinhaTexto(linha, larguraLinha, ultimaLinhaParagrafo=0)


################### Define the inputs  ##########################################################################################
textSize=40
text = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n\n\n And God said, \"Let there be light,\" and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light \"day,\" and the darkness he called \"night.\" And there was evening, and there was morning - the first day."

################### Call the functions and print  ##########################################################################################

print("Original Text: \n"+text)
print("\nLimit of characters: "+ str(textSize))
limitedText = cutText(text,textSize)
print("\nText with limit of characters: \n"+limitedText)
print("\nJustify text: \n")
justify(limitedText, textSize)







