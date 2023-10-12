nclude <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes_obj = (PyBytesObject *)p;
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", Py_SIZE(bytes_obj));
    printf("  trying string: %s\n", PyUnicode_1BYTE_DATA(p));

    printf("  first 10 bytes:");
    size_t i;
    for (i = 0; i < 10 && i < Py_SIZE(bytes_obj); i++) {
        printf(" %02x", bytes_obj->ob_sval[i] & 0xff);
    }
    printf("\n");
}

void print_python_list(PyObject *p) {
    PyListObject *list_obj = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = list_obj->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        }
    }
}

int main(void) {
    setbuf(stdout, NULL);
    PyObject *s = PyBytes_FromString("Hello");
    print_python_bytes(s);
    printf("\n");
    
    PyObject *b = PyBytes_FromString("\xff\xf8\x00\x00\x00\x00\x00\x00");
    print_python_bytes(b);
    printf("\n");

    PyObject *l = PyList_New(0);
    print_python_list(l);
    printf("\n");

    PyList_Append(l, PyBytes_FromString("Hello"));
    PyList_Append(l, PyBytes_FromString("World"));
    PyList_Append(l, PyLong_FromLong(98));
    PyList_Append(l, PyFloat_FromDouble(3.14));
    print_python_list(l);
    printf("\n");

    PyList_SetItem(l, 2, PyBytes_FromString("Holberton"));
    print_python_list(l);

    Py_XDECREF(s);
    Py_XDECREF(b);
    Py_XDECREF(l);
    return 0;
}
