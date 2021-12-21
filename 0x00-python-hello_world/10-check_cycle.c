#include "lists.h"
/**
 * check_cycle - Function that checks if a singly linked list has a cycle in it
 * @list: A pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fastptr;
	listint_t *slowptr;

	if (list != NULL)
	{
		fastptr = list;
		slowptr = list;
	}
	while (fastptr && fastptr->next)
	{
		if (fastptr->next->next == slowptr)
		{
			return (1);
		}
		fastptr = fastptr->next->next;
		slowptr = slowptr->next;
	}
	return (0);
}
