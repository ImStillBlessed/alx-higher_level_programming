#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Function to print Python List info
 * @p: only variable
 * Return: nothing.
 */

void print_python_list(PyObject *p) {
    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_GET_SIZE(p);
        Py_ssize_t allocated = ((PyListObject *)p)->allocated;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %zd\n", allocated);

        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject *element = PyList_GET_ITEM(p, i);
            const char *type = NULL;

            if (PyBytes_Check(element)) {
                type = "bytes";
            } else if (PyFloat_Check(element)) {
                type = "float";
            } else if (PyLong_Check(element)) {
                type = "int";
            } else if (PyUnicode_Check(element)) {
                type = "str";
            } else if (PyTuple_Check(element)) {
                type = "tuple";
            } else if (PyList_Check(element)) {
                type = "list";
            } else {
                type = "unknown";
            }

            printf("Element %zd: %s\n", i, type);
        }
    } else {
        printf("[*] Python list info\n");
        printf("[ERROR] Invalid List Object\n");
    }
}

/**
 * print_pytho _bytes - Function to print Python Bytes info
 * @p: only variable
 * Return: nothing.
 */

void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        Py_ssize_t size = PyBytes_GET_SIZE(p);
        const char *bytes = PyBytes_AsString(p);

        printf("[.] bytes object info\n");
        printf("  size: %zd\n", size);
        printf("  trying string: %s\n", bytes);
        printf("  first 10 bytes: ");
        for (Py_ssize_t i = 0; i < 10 && i < size; i++) {
            printf("%02x ", bytes[i] & 0xff);
        }
        printf("\n");
    } else {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

/**
 * print_python_float - Function to print Python Float info
 * @p: only vafiable.
 * Return: nothing.
 */

void print_python_float(PyObject *p) {
    if (PyFloat_Check(p)) {
        double value = PyFloat_AsDouble(p);

        printf("[.] float object info\n");
        printf("  value: %f\n", value);
    } else {
        printf("[.] float object info\n");
        printf("  [ERROR] Invalid Float Object\n");
    }
}

