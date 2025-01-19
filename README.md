<h2>Hotel Tupy é uma simulação de um Hotel, onde você deve gerenciar as reservas de quartos, melhorar e desbloquear mais quartos para o hotel e não perder suas energias.</h2>

<i>Trabalho para a matéria MATA55 - Programação Orientada a Objetos, UFBA 2023.</i>

<h3>No Hotel Tupy você é um <b>Atendente estagiando em um Hotel</b>. Seu turno é das <b>8h30 até 12h30</b>. Você deve gerenciar as reservas dos hóspedes para os quartos que atendam seus requisitos.</h3>

<h3>Suas funções são:</h3>
<ul>
<li><b>Reservas quarto</b>: Clicando na tecla <b>R</b>, você poderá escolher qual quarto o hospede que está sendo atendido irá se hospedar. Caso o quarto cumpra os requisitos do hóspede, ele irá para o quarto. </li>
<li> <b>Melhorar os quartos</b>b>: Clicando na tecla <b>M</b>, você poderá desbloquear ou aprimorar um quarto. O quarto que entrar em processo de aprimoramento ficará indisponível, mas no próximo dia estará disponível novamente.</li>
<li>Beber café: Clicando na tecla <b>C</b>, você recarrega as energias do atendente. Ao passar do tempo o atendente vai ficando cansado, se ele ficar <b>exausto</b> será incapaz de executar as outras funções.</li>
</ul>

<i>Você pode realizar uma função por vez. Quando você escolher um quarto para aplicar melhorias ou estiver satisfeito com o café, você voltará para a função de reservar quartos.</i>

<i>Para escolher o quarto que irá ser reserva ou que irá entrar em processo de aprimoramento, basta clicar no botão do quarto corresponde atrás da mesa do atendente. Um quarto so pode ser reservado se estiver livre e desbloqueado, assim como so poderá aplicar melhorias em quartos livres ou bloqueados.</i>

<h3>Sobre os quartos: </h3>
Há 3 tipos de Quartos:
<ul>
<li> <b>SIMPLES</b>. Que a diária custa R$ 50,00. </li>
<li> <b>MASTER</b>. Que a diária custa R$ 90,00. </li>
<li> <b>DELUXE</b>. Que a diária custa R$ 150,00. </li>
</ul>

<i>Um quarto SIMPLES pode ser aprimorado para um quarto MASTER. Um quarto MASTER pode ser aprimorado para um quarto DELUXE, desde que não esteja no térreo (andar 0). E os quartos DELUXE não recebem melhorias.</i>

<h3>Sobre os hóspedes:</h3>
Os hóspedes irão surgindo em certos momentos. Todo hóspede terá a quantidade máxima de dinheiro que tem para pagar o quarto e quantos dias querem ficar hospedados. 
Os hóspedes também tem uma barra de paciência. Quando eles estão na fila esperando sua barra de paciência vai diminuindo, até que eles percam a paciência e saiam do hotel ou sejam atendidos por você.

Os tipos de hóspedes:

<ul>
<li> <b>REGULAR</b>: Esses hóspedes não tem exigências de quartos, eles podem ficar hospedados em qualquer quarto desde tenha dinheiro suficiente para pagá-los. A cor da barra de paciência desse hóspede é azul. </li>
<li> <b>IMPACIENTE</b>: Esses hóspedes odeiam ficar no segundo e terceiro andar, pois é muito longe, além de que eles são os que perdem a paciencia mais rápido. A cor da barra de paciência desse hóspede é vermelha. </li>
<li> <b>AVARENTO</b>: Esses hóspedes aceitam ficar somente em quartos SIMPLES. São menos pacientes do que um RELUGAR, mas são mais pacientes do que um IMAPACIENTE. A cor da barra de paciência desse hóspede é cinza. </li>
<li> <b>ORGULHOSO</b>: Esses hóspedes querem ficar em quartos MASTER ou DELUXE. São tão pacientes como um AVARENTO. A cor da barra de paciência desse hóspede é rosa. </li>
<li> <b>PILANTRA</b>: Mesmo tendo dinheiro o suficiente, esses hóspedes tem chances de sair sem pagar ou pagar somente a metade da reserva, com sorte pagará todo o preço. Não se hospedam no térreo e são tão pacientes quanto um REGULAR. A cor da barra de paciência desse hóspede é verde. </li>
<li> <b>ESPECIAL</b>: Esses hóspedes são bastantes pacientes, como um REGULAR, e não tem exigências de quarto. Quando chegar a hora de pagar a reservas, eles irão te dar uma gorjeta. A cor da barra de paciência desse hóspede é amarela. </li>
</ul>
  
<h3> Mais sobre o Jogo: </h3>
<b>Quando o hóspede foro primeiro da fila, aparecerá uma mensagem no canto inferior dizendo as informações do hóspede (quantos dias pretende ficar, quanto de dinheiro tem e seu tipo). Tente hospedá-lo de forma que obtenha o melhor lucro, sem atrapalhar os futuros hóspedes.</b>
  
<b>Você pode mandar um hóspede ir embora esperando ele perder a paciência ou clicando no X da sua mensagem de reserva. Os hóspedes pagarão o valor da reserva quando seu reserva vencer. Ou seja, quando desocuparem os quartos.</b>

<b>Ao lado dos ícones de qual atividade o atendente está fazendo, há uma caixa cinza que informa o dia atual do hotel, a quantidade de dinheiro e uma meta de reserva para aquele dia. Batendo a meta você recebe mais R$ 100,00.</b> <br>

<b>Inicialmente você terá R$ 700,00 para investir em melhorias no hotel. A simulação tem duração de 5 dias.</b>

<i>A confecção dos avatares e alguns itens do cenário são originalmente do jogo Habbo Hotel.</i>
