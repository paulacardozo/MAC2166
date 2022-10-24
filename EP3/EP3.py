"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Paula Cardozo da Silva
  NUSP : 8803299
  Turma: 06
  Prof.: Daniel Macedo Batista

  Referências: 
  
  - Mat (gera_grafico_simples(cSIR)) e Mat2 (gera_grafico_composto(S, I, R)) 
  foram baseados na função cria_matriz apresentada em
  https://www.ime.usp.br/~mac2166/1s20/index.html#aula13
  
  - As leituras dos arquivos PGM (gera_grafico_simples(cSIR)) e PPM ((gera_grafico_composto(S, I, R))) foram 
  baseadas na função grava_PGM(M) apresentada em
  https://www.ime.usp.br/~mac2166/1s20/index.html#aula17
  
  - A leitura do nome_de_arquivo (leitura_de_valores(nome_de_arquivo)) foi baseada nos exemplos
  apresentados em
  https://www.ime.usp.br/~mac2166/1s20/index.html#aula17
  
"""
import math


def SIR (N, Beta, Gama, Tmax) :
    
    """Devolve três listas contendo Tmax elementos, correspondendo às variáveis S, I, R 
    em cada instante de tempo da lista. Sendo T = (Tmax - 1)"""
    
    So = N - 1
    Io = 1
    Ro = 0
    S = [So]
    I = [Io]
    R = [Ro]
    
    c = 0
    while Tmax-1 > c:
        Si = S[len(S)-1] - Beta*((S[len(S)-1]*I[len(I)-1])/N)
        
        Ii = I[len(I)-1] + Beta*((S[len(S)-1]*I[len(I)-1])/N) - Gama*(I[len(I)-1])
            

        Ri = R[len(R)-1] + Gama*(I[len(I)-1])
        
        S.append(Si)
        I.append(Ii)
        R.append(Ri)
        c += 1
            
    return S, I, R

def critic_SIR (N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta):
    """Devolve uma lista de valores máximos de I obtidos a partir dos valores Beta de BetaW"""
 
    BetaW = []
    IMax = []
    Bw = Beta_MIN
    w = 0
    while Bw < Beta_MAX:
        Bw = Beta_MIN + w*Beta_delta
        BetaW.append(Bw)
        w += 1
    
    for Beta in BetaW:
        S, I, R = SIR(N, Beta, Gama, Tmax)
    
        maxi = I[0]        
        #Retorno do valor máximo:
        for e in I:
            if e > maxi:
                maxi = e
            
        IMax.append(maxi)
            
    return IMax

def gera_grafico_simples(L):
   
    """Recebe como parâmetro uma lista L e devolve uma matriz com seus valores padronizados 
    (255) e um gráfico PGM"""

    #Determinando os limites
    X_Max = len(L) - 1
    #Y_Max é o teto do valor máximo de L
    maxi2 = L[0]        
    #Retorno do valor máximo:
    for e2 in L:
        if e2 > maxi2:
            maxi2 = e2  
    Y_Max = round(maxi2)
        
    #Ajustando Y_Max
    if Y_Max < maxi2:
        Y_Max += 1
        
    #De X_Min = 0 e Y_Min = 0:
    k = 0
    
    
    #Seja a matriz Mat[i][j] com valores iguais à zero
    #m = linhas, n = colunas
    m = Y_Max + 1
    n = len(L)
    
    Mat = []
    for i in range(m):
        l = []
        for j in range(n):
            l.append(0)
        
        Mat.append(l)
    
    #Atribuindo 255 aos pontos que possuem valores contidos em L
    while k <= len(L) - 1:
        Mat[round(Y_Max - L[k])][k] = 255
        k += 1
        
    #Leitura PGM    
    arquivo = open("graf_simples.pgm", 'w')
    arquivo.write("P2\n")
    m = len(Mat)
    n = len(Mat[0])
    arquivo.write("%d %d\n"%(n,m))
    arquivo.write("255\n")
    for i in range(m):
        for j in range(n):
            arquivo.write(" %3d"%(Mat[i][j]))
        arquivo.write("\n")
    arquivo.close()

           
    return Mat

def gera_grafico_composto(S, I, R):
    
    """Recebe como parâmetro três listas, S, I e R, e devolve uma matriz com seus valores 
    padronizados (255) e um gráfico PPM"""
    
    #Determinando os limites:
    X_Max = len(S) - 1 
    
    #Y_Max é o teto do valor máximo da concatenação de S, I, R
    
    Y = S + I + R
    maxi3 = Y[0]        
    #Retorno do valor máximo:
    for e3 in Y:
        if e3 > maxi3:
            maxi3 = e3  
    Y_Max = round(maxi3)
    #Ajustando Y_Max:
    if Y_Max < maxi3:
        Y_Max += 1
        
    #De X_Min = 0 e Y_Min = 0:
    u = 0

    
    #Seja a matriz Mat2[i][j] com valores iguais à zero
    #m2 = linhas, n2 = colunas
    m2 = Y_Max
    n2 = 3*len(S)
    
    Mat2 = []
    for i in range(m2 + 1):
        l = []
        for j in range(n2):
            l.append(0)
        
        Mat2.append(l)
        
    #Atribuindo 255 aos pontos que possuem valores contidos em S, I, R
    while u <= X_Max:
        Mat2[round(m2 - S[u])][3*u] = 255
        Mat2[round(m2 - I[u])][3*u + 1] = 255
        Mat2[round(m2 - R[u])][3*u + 2] = 255
        u += 1
        
    #Leitura PPM
    arquivo = open("graf_composto.ppm", 'w')
    arquivo.write("P3\n")
    m2 = len(Mat2)
    n2 = len(Mat2[0])
    arquivo.write("%d %d\n"%(n2//3,m2))
    arquivo.write("255\n")
    for i in range(m2):
        for j in range(n2):
            arquivo.write(" %3d"%(Mat2[i][j]))
        arquivo.write("\n")
    arquivo.close()
    
        
    return Mat2


def leitura_de_valores(nome_de_arquivo):
    """Devolve variáveis N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta a partir da leitura de um arquivo"""

    
    texto = open(nome_de_arquivo, 'r')
    
    N = texto.readline()
    Gama = texto.readline()
    Tmax = texto.readline()
    Beta_MIN = texto.readline()
    Beta_MAX = texto.readline()
    Beta_Delta = texto.readline()
    
    N = int(N)
    Gama = float(Gama)
    Tmax = int(Tmax)
    Beta_MIN = float(Beta_MIN)
    Beta_MAX = float(Beta_MAX)
    Beta_Delta = float(Beta_Delta)
    
    texto.close()
    
    return N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_Delta


            
            
# Opções
# 1: Calcular 'SIR' e imprimir os vetores S, I e R - leitura de teclado
# 2: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de teclado
# 3: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de arquivo
# 4: Calcular 'critic_SIR', testar matriz devolvida por 'gera_grafico_simples' - leitura de teclado
# 5: Calcular 'critic_SIR', testar arquivo PGM no disco por 'gera_grafico_simples' - leitura de teclado
# 6: Calcular 'SIR', testar matriz devolvida por 'gera_grafico_composto' - leitura de teclado
# 7: Calcular 'SIR', testar arquivo PPM no disco por 'gera_grafico_composto' - leitura de teclado

#Não altere as funções abaixo:
def imprimeLista(L) : 
    for i in range(len(L)):
      print("%.4f " % L[i], end=""); # usar apenas 4 digitos apos ponto
    print()

def main():
    Opt = int(input("Digite modo do programa: "))
    if (Opt == 1): # saida - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        print("S = ", end="")
        imprimeLista(S) 
        print("I = ", end="")
        imprimeLista(I)
        print("R = ", end="")
        imprimeLista(R)
    elif (Opt == 2): # saida - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 3): # saida - critic_SIR; entrada - arquivo
        Dados = input("Digite nome do arquivo: "); 
        N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leitura_de_valores(Dados)
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 4): # grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        print(M_grafico)
    elif (Opt == 5): # PGM - grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        g = open("graf_simples.pgm", "r")
        print(g.read())
        g.close()
    elif (Opt == 6): # grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        print(M_grafico)
    elif (Opt == 7): # PPM - grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        g = open("graf_composto.ppm", "r")
        print(g.read())
        g.close()

main()