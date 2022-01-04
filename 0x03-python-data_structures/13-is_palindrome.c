#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - Functionthat checks if a singly linked list is a palindrome.
 * @head: Check head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *low = *head;
	listint_t *fast = *head;

	if (*head == NULL)
	{
		return (1);
	}
	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			low = low->next;
		}
		return (1);
	}
	return (0);
}
