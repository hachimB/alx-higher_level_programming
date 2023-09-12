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
listint_t *temp = NULL;
if (*head == NULL)
return (NULL);
ptr = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;
while (ptr != NULL)
{
if (ptr->n < number)
{
temp = ptr;
ptr = ptr->next;
}
else
{
if (temp != NULL)
temp->next = new;
else
*head = new;
new->next = ptr;
return (new);
}
}
temp->next = new;
return (new);
}
