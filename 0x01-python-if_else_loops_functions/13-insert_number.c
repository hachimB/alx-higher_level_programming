#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *@head: first node.
 *@number: integer.
 * Return: node.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *ptr;
listint_t *new;
if (*head == NULL)
return (NULL);
ptr = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;
new->next = ptr->next;
ptr->next = new;
return (new);
}
