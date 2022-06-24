#linked list 
#the elements are stored using pointers 
#A linked list is represented by a pointer to the first node of the linked list
#
#The first node is called the head. If the linked list is empty, then #the value of the head points to NULL.

#1) data (we can store integer, strings or any type of data).
#2) Pointer (Or Reference) to the next node (connects one node to another)

#el nodo tiene su data y su siguiente 
#cabe señalar que la clase nodo solo crea un nodo, asi de sencillo como clase banana crea una banana clase nodo crea un nodo 



def traverse_linked_list():
 #code here
       t=node
       if t==None:
           return 0
       print(t.data,end=" " )
       while t.next!=None:
           t=t.next
           print(t.data,end=" ")

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    #Metodo para imprimir la lista 
    def printLL(self):
        if self.head == None:
            return AssertionError("The LL is empty :(")
        nodes = self.head
        while nodes is not None:
            print(nodes.data)
            nodes = nodes.next 
    #metodo para añadir al inicio
    def add_front(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head #hacemos el vinculo 
        self.head = new_node
    #metodo para añadir al final 
    def add_final(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 
    #añadir con un nodo de referencia en el medio 
    def middle(self,prev_node,new_data):
        if prev_node is None: #existencia del nodo anterior
            print("The node must be in the LL")
        new_node = Node(new_data)
        new_node.next = prev_node.next #asignamos el next del nuevo nodo al que tenia el anterior
    #eliminar el nodo
    def deletenode(self,key):
        temp = self.head #se guarda el valor base 
        if temp is not None:
            if temp.data == key: #checamos que el valor a borrar no sea el primero de la lista
            temp = None
            return 
        if temp is not None: #checa que las lista exista 
            if temp.data == key
                break
            prev = temp   #se almacena el nodo anterios
            temp = temp.next 
        if temp = None:
            return ValueError('key is not a node')

        prev.next = temp.next # se liga el nodo anterior a el siguiente despues del borrado

        temp = None

    def deletenodeIndex(self,position):
        if self.head is None:
            return "the list is empty LOL"
        if position == 0:
            self.head = self.head.next
            return self.head 
        index=0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None: #checamos que la lista no este vacia
            if index == position:
                temp = current.next 
                break
            prev = current
            current = current.next
            index +=1
        prev.next = temp
        return prev 
        








