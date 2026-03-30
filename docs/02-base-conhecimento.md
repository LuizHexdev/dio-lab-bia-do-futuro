# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilidade da Dina |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e dar segmento a atendimentos anteriores de forma mais eficiente|
| `perfil_investidor.json` | JSON | Personalizar recomendações e explicações com base no perfil e base nas dúvidas do cliente |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que eles sejam explicados para o cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar de forma didática para explicação |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

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
