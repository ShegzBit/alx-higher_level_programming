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

	if (head == NULL || *head == NULL)
	return (NULL);

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	prev_node = new_head;
	new_head = new_head->next;

	while (new_head != NULL)
	{
		/*Check if temp shoul be at start*/
		if (temp->n < prev_node->n)
		{
			temp->next = *head;
			*head = temp;
			break;
		}
		/*Check if node is right above prev and right below head*/
		else if (temp->n < new_head->n && temp->n > prev_node->n)
		{
			temp->next = new_head;
			prev_node->next = temp;
			break;
		}
		else if (new_head->next == NULL && temp->n > new_head->n)
		{
			temp->next = NULL;
			new_head->next = temp;
			break;
		}
		prev_node = new_head;
		new_head = new_head->next;
	}
	return (temp);
}
