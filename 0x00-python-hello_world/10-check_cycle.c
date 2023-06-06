#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: list to check
* Return: 0(no cycle) and 1(if cycle)
*/

int check_cycle(listint_t *list)
{
listint_t *first, *last = list;

if (list == NULL)
return (0);
first = list->next;
while (last != NULL && first != NULL && first->next != NULL)
{
if (last == first)
return (1);
first = first->next->next;
last = last->next;
}
return (0);
}
