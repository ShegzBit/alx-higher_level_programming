#include "lists.h"

/**
 * check_cycle - checks for a cycle in list
 * @list: list to check through
 * Return: 1 on true | 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *two, *one;

	if (list == NULL)
		return (0);
	two = list;
	one = list;
	while (one != NULL)
	{
		if (!one->next || !one->next->next || !one->next->next->next)
			return (0);
		one = one->next->next;
		if (one == two)
			return (1);
		two = two->next;
		if (one == two)
			return (1);
	}
	return (0);
}
