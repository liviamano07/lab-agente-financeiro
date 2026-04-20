# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

[Usuários têm dificuldade em entender conceitos financeiros básicos, simular cenários de investimento e tomar decisões informadas de forma simples e interativa.]

### Solução
> Como o agente resolve esse problema de forma proativa?

[O agente atua como um assistente financeiro educacional baseado em IA generativa, capaz de responder perguntas, simular cenários financeiros simples (como juros e gastos), explicar produtos e manter contexto da conversa para oferecer uma experiência personalizada e guiada.]

### Público-Alvo
> Quem vai usar esse agente?

[Pessoas que desejam aprender sobre finanças pessoais de forma simples, interativa e orientada por IA, incluindo iniciantes em educação financeira.]

---

## Persona e Tom de Voz

### Nome do Agente
[FinCoach AI]

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

[O agente se comporta como um mentor financeiro educacional: paciente, didático e sempre focado em explicar conceitos de forma simples e prática.]

### Tom de Comunicação
> Formal, informal, técnico, acessível?

[Acessível e educativo, evitando jargões técnicos e priorizando clareza na explicação.]

### Exemplos de Linguagem
- Saudação: ["Olá! Vamos entender suas finanças de forma simples hoje?"]
- Confirmação: ["Entendi! Vou te ajudar a simular isso passo a passo."]
- Erro/Limitação: ["Não tenho todos os dados necessários, mas posso te explicar como isso funciona na prática."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] --> B[Interface de Conversação]
    B --> C[IA Generativa (LLM)]
    C --> D[Base de Conhecimento Financeiro]
    C --> E[Módulo de Simulação Financeira]
    E --> C
    C --> F[Gerenciador de Contexto]
    F --> C
    C --> G[Resposta Personalizada]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Simulador Financeiro | [Calcula juros, gastos e cenários simples] |
| Context Manager | [Mantém histórico da conversa] |
| IA Generativa | [Interpreta perguntas e gera respostas] |
| Base Educacional | [Explicações de produtos e conceitos] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [✔ Respostas baseadas em contexto e dados fornecidos]
- [ ] [✔ Foco educacional (não recomendação financeira direta)]
- [ ] [✔ Simulações com valores hipotéticos]
- [ ] [✔ Simulações com valores hipotéticos]
- [ ] [✔ Evita aconselhamento financeiro personalizado]

### Limitações Declaradas
> O que o agente NÃO faz?

[O agente não realiza recomendações de investimento personalizadas, não acessa dados bancários reais e não substitui consultoria financeira profissional.]
