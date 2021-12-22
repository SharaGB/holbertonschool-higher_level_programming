#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * @brief 
 * 
 */
 listint_t *insert_node(listint_t **head, int number)
 {
     int key = number;
     listint_t *tmp = *head;
     listint_t *new = malloc(sizeof(listint_t));

    if (!new)
    {
        free(new);
        return (NULL);
    }
     new->n = number;
     new->next = *head;
     if (head == NULL || key < (*head)->n)
     {
         new->next = *head;
         *head = new;
     }
     else
     {
         tmp = *head;
         {
             while (tmp->next != NULL && tmp->next->n < key)
             {
                 tmp = tmp->next;
             }
             new->next = tmp->next;
             tmp->next = new;
         }
     }
     return (new);
 }
