# Variável para o interpretador Python
PYTHON=python3

# Regra padrão executada quando se digita apenas 'make'
all: run

# Executa o orquestrador principal interativo
run:
	@echo "Iniciando o orquestrador principal..."
	$(PYTHON) main.py

# Executa apenas os algoritmos básicos (O(n^2))
run-basic:
	@echo "Executando testes para Insertion e Selection Sort..."
	$(PYTHON) insertionSelectionSort.py

# Executa apenas os algoritmos avançados (O(n log n))
run-advanced:
	@echo "Executando testes para Merge e Quick Sort..."
	$(PYTHON) mergeSortQuickSort.py

# Exibe os comandos disponíveis
help:
	@echo "Comandos disponíveis:"
	@echo "  make run          - Inicia o menu interativo (main.py)"
	@echo "  make run-basic    - Executa apenas Insertion e Selection Sort diretamente"
	@echo "  make run-advanced - Executa apenas Merge e Quick Sort diretamente"
