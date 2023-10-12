#include "lists.h"

/**
 * print_dlistint - prints the values of a d list
 * @h: pointer to the first node
 * Return: 0 Always.
 */

size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t current;
	size_t node_count;

	current = h;
	node_count = 0;
	while (curent != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		node_count++;
	}
	return (node_count);
}
