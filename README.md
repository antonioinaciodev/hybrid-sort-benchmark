# 📊 Empirical Algorithm Analysis & Hybrid Sort

## 📌 Sobre o Projeto
Este repositório contém uma suíte de *benchmarking* e análise empírica de algoritmos de ordenação, desenvolvido como laboratório prático para a disciplina de **Projeto e Análise de Algoritmos** (Ciência da Computação - UFPI).

O objetivo deste projeto vai além da implementação pura. Ele visa provar empiricamente o comportamento teórico assintótico das classes de complexidade $O(n^2)$ e $O(n \log n)$ no hardware real e, a partir desses dados, projetar um **Algoritmo Híbrido** otimizado, semelhante ao princípio do Timsort.

## 🔬 Arquitetura e Análise

O projeto foi refatorado em uma arquitetura modularizada e limpa:
1. **`insertion_sort.py` ($O(n^2)$):** Extremamente rápido para subvetores pequenos ou vetores quase ordenados.
2. **`merge_sort.py` ($O(n \log n)$):** Eficiente para grandes volumes de dados, mas sofre com *overhead* de chamadas recursivas em partições minúsculas.
3. **`hybrid_sort.py`:** Algoritmo que divide o problema recursivamente (estilo Merge), mas delega a ordenação local para o Insertion Sort quando o subvetor atinge um limiar de tamanho $K$.
4. **`benchmark.py`:** O motor principal da análise empírica que orquestra os testes e plota os resultados visualmente usando `matplotlib`.

### A Descoberta do Limiar ($K$ Ótimo)
Em subvetores muito pequenos, o custo das chamadas recursivas do Merge Sort o torna mais lento que o Insertion Sort. O script de benchmark foi programado para encontrar visual e matematicamente o ponto de cruzamento exato onde essa inversão de performance ocorre no hardware atual, utilizando esse valor como o $K$ dinâmico para o Algoritmo Híbrido.

## 🚀 Como Executar a Suíte de Testes

**Pré-requisitos:**
* Python 3.x
* Bibliotecas `numpy` e `matplotlib`
```bash
pip install numpy matplotlib
```

**Rodando a Análise:**
Todos os testes foram unificados em um único ponto de entrada para facilitar a usabilidade.

Navegue até a pasta `src/` e execute:
```bash
cd src
python benchmark.py
```

**Fluxo de Execução:**
1. O programa executará baterias de teste com vetores de 2 a 100 elementos e abrirá o **Gráfico 1**, mostrando o ponto de cruzamento ($K$ Ótimo) entre Merge e Insertion.
2. Ao fechar a janela do primeiro gráfico, o programa captura o $K$ encontrado e inicia um teste de estresse massivo (cenários Aleatório, Crescente e Decrescente).
3. Ao finalizar, exibirá os **Gráficos 2, 3 e 4**, provando empiricamente a superioridade do Algoritmo Híbrido sobre o Merge Sort puro.