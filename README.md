# Tratamento de Erro em Python

Este repositório contém uma série de exemplos e boas práticas para lidar com tratamento de erros em Python. O objetivo é proporcionar uma base sólida para quem deseja entender como identificar, capturar e gerenciar erros de maneira eficaz no desenvolvimento de aplicações Python.

## Descrição do Projeto

Erros e exceções são uma parte inevitável da programação. Este projeto explora diversas abordagens para lidar com exceções em Python, mostrando desde o básico sobre blocos ```try/except ```até técnicas mais avançadas de logging, customização de exceções e manipulação de erros específicos.

# `try`/`except` em Python

O **`try`/`except`** em Python é usado para lidar com exceções, permitindo que erros sejam tratados de forma controlada, sem interromper o programa inesperadamente.

---

## **Sintaxe Básica**

A estrutura do `try`/`except` é a seguinte:

```python
try:
    # Código que pode gerar uma exceção
    x = int(input("Digite um número: "))
except ValueError:
    # Código executado se uma exceção ocorrer
    print("Por favor, insira um número válido.")
