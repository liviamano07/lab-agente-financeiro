# Base de Conhecimento

## Dados Utilizados

A base de conhecimento do agente foi estruturada com dados simulados para representar um ambiente real de educação financeira e análise de comportamento do usuário.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Mantém histórico de interações para contexto da conversa |
| `perfil_investidor.json` | JSON | Define perfil financeiro do usuário (conservador, moderado, agressivo) |
| `produtos_financeiros.json` | JSON | Base educacional com explicações de produtos financeiros |
| `transacoes.csv` | CSV | Simula padrões de consumo e auxilia em análises de gastos |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Os dados foram estruturados de forma simulada e educacional, com foco em:
-Representar perfis financeiros fictícios de usuários
-Simular histórico de transações para análise de comportamento
-Criar uma base de produtos financeiros explicativos (não comerciais)
-Permitir simulações de cenários financeiros simples (gastos e organização financeira)]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[Os arquivos JSON e CSV são carregados no início da execução da aplicação e convertidos em estruturas de dados Python (dicionários e DataFrames), permitindo consultas rápidas durante a interação com o usuário.t]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[A base de conhecimento é utilizada de forma dinâmica e contextual, sendo incorporada ao fluxo da IA da seguinte forma:
-O perfil do usuário personaliza o tom e o tipo de explicação
-O histórico de transações é usado para análises simples de comportamento financeiro
-Os produtos financeiros servem como base educacional para explicações
-O histórico de atendimento mantém contexto da conversa para continuidade
Os dados são combinados com o prompt da IA generativa para gerar respostas mais contextualizadas e personalizadas.]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
👤 Dados do Usuário:
- Nome: Maria Luiza
- Perfil: Moderado
- Objetivo: Organização financeira mensal

💰 Resumo de Transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 05/11: Restaurante - R$ 120

📊 Análise do Agente:
O usuário apresenta padrão de gastos recorrentes com lazer e alimentação fora de casa, podendo otimizar seu orçamento mensal.
...
```
