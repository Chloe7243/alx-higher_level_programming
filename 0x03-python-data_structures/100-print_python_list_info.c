#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p);

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_len = PyList_Size(p);
	printf("%zu", list_len);
}
