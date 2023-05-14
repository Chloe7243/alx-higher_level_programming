#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int i = 0, len, *numbers;

	if (*head == NULL)
		return (1);

	numbers = malloc(sizeof(int) * 1000);

	ptr = *head;
	while (ptr)
	{
		numbers[i] = ptr->n;
		ptr = ptr->next;
		i++;
	}
	if (i == 1)
		return (0);
	len = i;
	for (i = 0; i < (len / 2); i++)
	{
		if (numbers[i] != numbers[(len - i) - 1])
		{
			free(numbers);
			return (0);
		}
	}

	free(numbers);
	return (1);
}
