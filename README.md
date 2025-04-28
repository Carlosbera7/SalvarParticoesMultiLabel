# Geração e Salvamento de Partições de Treino e Teste

Este repositório contém scripts utilizados para gerar e salvar partições de treino e teste, baseadas na [base de dados de discurso de ódio em português](https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset), reduzida a 27 rótulos (foram mantidos somente os rótulos com 10 ou mais intências) disponibilizada por Paula Fortuna.

O script responsável por realizar este procedimento, localizado em [`Scripts/SalvaParticoes.py`](https://github.com/Carlosbera7/SalvarParticoes/blob/main/Scripts/SalvaParticoes.py), foi desenvolvido baseado no trabalho de Sechidis, K., Tsoumakas, G., & Vlahavas, I. (2011). Onde foi apresentada uma tecnica para fazer a estratificação multi_label.

As partições geradas são salvas no diretório [`Data/`](https://github.com/Carlosbera7/SalvarParticoes/tree/main/Data). Este repositório contém as partições já geradas e utilizadas nos experimentos, disponíveis em [`Data/Particoes Utilizadas`](https://github.com/Carlosbera7/SalvarParticoes/tree/main/Data/Particoes%20Utilizadas). O objetivo é garantir consistência nos dados utilizados em experimentos futuros. O código pode ser testado diretamente em um ambiente virutal [`Execução`](https://obscure-xylophone-wrr9q4j5v525g6.github.dev/)

## Detalhes das Partições

- **Partição de Treino:**  
  Contém 3.967 instâncias, sendo:
  ![DistribuicaoClasses-Treino](https://github.com/user-attachments/assets/9aee28d9-eff9-4d39-921f-e76081cb2afe)


- **Partição de Teste:**  
  Contém 1.701 instâncias, sendo:  
  ![DistribuicaoClasses-Teste](https://github.com/user-attachments/assets/10c9b5d9-48ff-4923-b3b9-e1b45a4cd62f)


## Observação
Os experimentos futuros utilizarão exclusivamente estas partições salvas para garantir a reprodutibilidade e comparabilidade dos resultados.  
