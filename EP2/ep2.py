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


"""

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente  neste bloco as funções obrigatórias do EP2.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================
def polinomioComRaiz(p,b):
    """Devolve True se b é raiz do polinômio representado pela lista p, 
       ou False no caso contrário.
       
       p -- a lista dos coeficientes do polinômio       
       b -- o número a ser testado como raiz
    """
    
    # poli é uma "substituição" de um b genérico no polinômio
    
    poli = 0
    for i in range (len(p)):
        poli += p[i]*b**i 
        
       
    if poli == 0:
        Raiz = True
    else:
        Raiz = False
            
    return Raiz
        

# ======================================================================

def polinomioQuociente(p,b):
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(x-b), onde p(x) é o polinômio cujos coeficientes estão na 
       lista p e b é uma raiz de p(x). 
       
       p -- a lista dos coeficientes do polinômio a ser dividido      
       b -- a raiz a ser usada como divisor
    """
    
    
    #aplicando briot-ruffini, a lista começa com o termo que possui maior grau
    #briot são as "etapas" do briot-ruffini e essas etapas são efetuadas até
    #o termo independente ser alcançado


    quo = [int(p[len(p)-1])]

    i = 2
    while len(p)-i > 0:
        briot = quo[len(quo)-1]*b + p[len(p)-i]
        quo.append(int(briot))
        i += 1
    
    quo.reverse()
    return quo
    
    

# ======================================================================
def listaCanonicaDeRaizes(p):
    """Devolve a lista canônica de raízes inteiras do polinômio 
       representado pela lista p.
       
       p -- a lista dos coeficientes do polinômios
    """

    
    #Pelo teorema das raízes racionais, toda raiz inteira de p(x) é um divisor 
    #do termo independente 
    #ou seja, a raiz inteira divide p[0]

    
    div = []
    raizes = []
    
    #caso o termo independente seja zero
    
    while p[0] == 0:
        raizes.append(0)
        p = polinomioQuociente(p,p[0])
        
    #lista de divisores do termo independente 
    i = 1
    indep = p[0]
    if indep <0:
        indep = -indep

    while indep >= i:
        d = indep % i
      
        if d == 0:
            div.append(-i)
            div.append(i)
            
        i += 1
            
    #verificando se o divisor do termo independente é raiz
    for divisores in div:
        r = polinomioComRaiz(p,divisores)
        
        while polinomioComRaiz(p,divisores) == True:
            raizes.append(divisores)
            p = polinomioQuociente(p,divisores)

            
    return raizes    

    


# ======================================================================
def polinomioQuocienteRacional(p,b,a):
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(ax-b) e o resto dessa divisão, onde p(x) é o polinômio 
       cujos coeficientes estão na lista p e b/a é uma raiz de p(x). 
       
       p -- a lista dos coeficientes do polinômio a ser dividido
       b -- numerador da raiz a ser usada como divisor
       a -- denominador da raiz a ser usada como divisor
    """
    
    quo2 = [int(p[len(p)-1])]
    quof2 = []
    i = 2
    
    if len(p) <= 1:
        quof2 = None
        rest = -1
        
    else:
        while len(p)-i > 0:
            briot = quo2[len(quo2)-1]*b/a + p[len(p)-i]
            quo2.append(int(briot))
            i += 1
        
    
        rest = quo2[len(quo2)-1]*b/a + p[0]

        
        for c in quo2:
            d = c/a
            quof2.append(int(d))

   

        quof2.reverse()

    return quof2, rest       

    
# ======================================================================
def listaRaizesRacionais(p):
    """Devolve a lista canônica de raízes racionais do polinômio 
       representado pela lista p.
       
       p -- a lista dos coeficientes do polinômio
    """
    
    # a raiz racional é b/a, sendo 'b' divisor de p0 e 'a' divisor 
    #de p[len(p)-1]
    # raizes2 são os divisores b/a confirmados
    
    raizes2 = []
    pb = []
    pa = []
    
    #pensando nos divisores de p0, ou seja, b
    
    #caso o termo independente seja zero
    
    while p[0] == 0:
        raizes2.append(0)
        p = polinomioQuociente(p,p[0])
        
    #lista de divisores de p0
    i = 1
    indep2 = p[0]
    if indep2 <0:
        indep2 = -indep2

    while indep2 >= i:
        d = indep2 % i
      
        if d == 0:
            pb.append(-i)
            pb.append(i)
            
        i += 1
    
    #pensando nos divisores de p(len(p)-1), ou seja, a
    j = 1
    while p[len(p)-1] >= j:
        d2 = p[len(p)-1] % j
        
        if d2 == 0:
            pa.append(j)
            
        j += 1
        
        
    k = 0
    #preparando os parâmetros de polinomioQuocienteRacional
    while k < len(pa):
        a = pa[k]
        k += 1
        
        w = 0
        while w < len(pb):
            b = pb[w]
            
            quof2,rest = polinomioQuocienteRacional(p,b,a)

            
            #teste da raiz 
            if rest == 0:
                raizes2.append(b/a)
                p = quof2
                
            else:
                w+=1   
    
    return raizes2


# ======================================================================
def racionalToString(pn,r):
    """Devolve uma string que apresenta a raiz r do polinômio do qual pn 
       é o coeficiente de maior grau como:
        - um inteiro, caso r seja inteiro
        - na forma b/a, com b e a primos entre si e a > 0, caso contrário

       pn -- coeficiente de maior grau do polinômio
       r -- uma raiz do polinômio
    """

    div = []
    #testando r
    if r == int(r):
        raiz = str(int(r))
        
    else:
        #r não é inteiro
        #calculando mdc
        i = 1
        n = round(r*pn)
        d = pn
        if n < 0:
            n = -n
        if d < 0:
            d = - d
        while d >= i and n >= i:
            n1 = n % i
            d1 = d % i
            if n1 == 0 and d1 == 0:
                div.append(i)
            
            i += 1
    

        mdc = div[len(div)-1]

    #dividindo n e d pelo mdc
        n2 = round(r*pn)/mdc
        d2 = d/mdc
        num = str(int(n2))
        deno = str(int(d2))

        raiz = num+"/"+deno
          

    return raiz 

# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================


# ======================================================================
# FUNÇÕES ADICIONAIS
# Implemente neste bloco as funções adicionais às obrigatórias do EP2.
# Duas funções desse tipo (a polinomioToString e a sig) foram 
# fornecidas no próprio enunciado do EP.
# ======================================================================
def polinomioToString(p):
    """Devolve uma string que representa o polinômio em um formato 
       legível para humanos.
       
       p -- a lista dos coeficientes do polinômio
    """
    n = len(p)-1
    s = ""
    for m in range(n-1):
        if p[n-m] != 0:
            s = "%s%s%dx^%d " % (s, sig(m,p[n-m]), p[n-m], n-m)
    if p[1] != 0:
        s = "%s%s%dx " % (s, sig(n-1,p[1]), p[1])
    if p[0] != 0:
        s = "%s%s%d" % (s, sig(n,p[0]), p[0])
    return s

# ======================================================================
def sig(nTermAnte,coef):
    """Devolve '+' se coef não é negativo e existe termo anterior ao
       termo dele no polinômio. Devolve '' (string vazia) no caso
       contrário. Usado para determinar se o '+' deve aparecer antes
       de coef na string que representa o polinômio.
       
       nTermAnte -- expoente de x no termo anterior ao termo do coef
       coef -- coeficiente de um termo do polinômio 
    """
    if nTermAnte > 0 and coef >= 0:
        return "+"
    else:
        return ""

# ======================================================================
# FIM DO BLOCO DE FUNÇÕES ADICIONAIS
# ======================================================================

# ======================================================================
# FUNÇÃO MAIN 
# Escreva dentro da função main() o código que quiser para testar suas 
# demais funções.
# Somente dentro da função main() você pode usar as funções print e
# input.     
# O código da função main() NÃO será avaliado.
# ======================================================================
def main():
    n = int(input("Digite o grau: "))
    
    # Lê os coeficientes do polinômio
    p = []
    for i in range(n+1):
        p.append(float(input("Digite p["+str(i)+"]: ")))
        i += 1
        
    # Obtém a lista de raízes
    if p[n] == 1:
        raizes = listaCanonicaDeRaizes(p)
        print( 'A lista canonica das raizes inteiras de p(x) =',
               polinomioToString(p), 'eh:')
    else:
        raizes = listaRaizesRacionais(p)
        print( 'A lista canonica das raizes racionais de p(x) =',
               polinomioToString(p), 'eh:')
    
    # Imprime a lista canônica de raízes
    for raiz in raizes:
        s = racionalToString(p[n],raiz)
        print(s, end=" ")
        
    print()
        
                
# ======================================================================
# FIM DA FUNÇÃO MAIN 
# ======================================================================


# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__":
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN 
# ======================================================================