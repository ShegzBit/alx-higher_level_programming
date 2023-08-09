#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a new node in the right position in the sorted list
 * @head: head of the sorted list
 * @number: data to store in new node
 * Return: Pointer to new inserted node | NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *prev_node;
	listint_t *new_head = *head;

	if (head == NULL)
	return (NULL);
	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	temp->next = NULL;
	prev_node = new_head;
	if (*head == NULL)
	{
		*head = temp;
		return (temp);
	}
	if (new_head->next != NULL)
		new_head = new_head->next;
	while (new_head != NULL)
	{
		if (temp->n < prev_node->n)
		{
			temp->next = *head;
			*head = temp;
			break;
		}
		else if (temp->n <= new_head->n && temp->n >= prev_node->n)
		{
			temp->next = new_head;
			prev_node->next = temp;
			break;
		}
		else if (new_head->next == NULL && temp->n > new_head->n)
		{
			new_head->next = temp;
			break;
		}
		prev_node = new_head;
		new_head = new_head->next;
	} return (temp);
}
