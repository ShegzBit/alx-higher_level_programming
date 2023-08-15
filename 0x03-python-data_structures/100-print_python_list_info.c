#include <listobject.h>
#include <object.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * type_name - returns the type name of a python object
 * @obj: pyobj to work on
 * Return: typename of the obj
 */
const char *type_name(PyObject *obj)
{
	PyObject *tp = PyObject_Type(obj);

	return (Py_TYPE(tp)->tp_name);
}

/**
 * print_python_list_info - prints the info of a list
 * @p: pointer to object of whose info to print
 */
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p), alloc = ((PyListObject *)p)->allocated;
	int i;
	PyObject *temp;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		temp = PyList_GetItem(p, i);
		print("Element %d: %s\n", i, type_name(temp));
	}
}
