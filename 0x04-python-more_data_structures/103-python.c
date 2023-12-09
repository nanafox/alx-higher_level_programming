#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints byte information of a Python object
 * @p: the PythonObject structure
 */
void print_python_bytes(PyObject *p)
{
	ssize_t size, limit;
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	limit = (size >= 10) ? 10 : size + 1;
	printf("  first %ld bytes:", limit);

	for (int i = 0; i < limit; i++)
	{
		printf(" %02x", (string[i] >= 0) ? string[i] : 256 + string[i]);
	}

	printf("\n");
}

/**
 * print_python_list - prints byte information of a Python list
 * @p: the PythonObject structure
 */
void print_python_list(PyObject *p)
{
	ssize_t size = ((PyVarObject *)(p))->ob_size;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (ssize_t i = 0; i < size; i++)
	{
		PyObject *obj = list->ob_item[i];

		printf("Element %ld: %s\n", i, (obj->ob_type)->tp_name);

		if (PyBytes_Check(obj))
		{
			print_python_bytes(obj);
		}
	}
}
