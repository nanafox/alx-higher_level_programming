#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints basic information about Python bytes
 * @p: a Python object
 */
void print_python_bytes(PyObject *p)
{
	ssize_t size, limit;
	char *string;

	fprintf(stdout, "[.] bytes object info\n");

	/* check for invalid byte objects */
	if (!PyBytes_Check(p))
	{
		fprintf(stdout, "  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	/* ensure we are getting at most  10 bytes */
	limit = (size >= 10) ? 10 : size + 1;

	fprintf(stdout, "  size: %ld\n", size);
	fprintf(stdout, "  trying string: %s\n", string);
	fprintf(stdout, "  first %ld bytes:", limit);

	for (ssize_t i = 0; i < limit; i++)
	{
		fprintf(stdout, " %02x",
				(string[i] >= 0) ? string[i] : 256 + string[i]);
	}

	fprintf(stdout, "\n");
	fflush(stdout);
}

/**
 * print_python_float - prints basic information about Python floats
 * @p: a Python object
 */
void print_python_float(PyObject *p)
{
	fprintf(stdout, "[.] float object info\n");

    /* check for Float objects */
	if (!PyFloat_Check(p))
	{
		fprintf(stdout, "  [ERROR] Invalid Float Object\n");
		return;
	}

	/* print the floating-point value */
	PyFloatObject *val = ((PyFloatObject *)p);

    /* ensure the returned number does not look like an integer */
	char *py_double_str =
		PyOS_double_to_string(val->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

    /* print the result and flush stdout */
	fprintf(stdout, "  value: %s\n", py_double_str);
	fflush(stdout);

    /* cleanup memory for the received string */
	PyMem_Free(py_double_str);
}

/**
 * print_python_list - prints basic information about Python list
 * @p: a Python object
 */
void print_python_list(PyObject *p)
{
	ssize_t size = ((PyVarObject *)p)->ob_size;
	PyListObject *list = (PyListObject *)p;

	fprintf(stdout, "[*] Python list info\n");

	/* check for invalid Python List Objects */
	if (!PyList_Check(list))
	{
		fprintf(stdout, "  [ERROR] Invalid List Object\n");
		return;
	}

	fprintf(stdout, "[*] Size of the Python List = %ld\n", size);
	fprintf(stdout, "[*] Allocated = %ld\n", list->allocated);

    /* print information about all list items */
	for (ssize_t i = 0; i < size; i++)
	{
		PyObject *obj = list->ob_item[i];

		fprintf(stdout, "Element %ld: %s\n", i, (obj->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		else if (PyFloat_Check(obj))
			print_python_float(obj);
	}
}
