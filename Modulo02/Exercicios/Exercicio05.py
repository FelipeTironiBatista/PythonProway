# Elabore um algoritmo para considerar a realidade de uma universidade
# Deverao ter as seguintes classes:
#       AtividadesAcademicas e AtividadesEsportivas
#       alem da classe herdeira Atividades

# AtividadesAcademicas deverao ter os seguintes metodos
#     LeituraComplementar
#     ApresentacaoTCC
#     ElaboracaoBook
    
# AtividadesEsportivas deverao ter os seguintes metodos
#     Natacao
#     Futebol
    
# Ao instanciar um objeto da classe Atividade, esta devera possuir dois metodos
#     metodosAcademicos
#     metodosEsportivos
# Cada metodo devera invocar os respectivos metodos de cada classe


class AtividadesAcademicas:
    
    def LeituraComplementar(self):
        print("Eu sou o método LeituraComplementar da AtividadesAcademicas")
        
    def ApresentacaoTCC(self):
        print("Eu sou o método ApresentacaoTCC da AtividadesAcademicas")
        
    def ElaboracaoBook(self):
        print("Eu sou o método ElaboracaoBook da AtividadesAcademicas")
        

class AtividadesEsportivas:
    
    def Natacao(self):
        print("Eu sou o método Natacao da AtividadesEsportivas")
        
    def Futebol(self):
        print("Eu sou o método Futebol da AtividadesEsportivas")
   
    
class Atividades(AtividadesAcademicas,AtividadesEsportivas):
    def metodosAcademicos(self):
        super().LeituraComplementar() #<-- O Super retorna apenas os metodos da classe específica.
        super().ApresentacaoTCC()
        super().ElaboracaoBook()
        
    def metodosEsportivos(self):
        super(AtividadesEsportivas, self).Natacao()
        super(AtividadesEsportivas, self).Futebol()
        
atividades = Atividades()
atividades.LeituraComplementar()    
atividades.ApresentacaoTCC()
atividades.ElaboracaoBook()
atividades.Natacao()
atividades.Futebol()
