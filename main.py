from tupy import *;
from typing import List, Optional;
from estruturas import Momento, Salao, Relogio, TipoIcone, Menu, MensagemReserva, Quadro, Quarto;
from personagens import Ponto, FilaNo, Personagem, Atendente, Hospede;
from controle import *;

class Hotel():
    """Classe Principal do Jogo"""
    def __init__(self) -> None:
        """Cria o Hotel com seu Salão, Quartos, Menu, Relógio e Atendente."""
        self._salao: 'Salao' = Salao();
        self._menu: 'Menu' = Menu();
        self._selecao: TipoIcone = TipoIcone.RESERVA;

        self._quartos: List['Quarto'] = Quarto.criarQuartos();
        self._atendente: 'Atendente' = Atendente();
        self._salao.addMesa(); #Esse mêtodo garante que o Atendente sempre ficará atrás da Mesa.
        self._relogio: 'Relogio' = Relogio();

        self._dinheiro: int = 500;
        self._numDia: int = 0;
        self._quadro: 'Quadro' = Quadro(1, self._dinheiro, 12);
        self._noite: bool = False;
        self._metas: List[int] = [0, 12, 15, 18, 20, 23]
        self._numTarefa: int = 1;
        self._reservasCont = 0;
        self._fila: 'FilaNo'|None = None;
        self._reservaMsg: MensagemReserva = MensagemReserva()
        self._saindo: List['Personagem'] = [];

    def comecar(self) -> None:
        """Começa o Jogo."""
        self._amanheceu();
    
    def _amanheceu(self) -> None:
        """Inicia o Dia no Hotel."""
        self._numDia += 1;
        self._relogio.cronograma(Momento.gerarMomentos());
        self._atendente.boraTrabalhar();
        self._selecao = TipoIcone.RESERVA;
        self._menu.padrao();
        self._mostrarQuartosLivres();
        self._quadro.novoDia(self._numDia, self._dinheiro, self._metas[self._numDia]);
    
    def _anoiteceu(self) -> None:
        """Finaliza o Dia no Hotel."""
        self._numTarefa = 1;
        self._reservaMsg.esconder();
        if self._fila:
            no: FilaNo|None = self._fila;
            while(no):
                self._saindo.append(no.hospede);
                no.hospede.trajeto(Ponto.indoEmbora());
                no.hospede.saindo();
                no = no.prox;
        self._saindo.append(self._atendente);
        self._atendente.fimDoTrabalho();
        self._selecao = TipoIcone.RESERVA;
        self._menu.encerrou();
    
    def _tarefa(self) -> None:
        """Adiciona novos Hóspedes."""
        posicao: int = 0;
        if self._fila: posicao = self._fila.tamanho+1;
        self._fila = FilaNo.entrarNaFila(self._fila, criarHospedes(self._numDia, self._numTarefa, posicao));
        self._numTarefa += 1;
    
    def recolherPagamento(self) -> None:
        """Finaliza as Reservas dos Quartos e recolhe os Pagamentos."""
        inicial: int = self._dinheiro;
        for x in self._quartos:
            if x.acabou(self._numDia+1):
                self._dinheiro += x.pegarPagamento();
        strdin: str = str(self._dinheiro-inicial);
        if self._dinheiro-inicial<10: strdin="0"+strdin;
        toast("Você faturou R$ "+strdin);
    
    def inaugurarQuartos(self) -> None:
        """Liberar os Quartos que estavam em aprimoramento."""
        for x in self._quartos:
            if x.aprimorando(): x.aprimorado();
    
    def _aquelesQueSeForam(self) -> None:
        """Limpa a Lista dos Personagens que estão se movimentando."""
        novaLista: List['Personagem'] = [];
        for x in self._saindo:
            if not x.saiu(): novaLista.append(x);
        self._saindo = novaLista;
    
    def _mostrarQuartosLivres(self) -> None:
        """Mostra os Botões dos Quartos que podem ser reservados."""
        for x in self._quartos: x.ajustarLiberdo();
    
    def _mostrarInferiores(self) -> None:
        """Mostra os botões dos Quartos que podem ser melhorados."""
        for x in self._quartos: x.podeAprimorar()
    
    def _tentarMelhorar(self, q: Quarto) -> None:
        """Tenta aprimorar algum Quarto."""
        if self._dinheiro == 0: raise OrcamentoException('Sem dinheiro para isso!');
        valor: int = q.melhorarQuarto(self._dinheiro);
        self._dinheiro -= valor;
        self._quadro.atualizeDinheiro(self._dinheiro);

    def _tentarReservar(self, q: Quarto) -> None:
        """Tenta reservar algum Quarto."""
        if self._fila:
            if not self._fila.hospede.parado(): raise PressaException("Aguarde o Hóspede!");
            cliente: Hospede = self._fila.hospede;
            q.validarResquisitos(cliente);
            toast(cliente.nome+" se reservou conosco!");
            self._reservasCont += 1;
            self._fila = FilaNo.sairDaFila(self._fila, 1);
            if not self._quadro.concluida: 
                self._quadro.atualizeReserva();
                if self._quadro.concluida: 
                    self._dinheiro+=100;
                    self._quadro.atualizeDinheiro(self._dinheiro);
                
            if q.andar>0: cliente.trajeto(Ponto.caminhoEscadas());
            elif q.numero==4: cliente.trajeto(Ponto.caminhoAte004());
            elif q.numero>6: cliente.trajeto(Ponto.caminhoQuartoEscondido());
            else: cliente.trajeto(Ponto.caminhoQuarto(q.numero));
            cliente.entrando()
            self._saindo.append(cliente);
            q.criarReserva(cliente, self._numDia);
            self._reservaMsg.esconder();

    def update(self) -> None:
        if self._numDia==2: 
            if self._salao.clicou(): exit();
        
        elif not self._noite:
            respostaRelogio: int = self._relogio.ticTac();
            if respostaRelogio!=2: 
                if respostaRelogio==1: 
                    self._tarefa();
                    self._aquelesQueSeForam();
            else:
                self._noite = True;
                self._anoiteceu();
                return None;  
            if self._reservaMsg.vazia:
                if self._fila and self._fila.hospede.sendoAtendido(): self._reservaMsg.alterarMensagem(self._fila.hospede);

            respostaMenu: TipoIcone = self._menu.update()
            if not self._atendente.andando() and respostaMenu != TipoIcone.IGNORE:
                if respostaMenu == TipoIcone.CAFE:
                    self._menu.mudeIcon(respostaMenu);
                    self._atendente.beba()
                elif respostaMenu == TipoIcone.MARTELO:
                    self._selecao = TipoIcone.MARTELO;
                    self._mostrarInferiores()
                    self._atendente.volteAoTrabalho();
                    self._menu.mudeIcon(self._selecao);
                else: 
                    self._selecao = TipoIcone.RESERVA;
                    self._mostrarQuartosLivres();
                    self._atendente.volteAoTrabalho();
                    self._menu.mudeIcon(self._selecao);
            
            if self._atendente.bebendo() and self._atendente.cheio():
                toast("Volte ao trabalho!");
                self._menu.padrao();
                self._atendente.volteAoTrabalho()
                self._mostrarQuartosLivres();
                self._selecao = TipoIcone.RESERVA;
            
            self._atendente.update();

            if self._fila:
                if self._fila.hospede.parado(): self._fila.hospede.emAtendimento();
                no: FilaNo|None = self._fila;
                while(no and no.posicao<4):
                    no.hospede.update();
                    if no.hospede.cansou(): 
                        toast(no.hospede.nome+" perdeu a paciência!", 3000);
                        no.hospede.saindo();
                        self._fila = FilaNo.sairDaFila(self._fila, no.posicao);
                        if no.posicao==1: self._reservaMsg.esconder();
                        self._saindo.append(no.hospede);
                        break;
                    no = no.prox;

            for x in self._saindo: x.saiu();
        
            if self._atendente.atendendo() and mouse.is_button_just_down():
                if self._fila and self._reservaMsg.clicou():
                    if self._atendente.exausto(): 
                        toast('Você precisa beber café!', 3000);
                        return None;
                    self._fila.hospede.trajeto(Ponto.indoEmbora());
                    self._fila.hospede.saindo();
                    self._saindo.append(self._fila.hospede);
                    toast("Você não quis atender "+ self._fila.hospede.nome);
                    self._fila = FilaNo.sairDaFila(self._fila, 1);
                    self._reservaMsg.esconder();
                else:
                    escolhido: Quarto|None = None
                    for q in self._quartos:
                        if q.testarClick():
                            escolhido = q;
                            break;
                    if escolhido: 
                        if self._atendente.exausto(): 
                            toast('Você precisa beber café!', 3000);
                            return None;
                        if self._selecao == TipoIcone.RESERVA:
                            try:
                                self._tentarReservar(escolhido)
                            except RequisitoException as re: toast(str(re), 3000);
                            except DinheiroException as de: toast(str(de), 3000);
                            except PressaException as pe: toast(str(pe), 3000);
                            
                        elif self._selecao == TipoIcone.MARTELO:
                            try:
                                self._tentarMelhorar(escolhido);
                                self._menu.padrao();
                                self._selecao = TipoIcone.RESERVA;
                                self._mostrarQuartosLivres();
                            except OrcamentoException as oe: toast(str(oe), 3000);
        
        else:
            if len(self._saindo)!=0: self._aquelesQueSeForam();
            else:
                self.inaugurarQuartos();
                self.recolherPagamento();
                self._amanheceu();
                if self._numDia == 2: self._salao.telaFinal(self._dinheiro, self._reservasCont);
                self._noite = False;
        

meuHotel = Hotel();
meuHotel.comecar();

def update() -> None:
   meuHotel.update();

run(globals())
        
