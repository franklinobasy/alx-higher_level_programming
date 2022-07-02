#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * 
 * @head: pointer to linked list head
 * 
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * 
 */

int is_palindrome(listint_t **head)
{
		int *values;
		listint_t *current, *nodes;
		unsigned int n, i, value, j;

		if (head == NULL)
			return (0);

		n = n_listint(*head);
		values = malloc(n * sizeof(int));
		nodes = malloc(n * sizeof(listint_t));

		current = *head;
		if (current == NULL)
				return (1);

		i = 0;
		while (current != NULL)
		{
				value = current->n;
				values[i] = value;
				nodes[i] = *current;
				current = current->next;
				i++;
		}

		i--;
		n = 1;
		j = 0;
		while (i >= n)
		{
				current = &nodes[i];
				if (current->n != values[j])
				{
					free(values);
					free(nodes);
					return (0);
				}
				i--;
				j++;
		}

		free(values);
		free(nodes);

		return (1);
}

/**
 * n_listint - counts elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */

size_t n_listint(const listint_t *h)
{
		const listint_t *current;
		unsigned int n; /* number of nodes */

		current = h;
		n = 0;
		while (current != NULL)
		{
				current = current->next;
				n++;
		}

		return (n);
}
