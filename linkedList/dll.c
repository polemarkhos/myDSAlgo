# include <stdlib.h>
# include <stdio.h>
# include <string.h>

int main() {
    return 1;
}

typedef struct DoublyLinkedListNode {
    struct DoublyLinkedListNode* prev;
    struct DoublyLinkedListNode* next;
    char* data;
} DoublyLinkedListNode;

typedef struct DoublyLinkedList {
    DoublyLinkedListNode* head;
    DoublyLinkedListNode* tail;
} DoublyLinkedList;

int InsertDoublyLinkedListNode (DoublyLinkedList *DLList, const char* data) {
    /**  
    * taking a pointer to the list, we want to set the prev of the head node to NULL
    * then insert a node with a prev pointer to the head and a next pointer to
    * the previous head node
    */

    DoublyLinkedListNode *newDLLNode = (DoublyLinkedListNode *)malloc(sizeof(DoublyLinkedListNode));
    if (newDLLNode == NULL) {
        perror("Failed to allocate memory for new node");
        return 0;
    }

    newDLLNode->data = strdup(data);
    newDLLNode->prev = NULL;
    newDLLNode->next = DLList->head;

    DLList->head = newDLLNode; 

    return 1;
}

DoublyLinkedListNode *FindInList(DoublyLinkedList *DLList, const char *data) {
    /* find a certain string. if it doesnt match iterate till we end
     */

    DoublyLinkedListNode* current = DLList->head; 

    while(current != NULL) {
        if(strcmp(data, current->data) == 0) {
            return current;
        }
        current = current-> next;
    }
    return NULL;
}

int DeleteNode(DoublyLinkedList *DLList, DoublyLinkedListNode *target) {
    if (target == NULL) {
        perror("Nothing to delete");
        return 0; //nothing to delete
    }
    
    if (target->prev != NULL)  {
        target->prev->next = target->next;
    } else {
        DLList->head = target->next;
    }

    if (target->next != NULL) {
        target->next->prev = target->prev;
    } else {
        DLList->tail = target->prev;
    }

    free(target->data);
    free(target);

    return 1;
}
