
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer to head pointer
 * @number: number to insert
 * Return: listint_t*
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev;
	listint_t *new;
	listint_t *current;
	int n;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (current == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}

	while (current != NULL)
	{
		n = current->n;
		if (n > number)
		{
			break;
		}

		prev = current;
		current = current->next;
	}

	new->next = current;
	if (current == *head)
		*head = new;
	else:
		prev->next = new;

	return (new);
}
