#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	if (list == NULL)
		return (0);
	ptr1 = list;
	ptr2 = ptr1->next;
	while (ptr1 && ptr2)
	{
		ptr1 = ptr2->next;
		ptr2 = ptr1->next;
		if (ptr1 == list || ptr2 == list)
			return (1);
	}
	return (0);
}
