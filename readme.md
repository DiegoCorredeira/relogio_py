# Relógio Digital com Exibição de Temperatura

Este é um simples aplicativo de relógio digital construído usando Tkinter em Python. O relógio exibe a hora atual e fornece recursos adicionais para mostrar a temperatura, data e dia da semana. A temperatura é obtida a partir de uma API com base na cidade informada pelo usuário.

## Dependências
- Python 3.x
- Tkinter
- requests

## Como Executar
1. Instale as dependências mencionadas acima.
2. Clone o repositório ou faça o download do arquivo `main.py`.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde está localizado o arquivo `main.py`.
4. Execute o seguinte comando:
```
python main.py
```
5. A janela do aplicativo de relógio digital será exibida, mostrando a hora atual.
6. Você pode clicar na opção "Temperatura" no menu para inserir o nome de uma cidade e obter a temperatura atual para essa cidade.
7. A opção "Data" no menu exibirá a data atual, e a opção "Dia da Semana" exibirá o dia da semana atual.

## Documentação
- `get_temperature(city)`: Obtém a temperatura atual de uma determinada cidade através de uma API.

    - Parâmetros:
        - `city` (str): O nome da cidade para obter a temperatura.
    
    - Retorna:
        - `float`: A temperatura atual da cidade em graus Celsius.

- `show_temperature()`: Exibe a temperatura da cidade inserida no campo `city_entry`.

    - Parâmetros:
        - Nenhum
    
    - Retorna:
        - Nenhum

- `update_clock()`: Atualiza a exibição do relógio digital a cada segundo.

    - Parâmetros:
        - Nenhum
    
    - Retorna:
        - Nenhum

- `show_day_of_week()`: Exibe o dia da semana atual no campo `info_label`.

    - Parâmetros:
        - Nenhum
    
    - Retorna:
        - Nenhum

- `show_date()`: Exibe a data atual no campo `info_label`.

    - Parâmetros:
        - Nenhum
    
    - Retorna:
        - Nenhum

## Contribuições
Contribuições para melhorar a funcionalidade ou adicionar novos recursos a este aplicativo de relógio digital são bem-vindas. Sinta-se à vontade para enviar problemas ou solicitações de alteração no repositório do GitHub.

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).