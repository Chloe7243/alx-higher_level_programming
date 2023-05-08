#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *ptr;
	listint_t **nodes;
	int i;

	if (list == NULL)
		return (0);

	nodes = malloc(sizeof(listint_t) * 1000);
	ptr = list;
	ptr2 = list->next;
	while (ptr != NULL)
	{
		for (i = 0; nodes[i] != NULL; i++)
			if (ptr == nodes[i])
			{
				free(nodes);
				return (1);
			}
		nodes[i++] = ptr;
		nodes[i] = NULL;
		ptr = ptr->next;
	}

	free(nodes);
	return (0);
}
