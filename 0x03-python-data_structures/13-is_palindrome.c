#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: the head node of the linked list
 * Return: 1 if is palindrome | 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp2;
	int *stack, used = 0, size = 1;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	stack = malloc(sizeof(int) * size);
	if (stack == NULL)
		return (0);
	temp = *head;
	temp2 = *head;
	while (temp != NULL)
	{
		stack[used++] = temp->n;
		if (used >= size)
		{
			stack = realloc(stack, (sizeof(int) * (++size)));
			if (stack == NULL)
			{
				free(stack);
				return (0);
			}
		}
		temp = temp->next;
	}
	used--;
	while (temp2 != NULL)
	{
		if (temp2->n != stack[used--])
		{
			free(stack);
			return (0);
		}
		temp2 = temp2->next;
	} free(stack);
	return (1);
}
