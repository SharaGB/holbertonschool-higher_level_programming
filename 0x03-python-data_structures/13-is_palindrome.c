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
	listint_t *second, *prev = *head;
	listint_t *midnode = NULL;

	if (*head == NULL)
	{
		return (1);
	}
	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev = low;
			low = low->next;
		}
	}
	if (fast != NULL)
	{
		midnode = low;
		low = low->next;
	}
	second = low;
	prev->next = NULL;
	if (midnode != NULL)
	{
		prev->next = midnode;
		midnode->next = second;
	}
	else
	{
		prev->next = second;
	}
	return (0);
}
