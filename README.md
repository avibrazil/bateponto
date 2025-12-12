# Protótipo de Robô que bate ponto de trabalho

Este é um protótipo que funciona, mas está incompleto

Ele se loga no [TWO (Trading Works)](https://app.tradingworks.net/) e bate o
ponto.

Deveria rodar 4 vezes ao dia:
- De manhã ao chegar no trabalho
- Saída para o almoço
- Volta do almoço
- Final da jornada

Ele só precisa do Selenium e do Firefox em modo _headless_. O
[Containerfile](Containerfile) mostra as dependências exatas e o programa
[bateponto.py](bateponto.py) contém a lógica testada e funcional.

O programa roda o Firefox, sem UI, sem X11, sem janela. Entra no site, se loga
com usuário e senha, bate o ponto e fecha o browser e finaliza.

## O que falta
Este programa pode rodar em qualquer computador com Linux e Firefox. O Chrome
(Chromium) apresentou problemas.

Para manter isolamento do Firefox, sem interferências de cookies etc, o ideal
seria rodá-lo num container. Outra forma de isolá-lo é criar um usuário que só
faz isso e eventualmente apagar a pasta do Firefox no final de cada execução.
Esta opção é boa para quem já tem um servidor Linux rodando 24h/dia e quer
evitar containers.

O robô seria executado pelo cron (do host, no caso de container) 4 vezes ao
dia.

Outra abordagem mais sofisticada seria o robô se manter em execução e
decidir quando bater o ponto em certas horas pré-determinadas do dia, incluindo
alguma randomização. Nesta abordagem o robô teria um cron interno.

O robô poderia ainda incorporar o [módulo holidays](https://pypi.org/project/holidays/)
e inteligentemente saber os dias que não deve bater ponto, como feriados.

Outra melhoria ainda seria notificar o usuário pelo Telegram, avisando sobre
falhas, status semanal, próximos feriados etc. Da mesma forma como
[já faço no MercadoBitcoinBalance](https://github.com/avibrazil/MercadoBitcoinBalance/blob/cccf15d4907b8dab6584370a06470341345e8891/src/__main__.py#L17).

