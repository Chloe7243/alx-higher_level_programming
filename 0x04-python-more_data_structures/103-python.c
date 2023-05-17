#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, list_len = Py_SIZE(p);
	PyListObject* list_obj = (PyListObject*) p;
	printf("[*] Size of the Python List = %zd\n", list_len);
	printf("[*] Allocated = %zd\n", list_obj->allocated);

	for (i = 0; i < list_len; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
