# 📊 Estudo de Algoritmos de Ordenação

Bem-vindo ao **Estudo de Algoritmos de Ordenação**, um projeto focado na implementação, análise e benchmarking empírico de algoritmos clássicos de ordenação.

Este projeto compara a performance de algoritmos com complexidade quadrática ($O(n^2)$) contra algoritmos de divisão e conquista com complexidade log-linear ($O(n \log n)$), utilizando instâncias de dados estruturados em diferentes tamanhos.

---

## 🚀 Algoritmos Implementados

Os algoritmos estão divididos em dois grupos principais com base em suas características de complexidade de tempo:

### Algoritmos Básicos $\mathcal{O}(n^2)$
- **Insertion Sort**: Constrói o array final um elemento de cada vez. Costuma ser bastante eficiente para listas pequenas ou matrizes que já estão parcialmente ordenadas.
- **Selection Sort**: Algoritmo de seleção repetitiva que encontra o menor elemento da parte não ordenada e o move para o início, garantindo sempre a mesma quantidade de comparações independente do cenário.

### Algoritmos Avançados $\mathcal{O}(n \log n)$
- **Merge Sort**: Algoritmo focado em divisão e conquista que garante um tempo previsível dividindo a lista em metades, ordenando cada uma e as intercalando.
- **Quick Sort**: Utilizando o esquema de particionamento de Lomuto, é um dos algoritmos in-place mais eficientes na prática.

---

## 📂 Estrutura do Projeto

- `main.py`: O **ponto de entrada recomendado**. Fornece um menu interativo no terminal para rodar os testes parciais ou gerar uma poderosa tabela comparativa cruzando o tempo de todos os algoritmos simultaneamente.
- `insertionSelectionSort.py`: Módulo contendo as lógicas do Insertion e Selection Sort.
- `mergeSortQuickSort.py`: Módulo contendo as lógicas do Merge e Quick Sort (com proteções extras contra estouro do limite de recursão do Python).
- `instancias-numericas/instancias-num/`: Diretório contendo os dados de input. As instâncias variam exponencialmente em tamanho (1.000, 10.000 e 100.000 inteiros) e em grau de aleatoriedade/ordenação (representados pelas variantes de `.1.in` até `.4.in`).

---

## 🛠️ Requisitos e Instalação

- **Ambiente**: Python 3.11.7 (ou superior).
- **Dependências**: O projeto depende exclusivamente das bibliotecas nativas do core do Python (`time`, `sys`, `pathlib`). Não é necessário instalar pacotes externos via `pip`.

Para iniciar, faça o clone do repositório ou navegue até sua pasta no terminal:
```bash
cd estudo-complexidade-algoritmos
```

---

## 💻 Guia de Execução

### Método Recomendado: Menu Interativo
Para a melhor experiência, inicie o orquestrador interativo do projeto:

```bash
python3 main.py
```

> **OBS:** Caso esteja executando o código em um ambiente Linux ou MacOS, pode ser necessário ajustar o caminho do executável `python` para `python3`.

Você verá um menu com as seguintes opções:
1. **Executar Insertion e Selection Sort**: Útil para benchmark isolado em algoritmos de ordenação base.
2. **Executar Merge e Quick Sort**: Valida a performance avançada de log-linear.
3. **Executar Todos e Mostrar Tabela Comparativa**: O sistema fará a execução massiva em background e gerará uma super tabela cruzando todos os dados por instância para que você compare visualmente o abismo de tempo entre um $O(n^2)$ e um $O(n \log n)$ em 100.000 números.
4. **Sair**.

> ⚠️ **Atenção (Performance)**: A execução combinada (Opção 3) é extremamente pesada computacionalmente em razão da avaliação dos algoritmos $\mathcal{O}(n^2)$ rodando contra as bases de 100 mil números. Esse processo costuma demorar vários minutos.

### Execução Direta de Módulos (Standalone)
Se por motivos de debug você quiser executar um módulo de forma seca ignorando a interface de menu principal, os arquivos originais ainda estão acessíveis e totalmente operacionais diretamente:

```bash
# Executar a bateria de Insertion e Selection Sort
python insertionSelectionSort.py

# Executar a bateria de Merge e Quick Sort
python mergeSortQuickSort.py
```

> **OBS:** Caso esteja executando o código em um ambiente Linux ou MacOS, pode ser necessário ajustar o caminho do executável `python` para `python3`.  

---

*Desenvolvido por Matheus Fabião - Mestrando em Informática UFPB (PPGI).*

*Projeto desenvolvido para fins acadêmicos e análise de complexidade estrutural em Ciência da Computação.*
