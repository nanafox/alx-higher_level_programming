#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a pointer to the head node
 * @number: the number to insert
 *
 * Return: the address of the new node on success, else NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL); /* Memory allocation failed*/

	node->n = number;
	current = *head;

	/* handle insertion when the list is empty */
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}

	/* handle insertion at the beginning of the list */
	if (node->n < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	/* find the correct position to insert at */
	while (current->next != NULL && node->n > current->next->n)
		current = current->next;

	/* position found, let's insert the new node */
	node->next = current->next;
	current->next = node;

	return (node);
}
