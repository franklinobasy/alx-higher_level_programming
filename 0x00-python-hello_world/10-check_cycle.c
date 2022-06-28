#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list 
                 has a cycle in it.
 * @list: A singly-linked list.
 *
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *canoe, *yatch;

	if (list == NULL || list->next == NULL)
		return (0);

	canoe = list->next;
	yatch = list->next->next;

	while (canoe && yatch && yatch->next)
	{
		if (canoe == yatch)
			return (1);

		canoe = canoe->next;
		yatch = yatch->next->next;
	}

	return (0);
}