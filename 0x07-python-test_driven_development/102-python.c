#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: The Python object to work with. (Must be a string object).
 */
void print_python_string(PyObject *p)
{
	ssize_t size;

	printf("[.] string object info\n");

	/* ensure the object is a valid string object */
	if (strcmp((p->ob_type)->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  type: compact ascii\n");
	}
	else
	{
		printf("  type: compact unicode object\n");
	}

	/* get the size/length of the  string object */
	size = ((PyASCIIObject *)p)->length;
	printf("  length: %ld\n", size);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &size));
}
