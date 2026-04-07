# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização na FIONA |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Armazena as conversas passadas para que a Fiona mantenha o contexto e aprenda com as interações do usuário. |
| `perfil_investidor.json` | JSON | Guarda as preferências de risco do usuário para personalizar as recomendações de segurança financeira. |
| `produtos_financeiros.json` | JSON | Contém as regras e detalhes do Tesouro Selic e CDB para sugerir onde rentabilizar a reserva. |
| `transacoes.csv` | CSV | Registra todas as entradas e saídas financeiras para calcular o saldo e o progresso da meta de emergência. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Em Produtos Financeiros, foquei exclusivamente no Tesouro Selic e CDB, por serem os ativos mais indicados para reserva de emergência e metas de curto prazo. Além disso, expandi o arquivo de Transações com novos registros fictícios para garantir testes de estresse mais precisos.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

A ingestão de dados na Fiona ocorre por dois canais: via prompt interativo, onde o usuário registra seus gastos em tempo real, ou por injeção direta via código, facilitando a vinculação de bases de dados externas e testes automatizados.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

No prompt, a Fiona transforma mensagens informais em dados estruturados, utilizando o contexto da conversa para atualizar o saldo em tempo real e sugerir aportes financeiros imediatos

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
