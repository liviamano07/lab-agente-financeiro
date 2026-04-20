# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do FinCoach AI (Assistente Financeiro Educacional) é feita com base em três abordagens complementares:

1. **🧪 Testes estruturados**
Perguntas pré-definidas com respostas esperadas, validando consistência, segurança e uso correto da base de conhecimento.

2. **👥 Testes com usuários reais**
Usuários simulados (amigos ou colegas) interagem com o agente e avaliam a qualidade da experiência.

3. **📊 Análise qualitativa**
Avaliação da clareza das respostas, utilidade educacional e aderência ao perfil do usuário.

---

## 📈 Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
|🎯 **Assertividade** | Se o agente responde corretamente com base nos dados disponíveis | Retornar corretamente soma de gastos do usuário |
|🛡️ **Segurança** | Se o agente evita inventar dados ou recomendações indevidas | Admitir quando não tem informação suficiente |
|🧠 **Coerência** | Se a resposta está alinhada ao objetivo educativo do agente | Explicar conceitos de forma simples para iniciantes |
|💬 **Experiência do Usuário (UX)** | Clareza, fluidez e naturalidade da conversa | Respostas compreensíveis e bem estruturadas |
|🔄 **Contextualização** | Uso correto do histórico e perfil do usuário | Adaptar resposta ao perfil financeiro (ex: conservador) |


> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## 🧪 Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### 💰 Teste 1: Simulação financeira
- **Pergunta:** "Se eu guardar R$ 150 por mês, quanto terei em 1 ano?"
- **Resposta esperada:** R$ 1.800 ao final de 12 meses, sem considerar rendimentos.`
- **Resultado:** [ ] Correto [ ] Parcial   [ ] Incorreto

### 📊 Teste 2: Análise de gastos
- **Pergunta:** "Estou gastando muito com alimentação?"
- **Resposta esperada:** Análise baseada no transacoes.csv, com porcentagem ou padrão de consumo.
- **Resultado:** [ ] Correto [ ] Parcial  [ ] Incorreto

### 🧠 Teste 3: Educação financeira
- **Pergunta:** "O que é renda fixa?"
- **Resposta esperada:** Explicação simples, didática e sem jargões técnicos.
- **Resultado:** [ ] Correto [ ] Parcial   [ ] Incorreto

### 🚫 Teste 4: Fora do escopo
- **Pergunta:** "Qual a previsão do tempo amanhã?"
- **Resposta esperada:** Agente informa que atua apenas com educação financeira.
- **Resultado:** [ ] Correto [ ] Incorreto

---

## 📌 Resultados

Após os testes, registre suas conclusões:

**✅ O que funcionou bem:**
- [Respostas claras e educativas
Boa adaptação ao perfil do usuário
Simulações financeiras simples funcionando corretamente
Recusa adequada de perguntas fora do escopo]

** ⚠️ O que pode melhorar:**
- [Melhor precisão nas simulações com juros compostos
Aumento da profundidade nas análises de gastos
Memória de contexto mais longa entre interações]

---

## 📊 Métricas Avançadas (nível profissional)

Para evolução futura do projeto:

⚡ Latência de resposta (tempo de geração da IA)
💰 Custo por interação (tokens)
📉 Taxa de respostas inválidas ou fora do escopo
🧾 Taxa de uso da base de conhecimento vs. geração livre
🔁 Retenção de contexto na conversa

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
