# Filtro Python para remover linhas repetidas
Este script Python remove linhas duplicadas de um texto, agora com opções para considerar os espaços ou comentar linhas vazias.

## Funcionalidades
- Remove linhas duplicadas, mantendo a primeira ocorrência.
- Opção para considerar espaços na comparação de linhas (`-s`).
- Opção para comentar as linhas vazias com # (`-p`).
- Salva a saída em um novo arquivo (`<input_file>_filtered.txt` ou `filtered.txt` se usar o modo stdin).

## Como Usar
```sh
python rm_rlines.py -<opção> example.txt
