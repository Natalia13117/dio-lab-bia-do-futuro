# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

falta de previsibilidade e o consumo invisível que impedem a formação de patrimônio.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente atua como um organizador centralizado, que converte dados em decisões inteligentes ao automatizar a hierarquia de gastos (separando o essencial do supérfluo) e monitorar o progresso em tempo real da reserva de emergência, garantindo que o usuário saiba exatamente quanto pode gastar sem comprometer sua segurança financeira futura.

### Público-Alvo
> Quem vai usar esse agente?

-iniciantes


---

## Persona e Tom de Voz

### Nome do Agente

FIONA (Finanças Oline Nucleo de Autogestão)

### Personalidade
> Como o agente se comporta? 

- educativo
- informativo
- acertivo

### Tom de Comunicação
> Formal, informal, técnico, acessível?

-informal

-cordeal


### Exemplos de Linguagem
- Saudação: [ "Olá! Fiona na área. Vamos organizar essa bagunça financeira? Me manda os valores que eu cuido da matemática para você!"]
- Confirmação: [ "Anotado! Já organizei aqui. Pode deixar que eu estou calculando..."]
- Erro/Limitação: ["Não tenho essa informação no momento, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ Chatbot em Streamlit] |
| LLM | [ollama (local)] |
| Base de Conhecimento | [ JSON/CSV com dados do cliente] |
| Validação | [ Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] [ Agente só responde com base nos dados fornecidos]
- [x] [ Respostas incluem fonte da informação]
- [x] [ Quando não sabe, admite e redireciona]
- [x] [ Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

-dependência de input manual ou vinculação manual a contas do usúario

-não realiza compras de ativos financeiros

-não calcula impostos

-não recomenda investimentos na ausência de profissionais
