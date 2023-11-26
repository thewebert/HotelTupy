from tupy import *;
from enum import Enum;
from typing import List, Optional;
from abc import abstractmethod;
import random;

#CLASSES ENUM (PERSONAGENS)
class Direcao(Enum):
    """Direções de Movimento."""

    ESQUERDA = 'L';
    DIREITA = 'R';
    FRENTE = 'F';
    COSTAS = 'B';

class TipoHospede(Enum):
    """Tipos de Hóspedes."""

    REGULAR: int = 1;
    IMPACIENTE: int = 2;
    AVARENTO: int = 3;
    ORGULHOSO: int = 4;
    PILANTRA: int = 5;
    ESPECIAL: int = 6;

    @staticmethod
    def decrementoPaciencia(tipo: 'TipoHospede') -> int:
      """Retorna o quanto Decremento de Paciência de acordo com o Tipo do Hóspede.
      
      Parâmetro:
      tipo (TipoHospede): O Tipo do Hóspede."""
      if tipo==TipoHospede.IMPACIENTE: return 3;
      elif tipo==TipoHospede.AVARENTO or tipo==TipoHospede.ORGULHOSO: return 2;
      else: return 1;

    @staticmethod
    def cor(tipo: 'TipoHospede') -> str:
      """Retorna a Cor que representa cada Tipo de Hóspede.
      
      Parâmetro:
      tipo (TipoHospede): O Tipo do Hóspede."""
      if tipo==TipoHospede.REGULAR: return "Deep Sky Blue";
      elif tipo==TipoHospede.IMPACIENTE: return "Crimson";
      elif tipo==TipoHospede.AVARENTO: return "Silver";
      elif tipo==TipoHospede.ORGULHOSO: return "Thistle";
      elif tipo==TipoHospede.PILANTRA: return "Sea Green";
      elif tipo==TipoHospede.ESPECIAL: return "Goldenrod";

    @staticmethod
    def valorCarteira(tipo: 'TipoHospede', ndias: int) -> int:
      """Retorna o quanto de Dinheiro tem o Hóspede de acordo com o Tipo e quantos Dias ele pretende se hospedar.
      
      Parâmetros:
      tipo (TipoHospede): O Tipo do Hóspede.
      nDias (int): O número de Dias que ele pretende se hospedar."""
      if tipo==TipoHospede.REGULAR or tipo==TipoHospede.IMPACIENTE or tipo==TipoHospede.PILANTRA: 
          x: int = random.randint(ndias, 5)
          return x*70;
      elif tipo==TipoHospede.AVARENTO: return ndias*90;
      elif tipo==TipoHospede.ORGULHOSO: return ndias*163;
      elif tipo==TipoHospede.ESPECIAL: return random.randint(0, 250)+random.randint(300, 750);

class HospedeSituacao(Enum):
    """Situações do Hóspede."""
    FORA = 1;
    FILA = 2;
    ATENDIMENTO = 3;
    ENTRANDO = 4;
    SAINDO = 5;

class AtendenteSituacao(Enum):
    ATENDENDO = 1;
    SAINDO = 2
    CHEGANDO = 3;
    BEBENDO = 4;
    EXAUSTO = 5;

#CLASSES DE NÓ/LISTA (PERSONAGENS)
class Frame():
    """Frame define as imagens de movimento dos Personagens.
    
    Relacionado com a Pasta Avatares onde as imagens segue o padrão:
    tag_personagem + - + direcao + frame + .png
    ex: NPC01-LM1.png
    as Direção são: B (Back), F (Front), L (Left), R (Right).
    e os Frame são: M1 ou M2 (Moving, com as pernas do personagem alternando) e S1 (Static, o personagem parado).
    """
    def __init__(self, posicao: str) -> None:
        """Cria um Frame.
        
        Parâmetro: 
        posicao (str): o nome do Frame.
        """
        self.posicao: str = posicao+".png"
        self._prox: 'Frame'|None = None ;

    @property
    def prox(self) -> Optional['Frame']:
        """Retonra o próximo Frame.
        Retorna None caso esse seja o último Frame."""
        return self._prox;

    def apontePara(self, outroFrame: 'Frame') -> None:
        """Define o próximo Frame"""
        self._prox = outroFrame;

    @staticmethod
    def caminho() -> 'Frame':
        """Retorna o Frame inicial do ciclo de Frames do Personagem andando."""
        p1 = Frame('S1')
        p2 = Frame('M1')
        p1.apontePara(p2);
        p3 = Frame('S1')
        p2.apontePara(p3)
        p4 = Frame('M2')
        p3.apontePara(p4)
        p4.apontePara(p1)
        return p1;

    @staticmethod
    def cafe() -> 'Frame':
        """Retorna o Frame inicial do ciclo de Frames do Personagem bebendo café."""
        p1 = Frame('BC1')
        p2 = Frame('BC2')
        p2.apontePara(p1)
        p1.apontePara(p2)
        return p1;

class Ponto():
    """Ponto define a marcação X ou Y que o Personagem deve ir."""

    def __init__(self, final: int, direcao: Direcao) -> None:
        """Cria um Ponto de locomoção.
        
        Parâmetros:
        final (int): O destino que o Personagem deve ir.
        direcao (Direcao): A direção que o Personagem deve se locomover.
        
        caso o Final sejá 0 significa que o Personagem deve rotacionar para a Direção."""
        self.final: int = final
        self.direcao: Direcao = direcao;
        self._prox: 'Ponto'|None = None;

    @property
    def prox(self) -> Optional['Ponto']:
        """Retorna o próximo Ponto do trajeto do Personagem."""
        return self._prox;

    def apontePara(self, outroPonto: 'Ponto') -> None:
        """Aponta para um próximo Ponto.
        
        Parâmetro:
        outroPonto (Ponto): O Ponto que será referenciado."""
        self._prox = outroPonto;

    @staticmethod
    def _ligarPontos(lista: List['Ponto']) -> 'Ponto':
        """Cria uma Sêquencia de Pontos, um Trajeto.
        
        Parâmetros: 
        lista (List[Ponto]): Uma lista de Pontos.
        
        Retonra:
        O Ponto inicial do Trajeto."""
        p: 'Ponto' = lista[0];
        for x in range(1, len(lista)):
            p.apontePara(lista[x]);
            p = lista[x];
        return lista[0];

    @staticmethod
    def caminhoQuarto(numero: int) -> 'Ponto':
        """Retorna o caminho para algum Quarto do Térreo.
        
        Parâmetro:
        numero (int): O número do Quarto.
        
        Retorno:
        O Ponto inicial do Trajeto."""
        direcao: Direcao = Direcao.ESQUERDA;
        limite = 90;
        if numero == 6: 
            direcao = Direcao.DIREITA;
            limite = 690;
        elif numero == 5: 
            direcao = Direcao.DIREITA;
            limite = 560;
        elif numero == 3: limite = 330;
        elif numero == 2: limite = 210;
        lista: List['Ponto'] = [Ponto(0, Direcao.COSTAS), Ponto(125, Direcao.COSTAS), Ponto(0, direcao),
        Ponto(limite, direcao), Ponto(0, Direcao.COSTAS), Ponto(95, Direcao.COSTAS)]
        return Ponto._ligarPontos(lista);

    @staticmethod
    def caminhoQuartoEscondido() -> 'Ponto':
        """Retorna o caminho para os Quartos 7 e 8 do Térreo.
        Retorno:
        O Ponto inicial do Trajeto."""
        lista: List['Ponto'] = [Ponto(0, Direcao.COSTAS), Ponto(125, Direcao.COSTAS), Ponto(0, Direcao.DIREITA),
        Ponto(920, Direcao.DIREITA)]
        return Ponto._ligarPontos(lista);

    @staticmethod
    def caminhoAte004() -> 'Ponto':
        """Retorna o caminho para os Quarto 4 do Térreo.
        Retorno:
        O Ponto inicial do Trajeto."""

        lista: List['Ponto'] = [Ponto(0, Direcao.COSTAS), Ponto(95, Direcao.COSTAS)]
        return Ponto._ligarPontos(lista);
    
    @staticmethod
    def caminhoEscadas() -> 'Ponto':
        """Retorna o caminho para qualquer Quarto que não seja no térreo.
        
        Retorno:
        O Ponto inicial do Trajeto."""
        lista: List['Ponto'] = [Ponto(0, Direcao.COSTAS), Ponto(125, Direcao.COSTAS), Ponto(0, Direcao.DIREITA),
        Ponto(840, Direcao.DIREITA), Ponto(0, Direcao.COSTAS), Ponto(-75, Direcao.COSTAS)]
        return Ponto._ligarPontos(lista);
    
    @staticmethod
    def indoEmbora() -> 'Ponto':
        """Retorna o Ponto inicial do Trajeto até a porta de saída."""
        lista: List['Ponto'] = [Ponto(0, Direcao.COSTAS), Ponto(335, Direcao.COSTAS), Ponto(0, Direcao.ESQUERDA),
        Ponto(-50, Direcao.ESQUERDA)]
        return Ponto._ligarPontos(lista);

    @staticmethod
    def vamosTrabalhar() -> 'Ponto':
        """Retorna o Ponto inicial do Trajeto do Atendente até sua mesa."""
        lista: List['Ponto'] = [Ponto(950, Direcao.DIREITA), Ponto(0, Direcao.FRENTE), Ponto(325, Direcao.FRENTE),
        Ponto(0, Direcao.ESQUERDA), Ponto(620, Direcao.ESQUERDA)]
        return Ponto._ligarPontos(lista);

    @staticmethod
    def pareDeTrabalhar() -> 'Ponto':
        """Retorna o Ponto inicial do Trajeto do Atendente até a saída."""
        lista: List['Ponto'] = [Ponto(0, Direcao.FRENTE), Ponto(0, Direcao.DIREITA), Ponto(950, Direcao.DIREITA),
        Ponto(0, Direcao.COSTAS), Ponto(125, Direcao.COSTAS), Ponto(0, Direcao.ESQUERDA), Ponto(-70, Direcao.ESQUERDA)]
        return Ponto._ligarPontos(lista);

    @staticmethod
    def andarFila(posicao: int) -> 'Ponto':
        """Retorna o Ponto que os Hóspedes na Fila devem ir de acordo com suas posições.
        
        Paraâmetro:
        posicao (int): Posição do Hóspede na Fila.
        
        Retorno:
        Ponto inicial do Trajeto."""
        if posicao == 1: return Ponto(450, Direcao.DIREITA)
        elif posicao == 2: return Ponto(340, Direcao.DIREITA)
        elif posicao == 3: return Ponto(230, Direcao.DIREITA)
        elif posicao == 4: return Ponto(120, Direcao.DIREITA)
        elif posicao == 5: return Ponto(10, Direcao.DIREITA)
        else: return Ponto(0, Direcao.DIREITA)

class FilaNo():
    """FilaNo representa a Fila de Atendimento do Hotel."""

    def __init__(self, hospede: 'Hospede', posicao: int) -> None:
        """Cria um No na Fila dos Hóspedes.
        
        Parâmetros:
        hospede (Hospede): O Hóspede.
        posicao (int): Sua posição na Fila."""
        self._hospede: 'Hospede' = hospede;
        self._posicao: int = posicao;
        self._prox: 'FilaNo'|None = None;
    
    @property
    def hospede(self) -> 'Hospede':
        """Retonra o Hospede."""
        return self._hospede;

    @property
    def posicao(self) -> int:
        """Retonra a posição do Hóspede na Fila."""
        return self._posicao;

    @posicao.setter
    def posicao(self, p: int) -> None:
        """Altera a posição do Hóspede."""
        self._posicao = p;

    @property
    def prox(self) -> Optional['FilaNo']:
        """Retonra o próximo Hóspede da Fila."""
        return self._prox;

    def apontePara(self, outroNo:'FilaNo') -> None:
        """Direciona o próximo Hóspede da Fila."""
        self._prox = outroNo;
    
    def ultimo(self) -> None:
        """Tire a refêrencia para o próximo Hóspede da Fila."""
        self._prox = None;

    @staticmethod
    def reordenar(no: Optional['FilaNo']) -> Optional['FilaNo']:
        """Reordena a Fila do Hóspedes.
        
        Parâmetro:
        no (FilaNo ou None): A Fila atual.
        
        Retonra:
        A Fila reordena."""
        posicao: int = 1;
        x: FilaNo|None = no;
        while(x and posicao<4):
            if x.posicao!=posicao:
                x.posicao = posicao;
                x.hospede.trajeto(Ponto.andarFila(posicao));
                x.hospede.enfilerado();
            x = x.prox;
            posicao += 1;
        return no;

    @property
    def tamanho(no: Optional['FilaNo']) -> int:
        """Retorna quantos Hóspedes há na Fila (Apartir de um Hóspede).
        
        Parâmetro:
        no (FilaNo ou None): A Fila atual.
        
        Retorna: Quantos nós há a partir desse. Zero casa a fila esteja vazia."""
        if not no: return 0;
        tam: int = no.posicao;
        n: FilaNo|None = no
        while (n):
            tam += 1;
            n = n.prox;
        return tam;

    @staticmethod
    def entrarNaFila(cabeca: Optional['FilaNo'], lista: List['Hospede']) -> Optional['FilaNo']:
        """Adiciona uma lista de Hóspedes na Fila.
        
        Parâmetros:
        cabeca (FilaNo ou None): A Fila atual.
        lista (List[Hospede]): Os Hóspedes que entraram na Fila.
         
        Retorna:
        O primeiro Nó da Fila. """
        posicao: int = 1;
        if len(lista)==0: return None;
        if not cabeca:
            novaCabeca: FilaNo = FilaNo(lista[0], posicao);
            lista[0].trajeto(Ponto.andarFila(posicao));
            no: FilaNo = novaCabeca
            posicao += 1;
            for x in range(1, len(lista)):
                novoNo: FilaNo = FilaNo(lista[x], posicao);
                if posicao<4: 
                    lista[x].trajeto(Ponto.andarFila(posicao));
                    lista[x].enfilerado();
                no.apontePara(novoNo);
                no = novoNo;
                posicao += 1;
            
            return novaCabeca;
        else:
            posicao+=1;
            ant = cabeca;
            n: FilaNo|None = None;
            if cabeca and cabeca.prox: n = cabeca.prox;
            while(n):
                if n.posicao!=posicao and posicao<4:
                    n.posicao = posicao;
                    n.hospede.trajeto(Ponto.andarFila(posicao));
                    lista[x].enfilerado();
                ant = n;
                n = n.prox;
                posicao+=1;
            
            nozinho = FilaNo(lista[0], posicao);
            if posicao<4: lista[0].trajeto(Ponto.andarFila(posicao));
            posicao += 1;
            ant.apontePara(nozinho);
            no = nozinho;
            for x in range(1, len(lista)):
                novoNo = FilaNo(lista[x], posicao);
                if posicao<4: lista[x].trajeto(Ponto.andarFila(posicao));
                no.apontePara(novoNo);
                no = novoNo;
                posicao += 1;
            return cabeca;

    @staticmethod
    def sairDaFila(cabeca: Optional['FilaNo'], posicao: int) -> Optional['FilaNo']:
        """Retira um Nó da Fila.
        
        Parâmetros:
        cabeca (FilaNo ou None): A Fila atual.
        posicao (int): A posição que está o Hóspede que saiu.
         
        Retorna:
        O primeiro Nó da Fila reordenada. """
        if not cabeca: return None;
        no: FilaNo|None = cabeca;
        ant: FilaNo|None = no;
        while(no and no.posicao!=posicao):
            ant = no;
            no = no.prox;
        if(cabeca.posicao == posicao): 
            cabeca = cabeca.prox;
        elif(no and no.prox and ant): ant.apontePara(no.prox);
        else: 
            if ant: ant.ultimo();
        return FilaNo.reordenar(cabeca);

#CLASSES TUPY (PERSONAGENS)

class Imagellela(BaseImage):
    """Subclasse de BaseImage"""
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y);

    def altereImagem(self, imagem: str) -> None:
        """Altera o arquivo da Imagem.
        Parâmetro:
        imagem (str): Endereço da nova Imagem."""
        self._file = imagem;

class Avatar(BaseGroup):
    """Avatar dos Personagens."""
    def __init__(self, x: int, y: int, file: str) -> None:
        """Cria um Avatar.
        
        Parâmetros:
        x (int): Posição horizontal inicial.
        y (int): Posição vertical inicial.
        file (str): Arquivo com a Imagem do Avatar."""
        self._x: int = x;
        self._y: int = y;
        self._avatar: Imagellela = Imagellela(file, x, y);
        self._espaco: Rectangle = Rectangle(x-37, y-97, 80, 9, fill = "", outline = "Black")
        self._add(self._avatar);
        self._add(self._espaco)
    
    def _pare(self, tipo: str, direcao: Direcao) -> None:
        """Atualiza a Imagem do Avatar para uma posição estática.
        
        Parâmetros:
        tipo (str): tag do Personagem.
        direcao (Direcao): Direção atual do Personagem."""

        self._avatar.altereImagem("avatares/"+tipo+"-"+direcao.value+"S1.png");

    def _pegarImagem(self, tipo: str, direcao: Direcao, posicao: str) -> str:
        """Retorna a Imagem do Avatar para uma posição.
        
        Parâmetros:
        tipo (str): tag do Personagem.
        direcao (Direcao): Direção atual do Personagem.
        pisicao (str): Posição atual do Personagem."""

        img: str = "avatares/"+tipo+"-"+direcao.value+""+posicao;
        return img;

    def _movimentoEsquerda(self, arquivo: str) -> None:
            """Movimenta o Avatar no eixo horizontal para a esquerda."""
            self._avatar.altereImagem(arquivo);
            self._x -= 10;
    
    def _movimentoDireita(self, arquivo: str) -> None:
            """Movimenta o Avatar no eixo horizontal para a direita."""
            self._avatar.altereImagem(arquivo);
            self._x += 10;

    def _movimentoFrente(self, arquivo: str) -> None:
            """Movimenta o Avatar no eixo vertical para a cima."""
            self._avatar.altereImagem(arquivo);
            self._y += 10;

    def _movimentoCostas(self, arquivo: str) -> None:
            """Movimenta o Avatar no eixo vertical para a baixo."""
            self._avatar.altereImagem(arquivo);
            self._y -= 10;
    
    def movimento(self, p: 'Ponto', frame: Frame, tipo: str) -> bool:
        """Realiza o Movimento do Avatar.
        
        Parâmetros:
        p (Ponto): O Ponto que o Avatar deve ir.
        frame (Frame): O Frame atual do Personagem;
        tipo (str): tag do Personagem.
        
        Retorna True caso o Avatar tenha chegado no destino, False caso contrário."""
        if p.final==0:
            self._pare(tipo, p.direcao)
            return True;
        else:
            img: str = self._pegarImagem(tipo, p.direcao, frame.posicao)
            saida: int = 0;
            if p.direcao==Direcao.ESQUERDA: 
                saida = self._x;
                self._movimentoEsquerda(img);
            elif p.direcao==Direcao.DIREITA: 
                saida = self._x;
                self._movimentoDireita(img)
            elif p.direcao==Direcao.FRENTE:
                saida = self._y;
                self._movimentoFrente(img)
            elif p.direcao==Direcao.COSTAS: 
                saida = self._y;
                self._movimentoCostas(img)
            if saida==p.final: 
                self._pare(tipo, p.direcao)
                return True
            return False;

class PC(Avatar):
    """PC é Player Character, o Avatar do Atendente."""
    def __init__(self, x: int, y: int, file: str) -> None:
        """Cria o Avatar do Antendete.
        
        Parâmetros:
        x (int): Posição horizontal inicial.
        y (int): Posição vertical inicial.
        file (str): Arquivo com a Imagem do Avatar.
        """
        super().__init__(x, y, file)
        self._energia: Rectangle = Rectangle(x-36, y-96, 78, 7, fill = "Dark Green", outline = 'Dark Green')
        self._add(self._energia)
        #Um PC tem uma barra de energia.
    
    def consumirEnergia(self) -> bool:
        """Diminui a barra de energia do PC.
        Retonra True caso já tenha reduzido o máximo, Falso caso contrário."""
        if self._energia.width==0: return True;
        self._energia.width -= 1;
        self._mudarCor();
        return False;

    def bebendoCafe(self) -> None:
        """Aumenta a barra de energia do PC."""
        if self._energia.width < 78:
            self._energia.width += 1;
            self._mudarCor();
    
    def animacaoCafe(self, tag: str, p: 'Frame') -> None:
        """Atualiza a Imagem do PC bebendo café.
        
        Parâmetros:
        tag (str): tag do Personagem."""
        self._avatar.altereImagem("avatares/"+tag+"-"+p.posicao);
    
    def parandoCafe(self, tag: str, direcao: Direcao) -> None:
        """Atualiza a Imagem do PC para um Frame estático.
        
        Parâmetros:
        tag (str): tag do Personagem.
        direcao (Direcao): Direcao atual do Personagem. """
        self._avatar.altereImagem("avatares/"+tag+"-"+direcao.value+"S1.png");

    def cheio(self) -> bool:
        """Retorna True se a barra de energia está cheia, False caso contrário."""
        if self._energia.width==78: return True;
        return False;

    def _mudarCor(self) -> None:
        """Altera a cor da barra de energia de acordo com sua largura."""
        cor: str = "Dark Green"
        if self._energia.width > 25 and self._energia.width < 55: cor = "Gold"
        elif self._energia.width < 26: cor = "Maroon"
        self._energia.fill = cor;
        self._energia.outline = cor;

    def reanimar(self) -> None:
        """Retorna as a situação padrão da barra de energia do PC>"""
        self._energia.width = 78;
        self._energia.outline = "Dark Green";
        self._energia.fill = "Dark Green"

class NPC(Avatar):
    """NPC é Nonplayer Character, o Avatar do Hóspede."""
    def __init__(self, x: int, y: int, hospede: 'Hospede') -> None:
        """Cria o Avatar do Hóspede.
        
        Parâmetros:
        x (int): Posição horizontal inicial.
        y (int): Posição vertical inicial.
        file (str): Arquivo com a Imagem do Avatar.
        """
        super().__init__(x, y, hospede.imagemEstatica);
        self._paciencia: Rectangle = Rectangle(x-36, y-96, 78, 7, fill = hospede.cor, outline = hospede.cor);
        self._add(self._paciencia);
        #NPC tem uma barra de paciência.

    def consumirPaciencia(self) -> bool:
        """Retorna True caso já tenha consumido toda a paciência, False caso contrário."""
        self._paciencia.width -= 1;
        if self._paciencia.width==0: return True;
        return False;

    def esconder(self) -> None:
        """Esconde o Avatar."""
        self._hide();

    def aparecer(self) -> None:
        """Reaparece o Avatar."""
        self._show();

#CLASSES PRINCIPAIS (PERSONAGENS)
class Personagem():
    """Personagem é um Personagem do Hotel (Hóspede ou Atendente)"""
    def __init__(self, tag: str, direcao: Direcao) -> None:
      """Cria um Personagem.
      
      Parâmetros:
      tag (str): A tag do Personagem, que refêrencia como seus frames foram salvos na pasta Avatares.
      direcao (Direcao): A direção que o Personagem está olhando."""
      self._tag: str = tag;
      self._direcao: Direcao = direcao;
      self._frame: 'Frame' =  Frame.caminho();
      self._frameTemp: int = 0;
      self._ponto: 'Ponto'|None = None;
      self._pontoTemp: int = 0;

    @property
    def imagemEstatica(self) -> str:
      """Retorna a Imagem do Frame estático do Personagem."""
      return "avatares/"+self._tag+"-"+self._direcao.value+"S1.png"
    
    def parado(self) -> bool:
        """Caso o Personagem não tenha nenhum Ponto de Trajeto retorna True, False caso contrário."""
        if self._ponto: return False;
        return True;

    def trajeto(self, ponto: 'Ponto') -> None:
        """Adiciona um Trajeto para o Personagem."""
        self._ponto = ponto;

    def _mudandoFrame(self) -> None:
        """Muda os Frames do Personagem."""
        if self._frameTemp==0:  
            if self._frame and self._frame.prox: self._frame = self._frame.prox;
            self._frameTemp=3;
        else: self._frameTemp-=1;

    def _movimentando(self, avatar: 'Avatar') -> None:
        """Realiza os Movimentos do Personagem.
        
        Parâmetro:
        avatar (Avatar): O avatar que irá implementar o movimento."""
        if self._ponto: 
            if self._pontoTemp==0:
                self._mudandoFrame()             
                if avatar.movimento(self._ponto, self._frame, self._tag):
                    self._mudandoFrame()
                    if self._ponto and self._ponto.prox: 
                        self._ponto = self._ponto.prox;
                        self._direcao = self._ponto.direcao;
                    else: self._ponto = None;
                    self._pontoTemp = 8;
            else: self._pontoTemp-=1;

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def saiu(self) -> bool:
        pass

class Atendente(Personagem):
    def __init__(self) -> None:
        super().__init__('MAIN', Direcao.DIREITA)
        self._energiaTemp = 24;
        self._andando: bool = False;
        self._situacao: AtendenteSituacao = AtendenteSituacao.CHEGANDO;
        self._avatar: 'PC' = PC(0, 125, super().imagemEstatica);

    def volteAoTrabalho(self) -> None:
        if self._situacao == AtendenteSituacao.BEBENDO:
            self._situacao = AtendenteSituacao.ATENDENDO;
            self._frameTemp = 0;
            self._frame = Frame.caminho();
            self._avatar.parandoCafe(self._tag, self._direcao);
            self._energiaTemp = 24;

    def estaTrabalhando(self) -> bool:
        if self._situacao == AtendenteSituacao.ATENDENDO: return True;
        return False;

    def boraTrabalhar(self) -> None:
        self._situacao = AtendenteSituacao.CHEGANDO;
        self._avatar.reanimar();
        self._andando = True;
        self._ponto = Ponto.vamosTrabalhar();
    
    def fimDoTrabalho(self) -> None:
        self._situacao = AtendenteSituacao.SAINDO;
        self._frame = Frame.caminho();
        self._ponto = Ponto.pareDeTrabalhar();
        self._andando = True;

    def saiu(self) -> bool:
        if self._situacao == AtendenteSituacao.SAINDO and not self._ponto:
            self._andando = False;
            return True;
        self.update();
        return False;

    def andando(self) -> bool:
        return self._andando;

    def cheio(self) -> bool:
        return self._avatar.cheio();

    def beba(self) -> None:
        self._energiaTemp = 24;
        self._frame = Frame.cafe();
        self._frameTemp = 0;
        self._situacao = AtendenteSituacao.BEBENDO;
        
    def exausto(self) -> bool:
        if self._situacao == AtendenteSituacao.EXAUSTO:
            return True;
        return False;

    def bebendo(self) -> bool:
        if self._situacao == AtendenteSituacao.BEBENDO:
            return True;
        return False;

    def atendendo(self) -> bool:
        if self._situacao == AtendenteSituacao.ATENDENDO:
            return True;
        return False;

    def _mudandoFrameCafe(self) -> None:
        if self._frameTemp==0:  
            if self._frame and self._frame.prox: self._frame = self._frame.prox;
            self._frameTemp=3;
            self._avatar.animacaoCafe(self._tag, self._frame);
        else: self._frameTemp-=1;
    
    def update(self) -> None:
        if self._situacao == AtendenteSituacao.ATENDENDO:
            if self._energiaTemp <= 1:
                self._energiaTemp = 24;
                if self._avatar.consumirEnergia(): 
                    self._situacao = AtendenteSituacao.EXAUSTO;
                    toast("Você está exautsto", 3000)
            else: self._energiaTemp -= 1;
        
        elif self._situacao == AtendenteSituacao.BEBENDO:
            if self._energiaTemp <= 0:
                self._energiaTemp = 24;
                self._avatar.bebendoCafe();
                self._mudandoFrameCafe();
            else: self._energiaTemp -= 3;

        elif self._situacao == AtendenteSituacao.CHEGANDO:
            if self._ponto: self._movimentando(self._avatar);
            else: 
                self._andando = False;
                self._situacao = AtendenteSituacao.ATENDENDO;

        elif self._situacao == AtendenteSituacao.SAINDO:
            self._movimentando(self._avatar);

class Hospede(Personagem):
    """Hospede é uma subclasse de Personagem."""
    def __init__(self, nome: str, tag: str, tipo: TipoHospede, ndias: int, posicao: int) -> None:
        """Cria um Hóspede.
      
        Parâmetros:
        nome (str): O nome do Hóspede.
        tag (str): A tag do Hóspede, que refêrencia como seus Frames foram salvos na pasta Avatares.
        tipo (TipoHospede): O Tipo do Hóspede
        ndias (int): Quantos dias pretende se hospedar.
        posicao (int): Posição horizontal onde seu Avatar irá aparecer.
        """
        super().__init__(tag, Direcao.DIREITA)
        self._nome: str = nome;
        self._tipo: TipoHospede = tipo;
        self._situacao: 'HospedeSituacao' = HospedeSituacao.FORA;
        self._pacienciaTemp: int = 22;
        self._carteira: int = TipoHospede.valorCarteira(tipo, ndias);
        self._totalDias: int = ndias;
        posicao = posicao * 120; #Garantindo que nenhum Avatar fique em cima de outro.
        self._avatar: 'NPC' = NPC(0-posicao, 335, self);
    
    def tituloMensagem(self) -> str:
        """Retorna o título para a MensagemReserva desse Hóspede."""
        if self._totalDias==1: return self._nome+" ficará 1 dia."
        else: return self._nome+" ficará "+str(self._totalDias)+" dias."
    
    def descricao(self) -> str:
        """Retorna um descrição dizendo o Tipo do Hóspede para a MensagemReserva."""
        return "Esse hospede é do tipo "+self._tipo.name.lower()+"."
    
    def carteira_str(self) -> str:
        """Retorna quanto de Dinheiro esse Hóspede tem para a MensagemReserva."""
        txt: str = "R$ "+str(self._carteira)+",00"
        return txt;

    @property
    def cor(self) -> str:
        """Retorna a cor desse Hóspede ao depender do seu Tipo."""
        return TipoHospede.cor(self._tipo);

    @property
    def decremento(self) -> int:
        """Retorna o decremento de paciência do Hóspede, ao depender do seu Tipo."""
        return TipoHospede.decrementoPaciencia(self._tipo);

    @property
    def totalDias(self) -> int:
        """Retorna quantos dias o Hóspede pretender ficar."""
        return self._totalDias;

    @property
    def nome(self) -> str:
        """Retorna o nome do Hóspede."""
        return self._nome;

    @property
    def tipo(self) -> TipoHospede:
        """Retorna o Tipo do Hóspede."""
        return self._tipo;

    @property
    def carteira(self) -> int:
        """Retorna a quantidade de Dinheiro do Hóspede."""
        return self._carteira; 

    def update(self) -> None:
        """Realiza as movimentações do Hóspede."""
        if self._situacao == HospedeSituacao.FORA and self._ponto:
            self._situacao = HospedeSituacao.FILA;
        elif self._situacao == HospedeSituacao.FILA or self._situacao == HospedeSituacao.ATENDIMENTO:
            self._movimentando(self._avatar);
        elif self._situacao == HospedeSituacao.ENTRANDO or self._situacao == HospedeSituacao.SAINDO:
            self._movimentando(self._avatar);
    
    def emAtendimento(self) -> None:
        """Altera a situação do Hóspede para ATENDIMENTO, quando ele é o primeiro da Fila."""
        self._situacao = HospedeSituacao.ATENDIMENTO;
    
    def sendoAtendido(self) -> bool:
        """Retorna True caso o Hóspede esteja em ATENDIMENTO, False caso contrário."""
        return (self._situacao == HospedeSituacao.ATENDIMENTO and not self._ponto);
    
    def cansou(self) -> bool:
        """Retorna True caso o Hóspede já tenha perdido toda a paciência, False caso contrário."""
        if self._pacienciaTemp<=0:
            self._pacienciaTemp=22;
            if self._avatar.consumirPaciencia():
                self._ponto = Ponto.indoEmbora();
                self._situacao = HospedeSituacao.SAINDO;
                return True;
        else: self._pacienciaTemp -= self.decremento;
        return False;        

    def saiu(self) -> bool:
        """Retorna True caso o Hóspede já tenha conclúido seu Trajeto, False caso contrário."""
        if (self._situacao == HospedeSituacao.ENTRANDO or self._situacao == HospedeSituacao.SAINDO) and not self._ponto:
            self._avatar.esconder()
            return True;
        self.update();
        return False;
    
    def enfilerado(self) -> None:
        """Altera a situação do Hóspede para FILA."""
        self._situacao = HospedeSituacao.FILA;
    
    def entrando(self) -> None:
        """Altera a situação do Hóspede para ENTRANDO."""
        self._situacao = HospedeSituacao.ENTRANDO;
    
    def saindo(self) -> None:
        """Altera a situação do Hóspede para SAINDO."""
        self._situacao = HospedeSituacao.SAINDO;
    
    def sumir(self) -> None:
        """Esconde o Avatar do Hóspede."""
        self._avatar.esconder();

    def pagarReserva(self, valor: int) -> int:
        """Retorna o Valor que o Hóspede pagou da sua Reserva.
        
        Parâmetro:
        valor (int): O Preço do Reserva.
        
        Retorna o Valor pago."""
        if self._tipo == TipoHospede.ESPECIAL:
            return (valor+((self._carteira-valor)//2))
        elif self._tipo == TipoHospede.PILANTRA:
            x: int = random.randint(1, 5)
            if x == 1: return valor;
            elif x<4: return (valor//2);
            else: return 0;
        else: return valor;


