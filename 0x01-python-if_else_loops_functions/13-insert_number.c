#include "lists.h"
/**
 * insert_node - Add a new node to a list.
 * @head: Address of the first node of a list.
 * @number: number to insert into the new node.
 * Return: Address of the new node.
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *temp2;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);

	temp->n = number;

	if (*head == NULL)
	{
		*head = temp;
		temp->next = NULL;
		return (temp);
	}

	temp2 = *head;
	while (temp2->next)
	{
		if (number < temp2->n)
		{
			temp->next = temp2->next;
			*head = temp;
			break;
		}
		if (number >= temp2->n && number <= temp2->next->n)
		{
			temp->next = temp2->next;
			temp2->next = temp;
			break;
		}
		temp2=temp2->next;
	}
	return (temp);
}
