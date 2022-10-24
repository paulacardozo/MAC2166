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
  
  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html


"""

# ======================================================================
#
#   M A I N 
#
# ======================================================================

def main():
    modo = int(input("modo: "))
    if modo == 1:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
        n3 = int(input("n3: "))
        n4 = int(input("n4: "))
        n = int(input("n: "))
        soma = n1**2 + n2**2 + n3**2 + n4**2 
        if soma != n:
            print("falso")
        else:
            print("verdadeiro")
    else:
        n = int(input("n: "))
        n1 = 2
        n2 = 3
        n3 = 5
        n4 = 7
        soma = n1**2+n2**2+n3**2+n4**2
        if soma > n:
            print("falso")
        elif soma == n:
            print(n1, n2, n3, n4)
        else:
            #aqui a soma é menor, então precisamos achar uma nova sequência de n que satisfaça a soma
            #aumentando de primo e primo e encontrando um novo valor para n4
                n1=n2
                n2=n3
                n3=n4
                n4=n4 + 1
                n4primo = False
                cont = 0
                div = 1
                somamenor = True
            #o cont e o div irão auxiliar no laço que testa se o novo n4 será primo
            #o laço ocorre enquanto o n4 não é primo
                while somamenor == True or n4primo == False:
                    while div <= n4:
                        if n4 % div == 0:
                            cont = cont + 1
                        div = div + 1
                    if cont > 2:
                        n4 = n4 + 1
                        cont = 0
                        div = 1
                    #aqui significa que não é primo, então um novo n4 será gerado e testado
                    #sendo assim, cont e o div devem voltar ao valor padrão
                    elif cont == 2:
                        n4primo = True
                        soma = n1**2+n2**2+n3**2+n4**2
                    #aqui significa que é primo, mas é necessário testar a soma
                        if soma < n:
                            n1 = n2
                            n2 = n3
                            n3 = n4
                            n4 = n4 + 1
                            n4primo = False
                    #o n4primo deixa de ser true, pois foi adicionado 1
                    #então, cont e div devem voltar ao valor padrão
                            cont = 0
                            div = 1
                        elif soma == n:
                            print(n1, n2, n3, n4)
                            somamenor = False
                        else:
                            #aqui a soma > n
                            print("falso")
                            somamenor = False
            
main ()