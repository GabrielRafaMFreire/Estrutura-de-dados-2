#Gabriel Rafá Martins Freire mat: 20230145310

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value, position=None):
        new_node = Node(value)

        # Caso a posição não seja especificada, adiciona ao final
        if position is None:  
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = new_node

        # Caso a posição seja especificada, adiciona naquele local
        else:  
            # Inserir no início
            if position == 0:  
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                count = 0
                while current is not None and count < position - 1:
                    current = current.next
                    count += 1
                if current is None:
                    raise IndexError("Posição não encontrada")
                new_node.next = current.next
                current.next = new_node

    def remove(self, position):
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        count = 0
        while current is not None:
            if count == position:
                previous.next = current.next
                return
            previous = current
            current = current.next
            count += 1
        raise IndexError("Posição não encontrada")

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def get_element(self, position):
        current = self.head 
        count = 0
        while current is not None:
            if count == position:
                return current.value
            count += 1
            current = current.next
        raise IndexError("Posição não encontrada")
    
    def update_element(self, position, new_value):
        current = self.head
        count = 0
        while current is not None:
            if count == position:
                current.value = new_value
                return
            count += 1
            current = current.next
        raise IndexError("Posição não encontrada")

    def print_elements(self):
        if self.is_empty():
            print("Lista está vazia")
        else:
            elements = []
            current = self.head
            while current is not None:
                elements.append(current.value)
                current = current.next
            print(elements)

def run_tests():
    linked_list = LinkedList()

    # Adiciona elementos ao final da lista
    linked_list.add(35)
    linked_list.add(10)
    linked_list.add(20)
    linked_list.add(30)
    print("Conteúdo da lista:")
    # Os elementos são exibidos em forma de lista. Isso facilita a visualização e identificação das posições.
    linked_list.print_elements()

    # Obtém o tamanho da lista
    print("Tamanho da lista: ", linked_list.size())

    # Verifica se a lista está vazia
    print("A lista está vazia?", linked_list.is_empty())

    # Obtém um elemento de uma posição específica
    print("Elemento na posição 2: ", linked_list.get_element(2))
    print("Elemento na posição 3: ", linked_list.get_element(3))

    # Atualiza um elemento em uma posição específica
    print("Atualizando o elemento na posição 2 para 314")
    linked_list.update_element(2, 314)
    linked_list.print_elements()

    # Remove o elemento em uma posição específica
    print("Removendo o elemento na posição 3")
    linked_list.remove(3)
    linked_list.print_elements()

    # Adiciona um elemento em uma posição específica
    print("Adicionando 50 na posição 2")
    linked_list.add(50, 2)
    linked_list.print_elements()

if __name__ == "__main__":
    run_tests()
