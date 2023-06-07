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
listint_t *node = *head, *newNum;

newNum = malloc(sizeof(listint_t));
if (newNum == NULL)
{
return (NULL);
}
newNum->n = num;
if (node == NULL || node->n >= num)
{
newNum->next = node;
*head = newNum;
return (newNum);
}
while (node && node->next && node->next->n < num)
{
node = node->next;
}
newNum->next = node->next;
node->next = newNum;
return (newNum);
}
