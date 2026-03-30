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

O produto de Fundo Muntimercado foi substituído pelo produto de Fundo Imobiliário.
---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

```python
import panda as pd
import json

# CSVs:
  historico = pd.read_csv('data/historico_atendimento.csv')
  transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
  with open ( 'data/perfil_investidor.json', 'r',encoding = 'utf8') as f:
    perfil = json.load(f)
  with open ( 'data/produtos_financeiros.json', 'r',encoding = 'utf8') as f:
    perfil = json.load(f)
```
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
