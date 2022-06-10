#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * recursion - Function that use a recursion to check palindromic
 * @head: Head of linked list
 * @tail: Node that will be the tail of a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int recursion(listint_t **head, listint_t *tail)
{
	int result = 0;

	if (tail == NULL)
		return (1);

	result = recursion(head, tail->next);
	if (result == 0)
		return (0);
	result = ((*head)->n == tail->n);
	*head = (*head)->next;

	return (result);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (recursion(head, *head));
}
