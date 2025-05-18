# Geração e Salvamento de Partições de Treino e Teste

Este repositório contém scripts utilizados para gerar e salvar partições de treino e teste, baseadas na [base de dados de discurso de ódio em português](https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset), reduzida a 27 rótulos (foram mantidos somente os rótulos com 10 ou mais intências) disponibilizada por Paula Fortuna.

O script responsável por realizar este procedimento, localizado em [`Scripts/SalvaParticoesHierarquico.py`](https://github.com/Carlosbera7/SalvarParticoesMultiLabel/blob/main/Script/SalvaParticoesHierarquico.py), foi desenvolvido baseado no trabalho de Sechidis, K., Tsoumakas, G., & Vlahavas, I. (2011). Onde foi apresentada uma tecnica para fazer a estratificação multi_label.

As partições geradas são salvas no diretório [`Data/`](https://github.com/Carlosbera7/SalvarParticoesMultiLabel/tree/main/Data). Este repositório contém as partições já geradas e utilizadas nos experimentos, disponíveis em [`Data/`](https://github.com/Carlosbera7/SalvarParticoesMultiLabel/tree/main/Data). O objetivo é garantir consistência nos dados utilizados em experimentos futuros. O código pode ser testado diretamente em um ambiente virutal [`Execução`](https://expert-space-winner-76gqpqw9prcxj4p.github.dev/)

## Detalhes das Partições

- **Partição de Treino:**  
  Contém 3.967 instâncias, sendo:
  '
  [Uploading<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Distribuição de Classes</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div style="width: 80%; margin: auto;">
        <canvas id="classDistributionChart"></canvas>
    </div>
    <script>
        // Dados do gráfico
        const data = {
            labels: [
                "Hate speech", "Sexism", "Body", "Racism", "Ideology", "Homophobia", "Origin", "Religion",
                "Other lifestyle", "Fat people", "Left-wing ideology", "Ugly people", "Black people", "Fat women",
                "Feminists", "Gays", "Immigrants", "Islamists", "Lesbians", "Men", "Muslims", "Refugees",
                "Trans women", "Women", "Transsexuals", "Ugly women", "Migrants", "Homosexuals"
            ],
            datasets: [
                {
                    label: "Instâncias Positivas",
                    data: [
                        800, 450, 120, 90, 50, 200, 100, 20, 30, 150, 60, 80, 90, 70,
                        60, 50, 40, 30, 100, 50, 40, 20, 150, 300, 100, 80, 90, 120
                    ],
                    backgroundColor: "rgba(75, 192, 192, 0.5)",
                    borderColor: "rgba(75, 192, 192, 1)",
                    borderWidth: 1
                },
                {
                    label: "Instâncias Negativas",
                    data: [
                        4868 - 800, 4868 - 450, 4868 - 120, 4868 - 90, 4868 - 50, 4868 - 200, 4868 - 100, 4868 - 20,
                        4868 - 30, 4868 - 150, 4868 - 60, 4868 - 80, 4868 - 90, 4868 - 70,
                        4868 - 60, 4868 - 50, 4868 - 40, 4868 - 30, 4868 - 100, 4868 - 50, 4868 - 40, 4868 - 20,
                        4868 - 150, 4868 - 300, 4868 - 100, 4868 - 80, 4868 - 90, 4868 - 120
                    ],
                    backgroundColor: "rgba(153, 102, 255, 0.5)",
                    borderColor: "rgba(153, 102, 255, 1)",
                    borderWidth: 1
                }
            ]
        };

        // Configuração do gráfico
        const config = {
            type: "bar",
            data: data,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: "top",
                    },
                    title: {
                        display: true,
                        text: "Distribuição de Classes (Positivas e Negativas)"
                    }
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: "Classes"
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: "Número de Instâncias"
                        }
                    }
                }
            }
        };

        // Renderiza o gráfico
        const ctx = document.getElementById("classDistributionChart").getContext("2d");
        new Chart(ctx, config);
    </script>
</body>
</html>
'
 GraficoDistrTreino.html…]()

  ![DistribuicaoClasses-Treino](https://github.com/user-attachments/assets/9aee28d9-eff9-4d39-921f-e76081cb2afe)


- **Partição de Teste:**  
  Contém 1.701 instâncias, sendo:  
  ![DistribuicaoClasses-Teste](https://github.com/user-attachments/assets/10c9b5d9-48ff-4923-b3b9-e1b45a4cd62f)


## Observação
Os experimentos futuros utilizarão exclusivamente estas partições salvas para garantir a reprodutibilidade e comparabilidade dos resultados.  
