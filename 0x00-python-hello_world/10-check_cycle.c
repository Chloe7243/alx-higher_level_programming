#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *ptr, *ptr2;

	if (list == NULL)
		return (0);

	ptr = list;
	ptr2 = list->next;
	while (ptr2 != NULL && ptr2->next != NULL)
	{
		if (ptr == ptr2)
			return (1);
		ptr = ptr->next;
		ptr2 = ptr2->next->next;
	}

	return (0);
}
