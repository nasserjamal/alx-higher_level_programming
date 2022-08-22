#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list cycles
 *
 * @list: Head node
 * Return: 0 if no cycle and 1 if cycles
 */
int check_cycle(listint_t *list)
{
listint_t *current;
listint_t *loop;

if (list == NULL)
	return (0);

current = list;
while (current != NULL)
{
	loop = current->next;
	while (loop != NULL)
	{
		if (loop == current)
			return (1);
		loop = loop->next;
	}
	current = current->next;
}
return (0);
}
