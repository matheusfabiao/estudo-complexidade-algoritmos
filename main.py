import sys

from insertionSelectionSort import executar_insertion_selection
from mergeSortQuickSort import executar_merge_quick


def menu():
    """Exibe o menu de interação no terminal e orquestra a execução dos testes."""
    while True:
        print('\n' + '=' * 50)
        print('    MENU DE EXECUÇÃO - ALGORITMOS DE ORDENAÇÃO')
        print('=' * 50)
        print('1. Executar Insertion e Selection Sort (O(n²))')
        print('2. Executar Merge e Quick Sort (O(n log n))')
        print('3. Executar Todos e Mostrar Tabela Comparativa')
        print('4. Sair')
        print('=' * 50)

        opcao = input('Escolha uma opção (1-4): ')

        if opcao == '1':
            print('\nExecutando Insertion e Selection Sort...')
            executar_insertion_selection(verbose=True)

        elif opcao == '2':
            print('\nExecutando Merge e Quick Sort...')
            executar_merge_quick(verbose=True)

        elif opcao == '3':
            print(
                '\nExecutando TODOS os algoritmos... Isso pode demorar alguns minutos para instâncias grandes.'
            )
            print('Processando Insertion e Selection Sort (Aguarde)...')
            res_is = executar_insertion_selection(verbose=False)

            print('Processando Merge e Quick Sort (Aguarde)...')
            res_mq = executar_merge_quick(verbose=False)

            # Combinação dos resultados
            # res_is: [file_name, tempo_selection, tempo_insertion]
            # res_mq: [file_name, tempo_merge, tempo_quick]

            tabela_combinada = {}
            for res in res_is:
                file_name = res[0]
                tabela_combinada[file_name] = {
                    'selection': res[1],
                    'insertion': res[2],
                    'merge': 'N/A',
                    'quick': 'N/A',
                }

            for res in res_mq:
                file_name = res[0]
                if file_name in tabela_combinada:
                    tabela_combinada[file_name]['merge'] = res[1]
                    tabela_combinada[file_name]['quick'] = res[2]
                else:
                    tabela_combinada[file_name] = {
                        'selection': 'N/A',
                        'insertion': 'N/A',
                        'merge': res[1],
                        'quick': res[2],
                    }

            # Ordenando as chaves para a exibição ficar correta
            def extract_size(filename):
                parts = filename.split('.')
                if (
                    len(parts) >= 3
                    and parts[1].isdigit()
                    and parts[2].isdigit()
                ):
                    return (int(parts[1]), int(parts[2]))
                return (0, 0)

            chaves_ordenadas = sorted(
                tabela_combinada.keys(), key=extract_size
            )

            # Print da tabela combinada
            header = [
                'Arquivo (Instância)',
                'Selection Sort',
                'Insertion Sort',
                'Merge Sort',
                'Quick Sort',
            ]
            print(
                f'\n{header[0]:<25} | {header[1]:<15} | {header[2]:<15} | {header[3]:<12} | {header[4]:<12}'
            )
            print('-' * 90)

            for file_name in chaves_ordenadas:
                dados = tabela_combinada[file_name]
                print(
                    f"{file_name:<25} | {dados['selection']:<15} | {dados['insertion']:<15} | {dados['merge']:<12} | {dados['quick']:<12}"
                )

        elif opcao == '4':
            print('Encerrando o programa...')
            sys.exit(0)

        else:
            print(
                '\nOpção inválida! Por favor, escolha um número entre 1 e 4.'
            )


if __name__ == '__main__':
    menu()
