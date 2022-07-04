#include <Python.h>

/**
 * print_python_list_info - print some basic info about
 *                          Python lists
 * @p: object
 *
 * Return: void
 *
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *listobject;
	PyObject *element;
	int length, i, alloc;

	listobject = (PyListObject *)p;
	length = Py_SIZE(p);
	alloc = (listobject)->allocated;

	printf("[*] Size of the python List = %d\n", length);
	printf("[*] Allocated = %d\n", alloc);

	i = 0;
	while (i < length)
	{
		element = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
		i++;
	}
}
