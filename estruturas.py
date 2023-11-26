from tupy import *;
from enum import Enum;
from typing import List, Literal;
from personagens import Hospede, TipoHospede;
from controle import DinheiroException, OrcamentoException, RequisitoException;


#CLASSES ENUM (ESTRUTURAS)
class TipoIcone(Enum):
    """
    Ícones que aparecerão no Menu do jogo.
    """
    IGNORE = 0;
    RESERVA = 1;
    MARTELO = 2;
    CAFE = 3;

class QuartoSituacao(Enum):
  """
  Todas as situações possíveis de um Quarto.
  """
  BLOQUEADO: int = 0;
  LIVRE: int = 1;
  OCUPADO: int = 2;
  UPGRADE: int = 3;

class TipoQuarto(Enum):
  """
  Todos tipos possíveis de Quarto.
  """
  SIMPLES: int = 1;
  MASTER: int = 2;
  DELUXE: int = 3;

  @staticmethod
  def cor(tipo: 'TipoQuarto') -> str:
      if tipo==TipoQuarto.SIMPLES: return "Powder Blue";
      elif tipo==TipoQuarto.MASTER: return "Lavender";
      elif tipo==TipoQuarto.DELUXE: return "Olive Drab";

#CLASSES DE NÓ/LISTA (ESTRUTURAS)
class Momento():
    """
    Cada Momento criado deverá ser associado a uma tarefa que o Hotel deve executar,
    sendo o último momento da lista o fim do expediente do Atendente.
    """

    def __init__(self, hora: int, minuto: int) -> None:
        """
        Parâmetros:
        hora (int): hora do momento.
        minuto (int): minuto do momento.

        Retorno: None
        """
        self._hora: int = hora;
        self._minuto: int = minuto;
        self.prox: 'Momento'|None = None;

    @staticmethod
    def _ligarMomentos(lista: List['Momento']) -> 'Momento':
      """
        Parâmetros:
        lista List[Momento]: A lista de momentos para aquele dia.

        A função irá criar uma Lista Simplesmente Encadeada entre todos os Momentos da lista.
        Assim, criando uma Sêquencia de Momentos.

        Retorno: O primeiro Momento da lista.
        """
      m: 'Momento' = lista[0];
      for x in range(1, len(lista)):
          m.prox = lista[x];
          m = lista[x]
      return lista[0];

    @staticmethod
    def _sequenciaMomento() -> 'Momento':
        """
        Cria os Momentos das Tarefas do Hotel.
        Retorno: O primeiro Momento da Sêquencia de Momentos.
        """
        lista: List['Momento'] = [Momento(8, 30), Momento(9, 15), Momento(9, 55), Momento(10, 40), Momento(11, 30), Momento(12, 30)]
        return Momento._ligarMomentos(lista);

    @staticmethod
    def gerarMomentos() -> 'Momento':
        """
        Retorno:
        O primeiro Momento da Sêquencia de Momentos..
        """
        return Momento._sequenciaMomento();

    def horaCerta(self, h: int, m: int) -> bool:
        if self._hora == h and self._minuto == m:
            return True;
        return False;

#CLASSES TUPY (ESTRUTURAS)
class Labelella(Label):
    """
    Sub-classe de Label com o sobreposição no mêtodo _hide()
    """
    def __init__(self, text: str, x: int, y: int, font: str = 'Arial 20', color: str = 'black', anchor: Literal['nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se'] = 'nw') -> None:
        super().__init__(text, x, y, font, color, anchor);
        self._placeholder: str = text;
        #O atributo _placeholder guarda o mesmo valor do atribulo text.
    
    def _hide(self) -> None:
        """
        Reduz o valor do atribulo text para '', 'escondendo' a Labelella.
        """
        self.text = '';

    def _show(self) -> None:
        """
        Recupera o valor original do atibuto text através do atributo _placeholder.
        """
        self.text = self._placeholder;

class Porta(BaseGroup):
    def __init__(self, x: int, y: int, numeroQuarto: str) -> None:
        """
        Cria uma porta de altura e largura predefinidas e com o número do Quarto.

        Parâmetros:
        x (int): Posição horizontal da Porta.
        y (int): Posição vertical da Porta.
        numeroQuarto (str): Número que aparecerá na Porta.
        """
         # x e y são as coordenadas (x-inicial, y-inicial), w será sempre 90 e h será sempre 160, pois todas as portas são iguais
        self._porta: Rectangle = Rectangle(x, y, 90, 160, fill = "Sienna", outline = "Black")
        self._quadro: Rectangle = Rectangle(x+67, y+77, 15, 15, fill = "Peru", outline = "Peru")
        self._macaneta: Oval = Oval(x+70, y+80, 10, 10, outline = 'Black', fill = 'Black')
        self._label_valor: Label = Label(numeroQuarto, x+47, y+15, 'Arial 13', anchor = 'center', color = 'Black')
        self._add(self._porta)
        self._add(self._quadro)
        self._add(self._macaneta)
        self._add(self._label_valor) 

class Salao(BaseGroup):
    def __init__(self) -> None:
        """
        Cria as Estruturas do Hotel.
        """
        #Adicionando os pisos e paredes.
        self._add(Rectangle(0,160, 895, 140, 'Dim Gray', 'Dim Gray'));
        self._add(Rectangle(0, 0, 780, 160, 'Black', 'Wheat'));
        self._add(Rectangle(0,300, 895, 120, 'Dark Gray', 'Dark Gray'));
        self._add(Rectangle(0, 420, 895, 80, 'Gray', 'Moccasin'));

        #Adicionando a escada
        self._add(Rectangle(785, 0, 105, 10, 'Black', 'Slate Gray'));
        self._add(Rectangle(785, 10, 105, 10, 'Black', 'Black'));
        self._add(Rectangle(785, 20, 105, 15, 'Black', 'Slate Gray'));
        self._add(Rectangle(785, 35, 105, 10, 'Black', 'Black'));
        self._add(Rectangle(785, 45, 105, 15, 'Black', 'Slate Gray'));
        self._add(Rectangle(785, 60, 105, 10, 'Black', 'Black'));
        self._add(Rectangle(785, 70, 105, 15, 'Black', 'Slate Gray'));
        self._add(Rectangle(785, 85, 105, 10, 'Black', 'Black'));
        self._add(Rectangle(785, 95, 105, 15, 'Black', 'Slate Gray'));
        self._add(Rectangle(785, 110, 105, 10, 'Black', 'Black'));
        self._add(Rectangle(785, 120, 105, 15, 'Black', 'Slate Gray'));
        self._add(Rectangle(785, 135, 105, 10, 'Black', 'Black'));
        self._add(Rectangle(785, 145, 105, 15, 'Black', 'Slate Gray'));
        self._add(Rectangle(780, 0, 5, 160, 'Black', 'Silver'));
        self._add(Rectangle(890, 0, 5, 160, 'Black', 'Silver'));

        #Adicionando as portas
        self._add(Porta(40, 0, '001'));
        self._add(Porta(160, 0, '002'));
        self._add(Porta(280, 0, '003'));
        self._add(Porta(400, 0, '004'));
        self._add(Porta(520, 0, '005'));
        self._add(Porta(640, 0, '006'));

        #Adicionando as paredes
        self._add(BaseImage(file='estruturas/parede.png', x = 445, y = 270));

        #Adicionando a tabela de preco:
        self._add(Rectangle(15, 235, 250, 115, 'Black', 'Dark Slate Gray'))
        self._add(Label("Tabela de Preços (Diária)", 26, 250, 'Candara 16 bold', 'White', 'w'));
        self._add(Label("R$ 50,00  — Quarto Simples", 30, 275, 'Candara 14 italic', 'Powder Blue', 'w'));
        self._add(Label("R$ 90,00  — Quarto Master", 30, 300, 'Candara 14 italic', 'Lavender', 'w'));
        self._add(Label("R$ 150,00 — Quarto Deluxe", 30, 325, 'Candara 14 italic', 'Olive Drab', 'w'));
        
      
    def addMesa(self) -> None:
        """
        Adiciona a Mesa e seus objetos no Hotel.
        Esse método deve ser chamado após a criação do Avatar do Atendente,
        garantindo que a Mesa sempre esteja na frente do Atendende.
        """
        self._add(BaseImage(file='estruturas/mesa.png', x = 630, y = 370));
        self._add(BaseImage(file='estruturas/cafeteira.png', x = 540, y = 290));
        self._add(BaseImage(file='estruturas/computador.png', x = 540, y = 330));
        self._add(BaseImage(file='estruturas/livros.png', x = 565, y = 380));
        self._add(BaseImage(file='estruturas/chaves.png', x = 680, y = 380));

    def telaFinal(self, dinheiro: int, nReservas: int) -> None:
        resstr: str = str(nReservas);
        if nReservas < 10: resstr="0"+resstr;
        dinstr: str = "R$ "+str(dinheiro)+",00";
        self._add(Rectangle(280, 175, 400, 200, 'white', 'white'))
        self._add(Label("O Jogo acaba por aqui...", 310, 190, "Candara 25 bold", 'Black', 'nw'));
        self._add(Label("Você atendeu "+resstr+" Hóspedes ao logo desses 5 Dias.", 290, 250, "Candara 14", 'Black', 'nw'));
        self._add(Label("E o Hotel ficou com "+dinstr+" de renda.", 290, 280, "Candara 14", 'Black', 'nw'));
        self._add(Rectangle(405, 320, 150, 40, 'silver', 'silver'));
        self._add(Label("Fechar o Jogo", 410, 325, "Candara 18 bold", 'Black', 'nw')); 

    def clicou(self) -> bool:
        if (mouse.x>=405 and mouse.x<=555) and (mouse.y>=320 and mouse.y<=360): return True;
        return False;

class Quadro(BaseGroup):
    def __init__(self, dia: int, dinheiro: int, meta: int) -> None:
        """
        Cria o Quadro de Informações sobre o Hotel.
        O Dia atual, quanto de Dinheiro tem e a Meta de Reservas.

        Parâmetros:
        dia (int): O dia atual do Hotel.
        dinheiro (int): A quantidade de Dinheiro atual do Hotel.
        meta (int): A meta de Reservas para o dia.
        """
        self._rectangle: Rectangle = Rectangle(250, 430, 190, 60, fill = 'Slate Gray', outline = 'Antique White'); 
        self._textoDia: Label = Label("DIA "+str(dia)+":", 255, 430, 'Consolas 16 bold', anchor = 'nw', color = 'White'); 
        self._textoDin: Label = Label("R$ "+str(dinheiro)+",00", 345, 432, 'Consolas 12 italic', anchor = 'nw', color = 'Dark Green'); 
        self._textoRes: Label = Label("Reservas: ", 255, 460, 'Corbel 14 bold', anchor = 'nw', color = 'White');
        self._textoMeta: Label = Label("00 | "+str(meta), 370, 463, 'Consolas 11 italic', anchor = 'nw', color = 'Dark Red'); 
        self._meta: int = meta;
        self._atual: int = 0;
        self._concluida: bool = False;
        self._add(self._rectangle);
        self._add(self._textoDia);
        self._add(self._textoDin);
        self._add(self._textoRes);
        self._add(self._textoMeta);
    
    @property
    def concluida(self) -> bool:
        """
        Retorno:
        Um valor booleano que irá informar se a Meta de Reservas foi ou não concluída.
        """
        return self._concluida;

    def novoDia(self, dia: int, dinheiro: int, meta: int) -> None:
        """
        Atualiza as Informações do Quadro
        
        Parâmetros:
        dia (int): O dia atual do Hotel.
        dinheiro (int): A quantidade de Dinheiro atual do Hotel.
        meta (int): A meta de Reservas para o dia.
        """
        diastr = str(dia);
        if dia<10: diastr='0'+diastr;
        self._textoDia.text = "DIA "+diastr+":";
        self.atualizeDinheiro(dinheiro);
        self._meta = meta;
        self._resetaMeta();

    def atualizeDinheiro(self, dinheiro: int) -> None:
        """
        Atualiza a quantidade de Dinheiro do Hotel.

        Parâmetros:
        dinheiro (int): A quantidade de Dinheiro atual do Hotel.
        """
        strdin: str;
        if dinheiro<9: strdin = "R$ 0"+str(dinheiro)+",00";
        else: strdin = "R$ "+str(dinheiro)+",00";
        self._textoDin.text = str(strdin);

    def _resetaMeta(self) -> None:
        """
        Reseta as Metas de Reservas.
        """
        self._atual = 0;
        strmeta: str;
        if self._meta<10: strmeta="0"+str(self._meta);
        else: strmeta=str(self._meta);
        self._textoMeta.text = "00 | "+strmeta;
        self._concluida = False;
        self._textoMeta.color="Dark Red";

    def atualizeReserva(self) -> None:
        """
        Contabiliza a Reserva concluída para a Meta de Reservas.
        """
        self._atual+=1;
        stratual: str;
        strmeta: str;
        if self._atual<10: stratual="0"+str(self._atual);
        else: stratual=str(self._atual);
        if self._meta<10: strmeta="0"+str(self._meta);
        else: strmeta=str(self._meta);
        self._textoMeta.text = stratual+" | "+strmeta;

        if self._atual == self._meta:
            self._concluida = True;
            self._textoMeta.color="Dark Green";
            toast("Meta de Reservas concluída!", 3000);

class BotaoQuarto(BaseGroup):
    def __init__(self, x: int, y: int, quarto: 'Quarto') -> None:
       self._x = x;
       self._y = y;
       self._rectangle: Rectangle = Rectangle(x, y, 25, 25, fill = quarto.cor, outline = 'black')
       self._texto: Labelella = Labelella(quarto.nome, x+2, y+13, 'Segoe 10 bold', anchor = 'w', color = 'black');
       self._add(self._rectangle);
       self._add(self._texto);

    def atualizarQuarto(self, cor: str) -> None:
        """
        Atualiza a cor do botão, reajustando o aprimoramento do Quarto.
        
        Parâmetro: 
        cor (str): Nome da cor (em inglês) ou seu código hexadecimal.
        """
        self._rectangle.fill = cor;

    def clicou(self) -> bool:
      """
        Retorna um valor booleano informando se o botão foi ou não clicado.
        """
      if (mouse.x>=self._x and mouse.x<=self._x+25) and (mouse.y>=self._y and mouse.y<=self._y+25):
          return True;
      return False;

    def mostrar(self) -> None:
        """Mostra o botão."""
        self._show();

    def esconder(self) -> None:
        """Esconde o botão."""
        self._hide();

class MensagemReserva(BaseGroup):
    def __init__(self) -> None:
        """Cria o molde da Mensagem de Reserva"""
        self._caixa: Rectangle = Rectangle(460, 430, 250, 60, fill = "Indian Red", outline = "Black");
        self._txtH: Label = Label("", 465, 440, 'Consolas 11 bold', anchor = 'w', color = 'Black');
        self._txtT: Label = Label("", 465, 460, 'Consolas 9 italic', anchor = 'w', color = 'Black');
        self._txtC: Label = Label("", 465, 480, 'Consolas 9', anchor = 'w', color = 'Dark Green');
        self._caixaC: Rectangle = Rectangle(695, 433, 10, 10, fill = "Dark Red", outline = "Dark Red");
        self._botaoC: Labelella = Labelella("x", 697, 437, 'Arial 10', anchor = 'w', color = 'White');
        self._add(self._caixa);
        self._add(self._txtH);
        self._add(self._txtT);      
        self._add(self._txtC);      
        self._add(self._caixaC);
        self._add(self._botaoC);
        self._vazia = True;
        self._hide();

    @property
    def vazia(self) -> bool:
        """Retorna se a Mensagem está ou não vazia."""
        return self._vazia;

    def alterarMensagem(self, hospede: 'Hospede') -> None:
        """
        Altera as informações da Mensagem para o novo Hóspede.

        Parâmetros:
        hospede (Hospede): O Hóspede que está sendo atendido.
        """
        self._txtH.text = hospede.tituloMensagem();
        self._txtT.text = hospede.descricao();
        self._txtC.text = "Carteira: "+hospede.carteira_str();
        self._vazia = False;
        self._show()

    def clicou(self) -> bool:
        """Retorna um valor booleano informando se o botão foi clicado ou não.
        
        Caso o botão foi clicado, a Mensagem é escondida."""
        if self._vazia: return False;
        if (mouse.x>=697 and mouse.x<=707) and (mouse.y>=433 and mouse.y<=443):
            self._hide();
            return True;
        return False;

    def esconder(self) -> None:
        """Esconde a Mensagem"""
        self._vazia = True;
        self._hide();

class Relogio(BaseGroup):
    """O Relógio do Hotel."""
    IGNORE: int = 0
    TAREFA: int = 1
    ANOITECEU: int = 2

    def __init__(self) -> None:
        """Cria o Relógio."""
        self._hora: int = 8;
        self._minuto: int = 20;
        self._temporizador: int = 20;
        self._momento: 'Momento'|None = None;
        self._rectangle: Rectangle = Rectangle(730, 430, 150, 60, fill = 'gray', outline = 'black');
        self._texto: Label = Label(self._horaAtual(), 805, 435, 'Arial 36 bold', anchor = 'n', color = 'dark green');
        self._add(self._rectangle);
        self._add(self._texto);
    
    def cronograma(self, m: 'Momento') -> None:
        """Adiciona uma Sequência encadeada de Momentos no Relógio."""
        self._momento = m;
        self._temporizador = 20;
        self._hora = 8;
        self._minuto = 20;

    def _horaAtual(self) -> str:
        """Atualiza a Hora."""
        strhora = str(self._hora);
        strminuto = str(self._minuto);

        if(self._hora <10): strhora = "0"+strhora;
        if(self._minuto <10): strminuto = "0"+strminuto;

        return strhora+":"+strminuto
    
    def _atualizarTempo(self) -> None:
        if self._minuto==59:
            self._minuto=0;
            self._hora+=1;
        else:
            self._minuto+=1;

        self._texto.text = self._horaAtual();
    
    def ticTac(self) -> int:
        """Faz o tempo passar...
        Retorna a Tarefa daquele Momento."""
        if(self._momento):
            if self._temporizador<=1: 
              self._atualizarTempo();
              self._temporizador = 20;
              if self._momento.horaCerta(self._hora, self._minuto):
                if self._momento.prox:
                    self._momento = self._momento.prox;
                    return Relogio.TAREFA;
                self._momento = None;
                return Relogio.ANOITECEU
              return self.IGNORE
            else: self._temporizador-=1;
        return Relogio.IGNORE

#CLASSES PRINCIPAIS
class Icone():
    def __init__(self, imagem: str, x: int, y: int, tipo: 'TipoIcone') -> None:
        self._imagem: str = imagem;
        self._ligado: bool = False
        self._botao: Image = Image(self._pegarImagem(), x, y);
        self._x: int = x;
        self._y: int = y;
        self._tipo = tipo;

    @property
    def tipo(self) -> TipoIcone:
        return self._tipo;

    def _pegarImagem(self) -> str:
        """
        Retorno:
        endereço da Imagem do Ícone.
        
        Há 2 endereços para cada Ícone, um 'Ligado' e outro 'desligado'."""
        txt: str = ''
        if self._ligado: txt='estruturas/'+self._imagem+"L.png";
        else: txt='estruturas/'+self._imagem+"A.png";
        return txt;

    def _alterarImagem(self) -> None:
        """Altera a Imagem do Ícone."""
        self._botao.file = self._pegarImagem();
    


    def mudar(self, estado: bool) -> None:
        """Muda a Imagem do Ícone.
        Parâmetros:
        estado (bool): O estado do Ícone, sendo True = Ligado e False = Desligado.
        """
        self._ligado = estado;
        self._alterarImagem();

class Menu():
    def __init__(self) -> None:
      """Cria o Menu com 3 Ícones."""
      self._iconR = Icone('iconR', 40, 460, TipoIcone.RESERVA);
      self._iconM = Icone('iconM', 120, 460, TipoIcone.MARTELO);
      self._iconC = Icone('iconC', 200, 460, TipoIcone.CAFE);
    
    def padrao(self) -> TipoIcone:
        """
        Ajusta as imagens dos Ícones para o Padrão:
        Ícone de Reservas ligado.
        Ícone de Melhoras apagado.
        Ícone de Café apagado.
        """
        self._iconR.mudar(True)
        self._iconM.mudar(False)
        self._iconC.mudar(False)
        return self._iconR.tipo;

    def encerrou(self) -> None:
        """
        Desliga todos os Ícones, fim do expediente."""
        self._iconR.mudar(False)
        self._iconM.mudar(False)
        self._iconC.mudar(False)

    def update(self) -> TipoIcone:
        """
        Testa se algum Tecla foi clicada.
        
        Retorno:
        O TipoIcone correspondente a Tecla clicada (R, M, C).
        Caso nenhuma das teclas foi clicada, retorna um IGNORE.
        """
        if keyboard.is_key_just_down('r'): return self._iconR.tipo;
        elif keyboard.is_key_just_down('m'): return self._iconM.tipo;
        elif keyboard.is_key_just_down('c'): return self._iconC.tipo;
        return TipoIcone.IGNORE;

    def mudeIcon(self, icone: TipoIcone) -> None:
        """
        Muda a situação das imagens dos Ícones de acordo com o Ícone selecionado.

        Parâmetro:
        icone (TipoIcone): o TipoIcone selecionado.
        """
        if icone == TipoIcone.MARTELO: 
            self._iconR.mudar(False);
            self._iconM.mudar(True);
            self._iconC.mudar(False);
        elif icone == TipoIcone.CAFE: 
            self._iconR.mudar(False);
            self._iconM.mudar(False);
            self._iconC.mudar(True);
        else:
            self._iconR.mudar(True);
            self._iconM.mudar(False);
            self._iconC.mudar(False);     

class Quarto():
    def __init__(self, tipo: TipoQuarto, situacao: QuartoSituacao, andar: int, numero: int, x: int, y: int) -> None:
            """
            Cria um Quarto para o Hotel.

            Parâmetros:
            tipo (TipoQuarto): O tipo do Quarto (Simples, Master, Deluxe).
            situacao (QuartoSituacao): A situação do quarto.
            andar (int): O andar do Quarto.
            numero (int): O número do Quarto.
            x (int): posição horizontal do Botão do Quarto.
            y (int): posição vertical do Botão do Quarto.
            """
            
            self._andar: int = andar;
            self._numero: int = numero;
            self._tipo: TipoQuarto = tipo
            self._preco: int = 0;
            self._situacao: QuartoSituacao = situacao;
            self._reserva: 'Reserva'|None = None;
            self._definirPreco()
            self._visivel = False
            self._botao: 'BotaoQuarto' = BotaoQuarto(x, y, self);
            self.ajustarLiberdo();

    @staticmethod
    def criarQuartos() -> List['Quarto']:
        """
        Cria os Quartos do Hotel."""
        q01 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 0, 1, 650, 235);
        q02 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 0, 2, 680, 235);
        q03 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 0, 3, 710, 235);
        q04 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 0, 4, 740, 235);
        q05 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 0, 5, 770, 235);
        q06 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 0, 6, 800, 235);
        q07 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 0, 7, 830, 235);
        q08 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 0, 8, 860, 235);

        q09 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 1, 1, 650, 265);
        q10 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 1, 2, 680, 265);
        q11 = Quarto(TipoQuarto.MASTER, QuartoSituacao.LIVRE, 1, 3, 710, 265);
        q12 = Quarto(TipoQuarto.MASTER, QuartoSituacao.LIVRE, 1, 4, 740, 265);
        q13 = Quarto(TipoQuarto.MASTER, QuartoSituacao.LIVRE, 1, 5, 770, 265);
        q14 = Quarto(TipoQuarto.MASTER, QuartoSituacao.LIVRE, 1, 6, 800, 265);
        q15 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 1, 7, 830, 265);
        q16 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.LIVRE, 1, 8, 860, 265);

        q17 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 2, 1, 650, 295);
        q18 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 2, 2, 680, 295);
        q19 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 2, 3, 710, 295);
        q20 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 2, 4, 740, 295);
        q21 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 2, 5, 770, 295);
        q22 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 2, 6, 800, 295);
        q23 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 2, 7, 830, 295);
        q24 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 2, 8, 860, 295);

        q25 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 3, 1, 650, 325);
        q26 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 3, 2, 680, 325);
        q27 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 3, 3, 710, 325);
        q28 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 3, 4, 740, 325);
        q29 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 3, 5, 770, 325);
        q30 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 3, 6, 800, 325);
        q31 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 3, 7, 830, 325);
        q32 = Quarto(TipoQuarto.SIMPLES, QuartoSituacao.BLOQUEADO, 3, 8, 860, 325);

        return [q01, q02, q03, q04, q05, q06, q07, q08, q09, q10, q11, q12, q13, q14, q15, q16,\
                q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32]
    
    def _definirPreco(self) -> None:
        """Define o Preço do Quarto associado a seu Tipo."""
        if self._tipo==TipoQuarto.SIMPLES: self._preco = 50;
        elif self._tipo==TipoQuarto.MASTER: self._preco = 90;
        elif self._tipo==TipoQuarto.DELUXE: self._preco = 150;

    @property
    def nome(self) -> str:
        """Retorna o Nome do Quarto (Andar + Número)."""
        numerostr = str(self._numero);
        if self._numero<10: numerostr="0"+numerostr;
        return str(self._andar)+numerostr;

    @property
    def cor(self) -> str:
        """Retorna a Cor do quarto associado a seu Tipo.
        Caso o Quarto esteja Bloqueado, a cor será transparente."""
        if self._situacao == QuartoSituacao.BLOQUEADO: return ""
        return TipoQuarto.cor(self._tipo);

    @property
    def andar(self) -> int:
        """Retorna o Andar do Quarto."""
        return self._andar;

    @property
    def numero(self) -> int:
        """Retorna o Número do Quarto."""
        return self._numero;

    @property
    def preco(self) -> int:
        """Retorna o Preço do Quarto."""
        return self._preco;

    @property
    def tipo(self) -> TipoQuarto:
        """Retorna o Tipo do Quarto."""
        return self._tipo;

    def bloqueado(self) -> bool:
        """Retorna um valor booleando informando se o Quarto está ou não bloqueado."""
        if self._situacao==QuartoSituacao.BLOQUEADO: return True;
        return False;

    def aprimorando(self) -> bool:
        """Retorna um valor booleando informando se o Quarto está ou não em processo de aprimoramento."""
        if self._situacao==QuartoSituacao.UPGRADE: return True;
        return False;

    def aprimorado(self) -> None:
        """Finaliza o processo de Aprimoramento de um Quarto."""
        self._situacao=QuartoSituacao.LIVRE;
        self._botao.atualizarQuarto(TipoQuarto.cor(self._tipo))

    def livre(self) -> bool:
        """Retorna se o Quarto está desocupado."""
        if self._reserva: return False;
        return True;

    def _liberado(self) -> None:
        """Remove a Reserva do Quarto."""
        self._reserva = None;
        self._situacao = QuartoSituacao.LIVRE;

    def ajustarLiberdo(self) -> None:
        """Mostra ou Esconde o Botão do Quarto ao decorrer da sua Situação."""
        if self._reserva or self._situacao != QuartoSituacao.LIVRE:
            self._esconderBotao();
        else: self._mostrarBotao();

    def podeAprimorar(self) -> None:
        """Esconde ou Mostra o Botão do Quarto ao decorrer se ele é ou não apto a melhorias."""
        if self._situacao == QuartoSituacao.BLOQUEADO: self._mostrarBotao();
        elif self._tipo == TipoQuarto.MASTER and self.andar==0: self._esconderBotao();
        elif self._situacao == QuartoSituacao.OCUPADO: self._esconderBotao();
        elif self._tipo == TipoQuarto.DELUXE: self._esconderBotao();
        elif self._situacao == QuartoSituacao.UPGRADE: self._esconderBotao();
        elif self._situacao == QuartoSituacao.LIVRE: self._mostrarBotao();

    def _mostrarBotao(self) -> None:
        self._botao.mostrar();
        self._visivel = True;
    
    def _esconderBotao(self) -> None:
        """Esconde o Botão do Quarto."""
        self._botao.esconder();
        self._visivel = False;

    def testarClick(self) -> bool:
        """Testa se o Botão do Quarto foi clicado."""
        if not self._visivel: return False;
        return self._botao.clicou();

    def criarReserva(self, hospede: 'Hospede', hoje: int) -> None:
        """Cria uma Reserva.
        
        Parâmetros:
        hospede (Hospede): O Hóspede que irá se reservar no Quarto.
        hoje (int): Dia atual do Hotel.
        """
        self._esconderBotao();
        self._reserva = Reserva(hoje, self._preco, hospede);
        self._situacao = QuartoSituacao.OCUPADO;

    def acabou(self, hoje: int) -> bool:
        """Informa se a Reserva do Quarto acabou ou não ao decorrer do Dia atual.
        
        Parâmetro:
        hoje (int): Dia atual do Hotel."""
        if self._reserva: 
            return self._reserva.acabou(hoje);
        return False;
    
    def pegarPagamento(self) -> int:
        """Retorna o pagamento da Reserva do Quarto e finaliza a Reserva."""
        if self._reserva:
            pagamento: int = self._reserva.finalizarReserva()
            self._liberado();
            return pagamento;
        else: return 0;

    def melhorarQuarto(self, dinheiro: int) -> int:
        """Inicia o processo de aprimoramento no Quarto, se houver Dinheiro o suficiente.
        
        Parâmetro:
        dinheiro (int): Quantidade de Dinheiro autal do Hotel."""
        preco: int = 0;
        if self._situacao == QuartoSituacao.BLOQUEADO:
            if dinheiro < 100: raise OrcamentoException("O Hotel não tem orçamento para liberar esse Quarto.");
            self._tipo = TipoQuarto.SIMPLES;
            toast("Quarto "+self.nome+" foi desbloqueado, amanhã estará disponível! (-100 R$)", 3000);
            preco = 100;
        elif self._tipo == TipoQuarto.SIMPLES:
            if dinheiro < 150: raise OrcamentoException("O Hotel não tem orçamento para liberar esse Quarto.");
            self._tipo = TipoQuarto.MASTER;
            toast("Quarto "+self.nome+" foi aprimorado, amanhã estará disponível! (-150 R$)", 3000);
            preco = 150;
        elif self._tipo == TipoQuarto.MASTER:
            if dinheiro < 250: raise OrcamentoException("O Hotel não tem orçamento para liberar esse Quarto.");
            self._tipo = TipoQuarto.DELUXE;
            toast("Quarto "+self.nome+" foi aprimorado, amanhã estará disponível! (-250 R$)", 3000);
            preco = 250;
        self._situacao = QuartoSituacao.UPGRADE;
        self._definirPreco();
        self._esconderBotao();
        return preco;

    def validarResquisitos(self, hospede: Hospede) -> None:
        """Verifica se o Quarto cumpre os resquisitos do Hóspede."""
        if hospede.tipo == TipoHospede.AVARENTO and (self._tipo != TipoQuarto.SIMPLES or self._andar!=0):
            raise RequisitoException(hospede.nome+" não aceita ficar nesse tipo de quarto!");
        elif hospede.tipo == TipoHospede.ORGULHOSO and self._tipo == TipoQuarto.SIMPLES:
            raise RequisitoException(hospede.nome+" não aceita ficar nesse tipo de quarto!");
        elif hospede.carteira < (self._preco*hospede.totalDias):
            raise DinheiroException(hospede.nome+" não possui dinheiro o suficiente!");

class Reserva():
    def __init__(self, diaEntrada: int, quartoPreco: int, hospede: 'Hospede') -> None:
            """Cria uma Reserva.
            
            Parâmetros:
            diaEntrada (int): Dia atual do Hotel.
            quartoPreco (int): Preço do Quarto.
            hospede (Hospede): Hóspede da Reserva.
            """
            self._diaEntrada: int = diaEntrada;
            self._diaSaida: int = diaEntrada+hospede.totalDias;
            self._preco: int = quartoPreco*hospede.totalDias;
            self._hospede: 'Hospede' = hospede;

    def acabou(self, dia: int) -> bool:
        """Informa se é o dia final da Reserva.
        
        Parâmetro:
        dia (int): Dia atual do Hotel."""
        if dia==self._diaSaida: return True;
        return False;

    def finalizarReserva(self) -> int:
        """Finaliza a Reserva e retorna o valor pago pelo Hóspede."""
        return self._hospede.pagarReserva(self._preco);
