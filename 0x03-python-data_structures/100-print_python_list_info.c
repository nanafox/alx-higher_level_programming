#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: Python object
 */
void print_python_list_info(PyObject *p)
{
	ssize_t i, size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
