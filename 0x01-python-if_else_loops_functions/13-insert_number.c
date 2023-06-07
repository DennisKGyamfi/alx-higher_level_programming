#include "lists.h"

/**
* insert_node - Insert number into a sorted singly-linked list
* @head: Ptr to the head of the linked list
* @num: Number to insert
* Return: NULL (if function fails)
* else a ptr to the new node
*/

listint_t *insert_node(listint_t **head, int num)
{
listint_t *node = *head, *new;

new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
new->n = num;
if (node == NULL || node->n >= num)
{
new->next = node;
*head = new;
return (new);
}
while (node && node->next && node->next->n < num)
{
node = node->next;
}
new->next = node->next;
node->next = new;
return (new);
}
