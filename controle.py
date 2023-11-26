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
            clientes.append(Hospede("Sr. Garcia", 'NPC17', TipoHospede.REGULAR, 1, posicao));
            clientes.append(Hospede("Sra. Machado", 'NPC10', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Fonseca", 'NPC14', TipoHospede.IMPACIENTE, 1, posicao+2));
            clientes.append(Hospede("Sr. Figuereido", 'NPC19', TipoHospede.PILANTRA, 1, posicao+3));
        elif tarefa == 2:
            clientes.append(Hospede("Sr. Nascimento", 'NPC21', TipoHospede.ORGULHOSO, 1, posicao));
            clientes.append(Hospede("Sr. Sant'Anna", 'NPC23', TipoHospede.PILANTRA, 1, posicao+1));
            clientes.append(Hospede("Sra. Telles", 'NPC18', TipoHospede.REGULAR, 3, posicao+2));
        elif tarefa == 3:
            clientes.append(Hospede("Sr. Rocha", 'NPC11', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sr. Pacheco", 'NPC05', TipoHospede.AVARENTO, 1, posicao+1));
            clientes.append(Hospede("Sra. Evans", 'NPC08', TipoHospede.REGULAR, 1, posicao+2));
        elif tarefa == 4:
            clientes.append(Hospede("Sra. Vieira", 'NPC22', TipoHospede.AVARENTO, 1, posicao));
            clientes.append(Hospede("Sr. Paes", 'NPC11', TipoHospede.ORGULHOSO, 2, posicao+1));
            clientes.append(Hospede("Sra. Fontes", 'NPC01', TipoHospede.REGULAR, 1, posicao+2));
        else:
            clientes.append(Hospede("Sr. Araújo", 'NPC23', TipoHospede.REGULAR, 2, posicao));
            clientes.append(Hospede("Sr. Montes", 'NPC03', TipoHospede.PILANTRA, 1, posicao+1));
            clientes.append(Hospede("Sra. Coelho", 'NPC16', TipoHospede.IMPACIENTE, 1, posicao+2));
            
    elif dia == 3: #DIA 3 - 20 Hospedes
        if tarefa == 1:
            clientes.append(Hospede("Sr. Benevides", 'NPC19', TipoHospede.REGULAR, 1, posicao));
            clientes.append(Hospede("Sra. Tosta", 'NPC16', TipoHospede.ORGULHOSO, 2, posicao+1));
            clientes.append(Hospede("Sra. Viana", 'NPC06', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sr. Bezerra", 'NPC02', TipoHospede.AVARENTO, 1, posicao+3));
        elif tarefa == 2:
            clientes.append(Hospede("Sr. Queiroz", 'NPC21', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sra. Sá", 'NPC10', TipoHospede.IMPACIENTE, 1, posicao+1));
            clientes.append(Hospede("Sra. Gonçalves", 'NPC14', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sr. Rocha", 'NPC00', TipoHospede.ESPECIAL, 1, posicao+3));
        elif tarefa == 3:
            clientes.append(Hospede("Sr. Lima", 'NPC07', TipoHospede.PILANTRA, 1, posicao));
            clientes.append(Hospede("Sr. Souza", 'NPC20', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Vitoriano", 'NPC01', TipoHospede.ORGULHOSO, 1, posicao+2));
            clientes.append(Hospede("Sra. Young", 'NPC04', TipoHospede.REGULAR, 1, posicao+3));
        elif tarefa == 4:
            clientes.append(Hospede("Sra. Neves", 'NPC12', TipoHospede.ORGULHOSO, 1, posicao));
            clientes.append(Hospede("Sr. Jordão", 'NPC17', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Reis", 'NPC08', TipoHospede.AVARENTO, 1, posicao+2));
            clientes.append(Hospede("Sr. Freire", 'NPC15', TipoHospede.IMPACIENTE, 1, posicao+3));
        else:
            clientes.append(Hospede("Sr. Costa", 'NPC03', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sra. Silva", 'NPC06', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sr. Nonaka", 'NPC13', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sr. Noro", 'NPC11', TipoHospede.PILANTRA, 1, posicao+3));
    
    elif dia == 4: #DIA 4 - 21 Hospedes
        if tarefa == 1:
            clientes.append(Hospede("Sr. Cunha", 'NPC05', TipoHospede.REGULAR, 1, posicao));
            clientes.append(Hospede("Sra. Carvalho", 'NPC18', TipoHospede.ORGULHOSO, 1, posicao+1));
            clientes.append(Hospede("Sra. Bastista", 'NPC22', TipoHospede.IMPACIENTE, 1, posicao+2));
            clientes.append(Hospede("Sr. Mesquita", 'NPC19', TipoHospede.PILANTRA, 1, posicao+3));
            clientes.append(Hospede("Sr. Kamaguchi", 'NPC13', TipoHospede.REGULAR, 1, posicao+4));
        elif tarefa == 2:
            clientes.append(Hospede("Sr. Butantã", 'NPC09', TipoHospede.ORGULHOSO, 2, posicao));
            clientes.append(Hospede("Sra. Moraes", 'NPC08', TipoHospede.IMPACIENTE, 1, posicao+1));
            clientes.append(Hospede("Sr. Pinheiro", 'NPC07', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sra. Alves", 'NPC01', TipoHospede.REGULAR, 1, posicao+3));
        elif tarefa == 3:
            clientes.append(Hospede("Sr. Dias", 'NPC17', TipoHospede.PILANTRA, 1, posicao));
            clientes.append(Hospede("Sr. Martins", 'NPC07', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Nunes", 'NPC06', TipoHospede.ORGULHOSO, 1, posicao+2));
            clientes.append(Hospede("Sra. Ramos", 'NPC14', TipoHospede.REGULAR, 1, posicao+3));
        elif tarefa == 4:
            clientes.append(Hospede("Sra. Toscano", 'NPC10', TipoHospede.ORGULHOSO, 1, posicao));
            clientes.append(Hospede("Sr. Jordão", 'NPC21', TipoHospede.REGULAR, 2, posicao+1));
            clientes.append(Hospede("Sra. Jang", 'NPC04', TipoHospede.AVARENTO, 1, posicao+2));
            clientes.append(Hospede("Sr. Blanco", 'NPC03', TipoHospede.IMPACIENTE, 1, posicao+3));
        else:
            clientes.append(Hospede("Sr. Siqueira", 'NPC15', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sra. Lopes", 'NPC16', TipoHospede.REGULAR, 1, posicao+1));
            clientes.append(Hospede("Sr. Henriquez", 'NPC02', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sr. Noro", 'NPC23', TipoHospede.AVARENTO, 1, posicao+3));
    
    else: #DIA 5 - 24 Hospedes
        if tarefa == 1:
            clientes.append(Hospede("Sra. Rezende", 'NPC01', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sr. Diniz", 'NPC02', TipoHospede.REGULAR, 1, posicao+1));
            clientes.append(Hospede("Sr. Torres", 'NPC03', TipoHospede.ORGULHOSO, 1, posicao+2));
            clientes.append(Hospede("Sra. Moon", 'NPC04', TipoHospede.IMPACIENTE, 1, posicao+3));
            clientes.append(Hospede("Sr. Dantes", 'NPC05', TipoHospede.REGULAR, 1, posicao+4));
        elif tarefa == 2:
            clientes.append(Hospede("Sra. Lins", 'NPC06', TipoHospede.ORGULHOSO, 1, posicao));
            clientes.append(Hospede("Sr. François", 'NPC07', TipoHospede.IMPACIENTE, 1, posicao+1));
            clientes.append(Hospede("Sra. Salvador", 'NPC08', TipoHospede.AVARENTO, 1, posicao+2));
            clientes.append(Hospede("Sr. Caiapó", 'NPC09', TipoHospede.REGULAR, 1, posicao+3));
        elif tarefa == 3:
            clientes.append(Hospede("Sra. Mendes", 'NPC10', TipoHospede.PILANTRA, 1, posicao));
            clientes.append(Hospede("Sr. Bispo", 'NPC11', TipoHospede.AVARENTO, 1, posicao+1));
            clientes.append(Hospede("Sra. Gomes", 'NPC00', TipoHospede.ESPECIAL, 1, posicao+2));
            clientes.append(Hospede("Sra. Feliciano", 'NPC12', TipoHospede.REGULAR, 1, posicao+3));
            clientes.append(Hospede("Sr. Hirai", 'NPC13', TipoHospede.PILANTRA, 1, posicao+4));
            clientes.append(Hospede("Sra. Pires", 'NPC14', TipoHospede.ORGULHOSO, 1, posicao+5));
        elif tarefa == 4:
            clientes.append(Hospede("Sr. Muñoz", 'NPC15', TipoHospede.AVARENTO, 1, posicao));
            clientes.append(Hospede("Sra. Coutinho", 'NPC16', TipoHospede.REGULAR, 1, posicao+1));
            clientes.append(Hospede("Sr. Borges", 'NPC17', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sra. Andrade", 'NPC18', TipoHospede.IMPACIENTE, 1, posicao+3));
        else:
            clientes.append(Hospede("Sr. Mello", 'NPC19', TipoHospede.IMPACIENTE, 1, posicao));
            clientes.append(Hospede("Sr. Lopes", 'NPC20', TipoHospede.ORGULHOSO, 1, posicao+1));
            clientes.append(Hospede("Sr. Miranda", 'NPC21', TipoHospede.REGULAR, 1, posicao+2));
            clientes.append(Hospede("Sra. Castro", 'NPC22', TipoHospede.AVARENTO, 1, posicao+3));
            clientes.append(Hospede("Sr. Barbosa", 'NPC23', TipoHospede.REGULAR, 1, posicao+4));
    return clientes;



class OrcamentoException(Exception):
  pass

class RequisitoException(Exception):
  pass

class DinheiroException(Exception):
  pass

class PressaException(Exception):
  pass
          