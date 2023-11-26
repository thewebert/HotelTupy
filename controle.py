from typing import List;
from personagens import Hospede, TipoHospede;

#Criando Hospedes

def criarHospedes(dia: int, tarefa: int, posicao: int) -> List['Hospede']:
    """Cria os Hóspedes do Hotel de acordo do dia e o número de tarefa.
    
    Parâmetros:
    dia (int): Dia atual do Hotel.
    tarefa (int): Número da tarefa.
    posicao (int): Tamanho da Fila do Hotel.

    Retorna uma Lista de Hóspedes.
    """
    clientes: List['Hospede'] = [];
    if dia == 1: #DIA 1 - 14 Hospedes
        if tarefa == 1: #+4 Hospedes
            clientes.append(Hospede("Sr. Guedes", 'NPC07', TipoHospede.REGULAR, 1, posicao));
            clientes.append(Hospede("Sra. Soares", 'NPC22', TipoHospede.ORGULHOSO, 1, posicao+1));
            clientes.append(Hospede("Sr. Santiago", 'NPC15', TipoHospede.AVARENTO, 1, posicao+2));
            clientes.append(Hospede("Sra. Daora", 'NPC12', TipoHospede.IMPACIENTE, 3, posicao+3));
        elif tarefa == 2: #+3 Hospedes
            clientes.append(Hospede("Sra. Park", 'NPC04', TipoHospede.REGULAR, 1, posicao));
            clientes.append(Hospede("Sr. Oliveira", 'NPC23', TipoHospede.ORGULHOSO, 1, posicao+1));
            clientes.append(Hospede("Sr. Ribeiro", 'NPC05', TipoHospede.REGULAR, 2, posicao+2));
        elif tarefa == 3: #+2 Hospedes
            clientes.append(Hospede("Sr. Toshiba", 'NPC13', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sra. Simões", 'NPC16', TipoHospede.AVARENTO, 1, posicao+1));
        elif tarefa == 4: #+4 Hospedes
            clientes.append(Hospede("Sra. Alencar", 'NPC18', TipoHospede.PILANTRA, 1, posicao));
            clientes.append(Hospede("Sr. Iberê", 'NPC09', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sr. Pereira", 'NPC11', TipoHospede.IMPACIENTE, 1, posicao+2));
        else: #+2 Hospedes
            clientes.append(Hospede("Sr. Duarte", 'NPC20', TipoHospede.AVARENTO, 1, posicao));
            clientes.append(Hospede("Sra. Braga", 'NPC06', TipoHospede.REGULAR, 1, posicao+1));
            
    elif dia == 2: #DIA 2 - 16 Hospedes
        if tarefa == 1:
            clientes.append(Hospede("Sr. Garcia", 'NCP17', TipoHospede.REGULAR, 1, posicao));
            clientes.append(Hospede("Sra. Machado", 'NCP10', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Fonseca", 'NCP14', TipoHospede.IMPACIENTE, 1, posicao+2));
            clientes.append(Hospede("Sr. Figuereido", 'NCP19', TipoHospede.PILANTRA, 1, posicao+3));
        elif tarefa == 2:
            clientes.append(Hospede("Sr. Nascimento", 'NCP21', TipoHospede.ORGULHOSO, 1, posicao));
            clientes.append(Hospede("Sr. Sant'Anna", 'NCP23', TipoHospede.PILANTRA, 1, posicao+1));
            clientes.append(Hospede("Sra. Telles", 'NCP18', TipoHospede.REGULAR, 3, posicao+2));
        elif tarefa == 3:
            clientes.append(Hospede("Sr. Rocha", 'NCP11', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sr. Pacheco", 'NCP05', TipoHospede.AVARENTO, 1, posicao+1));
            clientes.append(Hospede("Sra. Evans", 'NCP08 ', TipoHospede.REGULAR, 1, posicao+2));
        elif tarefa == 4:
            clientes.append(Hospede("Sra. Vieira", 'NPC22', TipoHospede.AVARENTO, 1, posicao));
            clientes.append(Hospede("Sr. Paes", 'NPC11', TipoHospede.ORGULHOSO, 2, posicao+1));
            clientes.append(Hospede("Sra. Fontes", 'NCP01', TipoHospede.REGULAR, 1, posicao+2));
        else:
            clientes.append(Hospede("Sr. Araújo", 'NCP23', TipoHospede.REGULAR, 2, posicao));
            clientes.append(Hospede("Sr. Montes", 'NCP03', TipoHospede.PILANTRA, 1, posicao+1));
            clientes.append(Hospede("Sra. Coelho", 'NCP16', TipoHospede.IMPACIENTE, 1, posicao+2));
            
    elif dia == 3: #DIA 3 - 20 Hospedes
        if tarefa == 1:
            clientes.append(Hospede("Sr. Benevides", 'NPC19', TipoHospede.REGULAR, 1, posicao));
            clientes.append(Hospede("Sra. Tosta", 'NPC16', TipoHospede.ORGULHOSO, 2, posicao+1));
            clientes.append(Hospede("Sra. Viana", 'NCP06', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sr. Bezerra", 'NPC02', TipoHospede.AVARENTO, 1, posicao+3));
        elif tarefa == 2:
            clientes.append(Hospede("Sr. Queiroz", 'NCP21', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sra. Sá", 'NCP10', TipoHospede.IMPACIENTE, 1, posicao+1));
            clientes.append(Hospede("Sra. Gonçalves", 'NCP14', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sr. Rocha", 'NPC00', TipoHospede.ESPECIAL, 1, posicao+3));
        elif tarefa == 3:
            clientes.append(Hospede("Sr. Lima", 'NCP07', TipoHospede.PILANTRA, 1, posicao));
            clientes.append(Hospede("Sr. Souza", 'NCP20', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Vitoriano", 'NCP01', TipoHospede.ORGULHOSO, 1, posicao+2));
            clientes.append(Hospede("Sra. Young", 'NCP04', TipoHospede.REGULAR, 1, posicao+3));
        elif tarefa == 4:
            clientes.append(Hospede("Sra. Neves", 'NCP12', TipoHospede.ORGULHOSO, 1, posicao));
            clientes.append(Hospede("Sr. Jordão", 'NCP17', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Reis", 'NCP08', TipoHospede.AVARENTO, 1, posicao+2));
            clientes.append(Hospede("Sr. Freire", 'NCP15', TipoHospede.IMPACIENTE, 1, posicao+3));
        else:
            clientes.append(Hospede("Sr. Costa", 'NCP03', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sra. Silva", 'NCP06', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sr. Nonaka", 'NPC13', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sr. Noro", 'NCP11', TipoHospede.PILANTRA, 1, posicao+3));
    
    elif dia == 4: #DIA 4 - 21 Hospedes
        if tarefa == 1:
            clientes.append(Hospede("Sr. Cunha", 'NCP05', TipoHospede.REGULAR, 1, posicao));
            clientes.append(Hospede("Sra. Carvalho", 'NCP18', TipoHospede.ORGULHOSO, 1, posicao+1));
            clientes.append(Hospede("Sra. Bastista", 'NCP22', TipoHospede.IMPACIENTE, 1, posicao+2));
            clientes.append(Hospede("Sr. Mesquita", 'NCP19', TipoHospede.PILANTRA, 1, posicao+3));
            clientes.append(Hospede("Sr. Kamaguchi", 'NPC13', TipoHospede.REGULAR, 1, posicao+4));
        elif tarefa == 2:
            clientes.append(Hospede("Sr. Butantã", 'NCP09', TipoHospede.ORGULHOSO, 2, posicao));
            clientes.append(Hospede("Sra. Moraes", 'NCP08', TipoHospede.IMPACIENTE, 1, posicao+1));
            clientes.append(Hospede("Sr. Pinheiro", 'NCP07', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sra. Alves", 'NCP01', TipoHospede.REGULAR, 1, posicao+3));
        elif tarefa == 3:
            clientes.append(Hospede("Sr. Dias", 'NCP17', TipoHospede.PILANTRA, 1, posicao));
            clientes.append(Hospede("Sr. Martins", 'NCP07', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Nunes", 'NCP06', TipoHospede.ORGULHOSO, 1, posicao+2));
            clientes.append(Hospede("Sra. Ramos", 'NCP14', TipoHospede.REGULAR, 1, posicao+3));
        elif tarefa == 4:
            clientes.append(Hospede("Sra. Toscano", 'NCP10', TipoHospede.ORGULHOSO, 1, posicao));
            clientes.append(Hospede("Sr. Jordão", 'NCP21', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Jang", 'NCP04', TipoHospede.AVARENTO, 1, posicao+2));
            clientes.append(Hospede("Sr. Blanco", 'NPC03', TipoHospede.IMPACIENTE, 1, posicao+3));
        else:
            clientes.append(Hospede("Sr. Siqueira", 'NCP15', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sra. Lopes", 'NCP16', TipoHospede.REGULAR, 1, posicao+1));
            clientes.append(Hospede("Sr. Henriqués", 'NPC02', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sr. Noro", 'NCP23', TipoHospede.AVARENTO, 1, posicao+3));
    
    else: #DIA 5 - 24 Hospedes
        if tarefa == 1:
            clientes.append(Hospede("Sra. Rezende", 'NCP01', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sr. Diniz", 'NCP02', TipoHospede.REGULAR, 1, posicao+1));
            clientes.append(Hospede("Sr. Torres", 'NCP03', TipoHospede.ORGULHOSO, 1, posicao+2));
            clientes.append(Hospede("Sra. Moon", 'NCP04', TipoHospede.IMPACIENTE, 1, posicao+3));
            clientes.append(Hospede("Sr. Dantes", 'NCP05', TipoHospede.REGULAR, 1, posicao+4));
        elif tarefa == 2:
            clientes.append(Hospede("Sra. Lins", 'NCP06', TipoHospede.ORGULHOSO, 1, posicao));
            clientes.append(Hospede("Sr. François", 'NCP07', TipoHospede.IMPACIENTE, 1, posicao+1));
            clientes.append(Hospede("Sra. Salvador", 'NCP08', TipoHospede.AVARENTO, 1, posicao+2));
            clientes.append(Hospede("Sr. Caiapó", 'NCP09', TipoHospede.REGULAR, 1, posicao+3));
        elif tarefa == 3:
            clientes.append(Hospede("Sra. Mendes", 'NCP10', TipoHospede.PILANTRA, 1, posicao));
            clientes.append(Hospede("Sr. Bispo", 'NCP11', TipoHospede.AVARENTO, 1, posicao+1));
            clientes.append(Hospede("Sra. Gomes", 'NCP00', TipoHospede.ESPECIAL, 1, posicao+2));
            clientes.append(Hospede("Sra. Feliciano", 'NCP12', TipoHospede.REGULAR, 1, posicao+3));
            clientes.append(Hospede("Sr. Hirai", 'NCP13', TipoHospede.PILANTRA, 1, posicao+4));
            clientes.append(Hospede("Sra. Pires", 'NCP14', TipoHospede.ORGULHOSO, 1, posicao+5));
        elif tarefa == 4:
            clientes.append(Hospede("Sr. Muñoz", 'NCP15', TipoHospede.AVARENTO, 1, posicao));
            clientes.append(Hospede("Sra. Coutinho", 'NCP16', TipoHospede.REGULAR, 1, posicao+1));
            clientes.append(Hospede("Sr. Borges", 'NCP17', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sra. Andrade", 'NCP18', TipoHospede.IMPACIENTE, 1, posicao+3));
        else:
            clientes.append(Hospede("Sr. Mello", 'NCP19', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sr. Lopes", 'NCP20', TipoHospede.ORGULHOSO, 1, posicao+1));
            clientes.append(Hospede("Sr. Miranda", 'NCP21', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sra. Castro", 'NCP22', TipoHospede.AVARENTO, 1, posicao+3));
            clientes.append(Hospede("Sr. Barbosa", 'NCP23', TipoHospede.REGULAR, 1, posicao+4));
    return clientes;



class OrcamentoException(Exception):
  pass

class RequisitoException(Exception):
  pass

class DinheiroException(Exception):
  pass

class PressaException(Exception):
  pass
          