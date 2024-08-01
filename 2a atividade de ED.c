#include <stdio.h>
#include <stdbool.h>

#define TAM_MAX 10

// Definindo os limites do vetor
int tamAtual = 5;
int dados[TAM_MAX] = {2, 3, 1, 5, 4, 0, 0, 0, 0, 0};

bool vazia() {
    return tamAtual == 0;
}

bool cheia() {
    return tamAtual == TAM_MAX;
}

int tamanhoLista() {
    return tamAtual;
}

const char* retornaElementoNaPosicao(int posicaoLista) {
    static char msg[50];
    if (posicaoLista > tamAtual || posicaoLista <= 0) {
        return "Não é possível buscar este valor. Está fora dos limites.";
    } else {
        sprintf(msg, "%d", dados[posicaoLista - 1]);
        return msg;
    }
}

const char* modificaElementoNaPosicao(int posicaoLista, int numero) {
    static char msg[50];
    if (posicaoLista > tamAtual || posicaoLista <= 0) {
        return "Não é possível alterar este elemento pois está fora dos limites.";
    } else {
        int numeroAnterior = dados[posicaoLista - 1];
        dados[posicaoLista - 1] = numero;
        sprintf(msg, "Elemento alterado de %d para %d", numeroAnterior, numero);
        return msg;
    }
}

const char* insereElementoNaPosicao(int posicaoLista, int numero) {
    if (cheia() || posicaoLista > tamAtual + 1 || posicaoLista <= 0) {
        return "Não é possível adicionar um elemento na posição indicada.";
    }

    for (int i = tamAtual; i >= posicaoLista; i--) {
        dados[i] = dados[i - 1];
    }

    dados[posicaoLista - 1] = numero;
    tamAtual++;
    return "Elemento inserido com sucesso";
}

const char* removeElementoNaPosicao(int posicaoLista) {
    if (vazia() || posicaoLista > tamAtual || posicaoLista < 1) {
        return "Não é possível remover um elemento na posição indicada.";
    }

    for (int i = posicaoLista - 1; i < tamAtual - 1; i++) {
        dados[i] = dados[i + 1];
    }

    dados[tamAtual - 1] = 0;
    tamAtual--;
    return "Elemento removido com sucesso";
}

void printArray() {
    for (int i = 0; i < tamAtual; i++) {
        printf("%d ", dados[i]);
    }
    printf("\n");
}

int main() {
    printArray();
    printf("%d\n", vazia());
    printf("%d\n", cheia());
    printf("%d\n", tamanhoLista());
    printf("%s\n", retornaElementoNaPosicao(4));
    printf("%s\n", modificaElementoNaPosicao(3, 5));
    printf("%s\n", insereElementoNaPosicao(3, 1));
    printf("%s\n", removeElementoNaPosicao(6));
    printArray();
    return 0;
}
