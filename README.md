Hotel Tupy é uma simulação de um Hotel, onde você deve gerenciar as reservas de quartos, melhorar e desbloquear mais quartos para o hotel e não perder suas energias.
trabalho para a matéria MATA55 - Programação Orientada a Objetos, UFBA 2023.

No Hotel Tupy você é um Atendente estagiando em um Hotel. Seu turno é das 8h30 até 12h30.
Você deve gerenciar as reservas dos hóspedes para os quartos que atendam seus requisitos.

Suas funções são:
- Reservas quarto: Clicando na tecla R, você poderá escolher qual quarto o hospede que está sendo atendido irá se hospedar. Caso o quarto cumpra os requisitos do hóspede, ele irá para o quarto.
- Melhorar os quartos: Clicando na tecla M, você poderá desbloquear ou aprimorar um quarto. O quarto que entrar em processo de aprimoramento ficará indisponível, mas no próximo dia estará disponível novamente.
- Beber café: Clicando na tecla C, você recarrega as energias do atendente. Ao passar do tempo o atendente vai ficando cansado, se ele ficar exausto será incapaz de executar as outras funções.
Você pode realizar uma função por vez. Quando você escolher um quarto para aplicar melhorias ou estiver satisfeito com o café, você voltará para a função de reservar quartos. 
Para escolher o quarto que irá ser reserva ou que irá entrar em processo de aprimoramento, basta clicar no botão do quarto corresponde atrás da mesa do atendente. Um quarto so pode ser reservado se estiver livre e desbloqueado, assim como so poderá aplicar melhorias em quartos livres ou bloqueados.

Sobre os quartos: 
Há 3 tipos de Quartos:
- SIMPLES. Que a diária custa R$ 50,00.
- MASTER. Que a diária custa R$ 90,00.
- DELUXE. Que a diária custa R$ 150,00.

Um quarto SIMPLES pode ser aprimorado para um quarto MASTER. Um quarto MASTER pode ser aprimorado para um quarto DELUXE, desde que não esteja no térreo (andar 0). E os quartos DELUXE não recebem melhorias.

Sobre os hóspedes:
Os hóspedes irão surgindo em certos momentos. Todo terá a quantidade máxima de dinheiro que tem para pagar o quarto e quantos dias querem ficar hospedados. 
Os hóspedes também tem uma barra de paciência. Quando eles estão na fila esperando sua barra de paciência vai diminuindo, até que eles percam a paciência e saiam do hotel ou sejam atendidos por você.

Os tipos de hóspedes:
- REGULAR: Esses hóspedes não tem exigências de quartos, eles podem ficar hospedados em qualquer quarto desde tenha dinheiro suficiente para pagá-los. A cor da barra de paciência desse hóspede é azul.
- IMPACIENTE: Esses hóspedes odeiam ficar no último andar, pois é muito longe, além de que eles são os que perdem a paciencia mais rápido. A cor da barra de paciência desse hóspede é vermelha.
- AVARENTO: Esses hóspedes somente aceitam ficar em quartos SIMPLES e no térreo. São menos pacientes do que um RELUGAR, mas são mais pacientes do que um IMAPACIENTE. A cor da barra de paciência desse hóspede é cinza.
- ORGULHOSO: Esses hóspedes querem ficar em quartos MASTER ou DELUXE. São tão pacientes como um AVARENTO. A cor da barra de paciência desse hóspede é rosa.
- PILANTRA: Mesmo tendo dinheiro o suficiente, esses hóspedes tem chances de sair sem pagar ou pagar somente a metade da reserva, com sorte pagará todo o preço. Não tem exigências de quartos e são tão pacientes quanto um REGULAR. A cor da barra de paciência desse hóspede é verde.
- ESPECIAL: Esses hóspedes são bastantes pacientes, como um REGULAR, e não tem exigências de quarto. Quando chegar a hora de pagar a reservas, eles irão te dar uma gorjeta. A cor da barra de paciência desse hóspede é amarela.

Quando for o primeiro da fila, aparecerá uma mensagem no canto inferior dizendo as informações do hóspede (quantos dias pretende ficar, quanto de dinheiro tem e seu tipo). Teste hospedá-lo de forma que obtenha o melhor dinheiro daquele hóspede. 
Você pode mandar um hóspede ir embora esperando ele perder a paciência ou clicando no X da sua mensagem de reserva. Os hóspedes pagarão o valor da reserva quando seu reserva vencer. Ou seja, quando desocuparem os quartos. 

Ao lado dos ícones de qual atividade o atendente está fazendo, há uma caixa cinza que informa o dia atual do hotel, a quantidade de dinheiro e uma meta de reserva para aquele dia. Batendo a meta você recebe mais R$ 100,00.
Inicialmente você terá R$ 600,00 para investir em melhorias no hotel. A simulação tem duração de 5 dias.

A confecção dos avatares e alguns itens do cenário são originalmente do jogo Habbo Hotel.

Membros da equipe:
João Paulo Mota Santana: Elaboração dos personagens e do cenária e contribuições na documentação do projeto. (2,5/5,0)
Marco Antônio Barreto Dos Santos: Ajuste no código do projeto e confecção do vídeo de apresentação. (2,5/5,0)
Webert Samuel Bezerra Henrique: Contribuições na documentação, desenvolvimento do código do projeto, confecção dos avatares e cenários. (5/5)
