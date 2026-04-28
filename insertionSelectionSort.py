import time
from pathlib import Path


def insertionSort(A, n):
    """Ordena uma lista usando o algoritmo Insertion Sort.

    Args:
        A (list): A lista de números a ser ordenada.
        n (int): O tamanho da lista.

    Returns:
        float: O tempo de execução do algoritmo em segundos.
    """
    inicio = time.perf_counter()
    for i in range(1, n):
        aux = A[i]
        j = i - 1
        while j >= 0 and A[j] > aux:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = aux
    return time.perf_counter() - inicio


def selectionSort(A, n):
    """Ordena uma lista usando o algoritmo Selection Sort.

    Args:
        A (list): A lista de números a ser ordenada.
        n (int): O tamanho da lista.

    Returns:
        float: O tempo de execução do algoritmo em segundos.
    """
    inicio = time.perf_counter()
    for i in range(0, n - 1):
        i_min = i
        for j in range(i + 1, n):
            if A[j] < A[i_min]:
                i_min = j
        if i_min != i:
            A[i], A[i_min] = A[i_min], A[i]
    return time.perf_counter() - inicio


def executar_insertion_selection(verbose=True):
    """Carrega as instâncias de teste e mede o desempenho do Insertion e Selection Sort.

    Args:
        verbose (bool, optional): Se True, exibe o progresso e a tabela final. Padrão é True.

    Returns:
        list: Resultados no formato [nome_arquivo, tempo_selection, tempo_insertion].
    """
    tamanhos = ['1000', '10000', '100000']
    resultados = []

    if verbose:
        print('Processando arquivos... Aguarde.')

    for tam in tamanhos:
        for num in range(1, 5):
            path = f'./instancias-numericas/instancias-num/num.{tam}.{num}.in'
            file_name = Path(path).name

            try:
                with open(path, 'r') as f:
                    lista_original = [int(line.strip()) for line in f]

                n = len(lista_original)

                tempo_selection = selectionSort(lista_original.copy(), n)
                tempo_insertion = insertionSort(lista_original.copy(), n)

                if verbose:
                    print(
                        f'Concluído: {file_name} (n={n}) | Selection: {tempo_selection:.6f}s | Insertion: {tempo_insertion:.6f}s'
                    )

                resultados.append(
                    [
                        file_name,
                        f'{tempo_selection:.6f}s',
                        f'{tempo_insertion:.6f}s',
                    ]
                )

            except FileNotFoundError:
                continue

    if verbose:
        header = ['Arquivo (Instância)', 'Selection Sort', 'Insertion Sort']
        print(f'\n{header[0]:<25} | {header[1]:<15} | {header[2]:<15}')
        print('-' * 60)

        for res in resultados:
            print(f'{res[0]:<25} | {res[1]:<15} | {res[2]:<15}')

    return resultados


if __name__ == '__main__':
    executar_insertion_selection(verbose=True)
