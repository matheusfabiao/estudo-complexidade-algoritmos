import sys
import time
from pathlib import Path

# Aumentando o limite de recursão para evitar erros em instâncias grandes de QuickSort
sys.setrecursionlimit(200000)

# mergeSort


def merge(A, p, q, r):
    """Intercala dois subarranjos ordenados em um único subarranjo ordenado.

    Args:
        A (list): A lista principal contendo os subarranjos.
        p (int): O índice inicial do primeiro subarranjo.
        q (int): O índice final do primeiro subarranjo (e divisor).
        r (int): O índice final do segundo subarranjo.
    """
    L = A[p : q + 1]
    R = A[q + 1 : r + 1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort_recursive(A, p, r):
    """Divide a lista recursivamente e a ordena utilizando a função merge.

    Args:
        A (list): A lista de números a ser ordenada.
        p (int): O índice inicial do subarranjo.
        r (int): O índice final do subarranjo.
    """
    if p < r:
        q = (p + r) // 2
        merge_sort_recursive(A, p, q)
        merge_sort_recursive(A, q + 1, r)
        merge(A, p, q, r)


def merge_sort(A, n):
    """Inicia a execução do algoritmo Merge Sort e mede seu tempo de execução.

    Args:
        A (list): A lista de números a ser ordenada.
        n (int): O tamanho da lista.

    Returns:
        float: O tempo total de execução do algoritmo em segundos.
    """
    inicio = time.perf_counter()
    merge_sort_recursive(A, 0, n - 1)
    return time.perf_counter() - inicio


# quickSort


def partition(A, inicio, fim):
    """Realiza o particionamento da lista para o Quick Sort (esquema de Lomuto).

    Args:
        A (list): A lista de números a ser particionada.
        inicio (int): O índice inicial do subarranjo.
        fim (int): O índice final do subarranjo, onde está localizado o pivô.

    Returns:
        int: A posição final (índice) em que o pivô foi inserido.
    """
    pivo = A[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if A[j] <= pivo:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[fim] = A[fim], A[i + 1]
    return i + 1


def quick_sort_recursive(A, inicio, fim):
    """Divide a lista recursivamente em torno do pivô para ordená-la.

    Args:
        A (list): A lista de números a ser ordenada.
        inicio (int): O índice inicial do subarranjo a ser processado.
        fim (int): O índice final do subarranjo a ser processado.
    """
    if inicio < fim:
        q = partition(A, inicio, fim)
        quick_sort_recursive(A, inicio, q - 1)
        quick_sort_recursive(A, q + 1, fim)


def quick_sort(A, n):
    """Inicia a execução do algoritmo Quick Sort e mede seu tempo de execução.

    Args:
        A (list): A lista de números a ser ordenada.
        n (int): O tamanho da lista.

    Returns:
        float: O tempo total de execução do algoritmo em segundos.
    """
    inicio = time.perf_counter()
    quick_sort_recursive(A, 0, n - 1)
    return time.perf_counter() - inicio


def executar_merge_quick(verbose=True):
    """Carrega as instâncias de teste e mede o desempenho do Merge e Quick Sort.

    Args:
        verbose (bool, optional): Se True, exibe o progresso e a tabela final no console. Padrão é True.

    Returns:
        list: Resultados no formato [nome_arquivo, tempo_merge, tempo_quick].
    """
    tamanhos = ['1000', '10000', '100000']
    resultados = []

    if verbose:
        print('Processando arquivos... Aguarde.')

    for tam in tamanhos:
        for num in range(1, 5):
            path = f'./instancias-numericas/instancias-num/num.{tam}.{num}.in'
            file_path = Path(path)

            if not file_path.exists():
                continue

            try:
                with open(path, 'r') as f:
                    lista_original = [int(line.strip()) for line in f]

                n = len(lista_original)

                # Executando e medindo cada algoritmo com uma cópia limpa da lista
                t_merge = merge_sort(lista_original.copy(), n)
                t_quick = quick_sort(lista_original.copy(), n)

                if verbose:
                    print(
                        f'Concluído: {file_path.name} (n={n}) | Merge: {t_merge:.6f}s | Quick: {t_quick:.6f}s'
                    )

                resultados.append(
                    [file_path.name, f'{t_merge:.6f}s', f'{t_quick:.6f}s']
                )

            except Exception as e:
                if verbose:
                    print(f'Erro ao processar {file_path.name}: {e}')

    # --- RESULTADOS ---
    if verbose:
        header = ['Arquivo (Instância)', 'MergeSort', 'QuickSort']
        print(f'\n{header[0]:<25} | {header[1]:<12} | {header[2]:<12}')
        print('-' * 85)

        for res in resultados:
            print(f'{res[0]:<25} | {res[1]:<12} | {res[2]:<12}')

    return resultados


if __name__ == '__main__':
    executar_merge_quick(verbose=True)
