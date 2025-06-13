# Geração e Salvamento de Partições de Treino e Teste

Este repositório contém scripts utilizados para gerar e salvar partições de treino e teste, baseadas na [base de dados de discurso de ódio em português](https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset), onde a base hierarquica utilizada consta com 5.668 instâncias divididas em reduzida a 27 rótulos (foram mantidos somente os rótulos com 10 ou mais intências) disponibilizada por Paula Fortuna.


## Distribuição dos Dados

- **Dados Originais:**  
O gráfico a seguir exibe a distribuição dos dados conforme foram rotulados na base disponibilizada no trabalho [base de dados de discurso de ódio em português](https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset).

 ![graficoDit](https://github.com/user-attachments/assets/975a6891-6628-4dd8-bb52-81077e820972)

- **Dados Reduzidos:**  
O gráfico a seguir exibe a distribuição dos dados pós um processo de redução.

![GraficoDistReduzido](https://github.com/user-attachments/assets/3658ba95-f3ba-41bd-84a9-3407cae2fd9a)


 
## Detalhes das Partições

O script responsável por realizar este procedimento, localizado em [`Scripts/SalvaParticoesHierarquico.py`](https://github.com/Carlosbera7/SalvarParticoesMultiLabel/blob/main/Script/SalvaParticoesHierarquico.py), foi desenvolvido baseado no trabalho de Sechidis, K., Tsoumakas, G., & Vlahavas, I. (2011). Onde foi apresentada uma tecnica para fazer a estratificação multi_label.

- **Partição de Treino:**  
  Contém 3.967 instâncias, sendo:
  ![treino](https://github.com/user-attachments/assets/47d3a6a7-f75a-400e-8f93-43eaf9028e43)



- **Partição de Teste:**  
  Contém 1.701 instâncias, sendo:  
  ![teste](https://github.com/user-attachments/assets/5c46c5c0-8181-4148-b440-5a6c7c5152f4)


As partições geradas são salvas no diretório [`Data/`](https://github.com/Carlosbera7/SalvarParticoesMultiLabel/tree/main/Data). Este repositório contém as partições já geradas e utilizadas nos experimentos, disponíveis em [`Data/`](https://github.com/Carlosbera7/SalvarParticoesMultiLabel/tree/main/Data). O objetivo é garantir consistência nos dados utilizados em experimentos futuros. O código pode ser testado diretamente em um ambiente virutal [`Execução`](https://expert-space-winner-76gqpqw9prcxj4p.github.dev/)

## Observação
Os experimentos futuros utilizarão exclusivamente estas partições salvas para garantir a reprodutibilidade e comparabilidade dos resultados.  
