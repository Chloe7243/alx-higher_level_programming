#include <Python.h>
#include <object.h>
#include <listobject.h>


void print_python_bytes(PyObject* p)
{
	Py_ssize_t i, size, m;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("[Error] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	m = size > 10 ? 10 : size + 1;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %zd bytes: ", m);
	for (i = 0; i < m ; i++)
		printf("%02hhX%s", PyBytes_AsString(p)[i], i + 1 < m ? " " : "");
	printf("\n");
}

void print_python_list(PyObject *p)
{
	Py_ssize_t i, list_len = PyList_Size(p);
	PyListObject* list_obj = (PyListObject*) p;
	printf("[*] Python List info\n");
	printf("[*] Size of the Python List = %zd\n", list_len);
	printf("[*] Allocated = %zd\n", list_obj->allocated);

	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{printf("Element %zd: %s\n", i,
			((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
	if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
		print_python_bytes(((PyListObject *)p)->ob_item[i]);

	}
}
