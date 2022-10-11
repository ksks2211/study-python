#include <Python.h>


// Python Object 
static PyObject *

// define method 
measurer_strlen(PyObject *self, PyObject *args)
{
    char* str;
    int len;
    // string
    if(!PyArg_ParseTuple(args,"s",&str)) return NULL;
    len = strlen(str);
    return Py_BuildValue("i",len); // return Interger
}

// define method name and description
static PyMethodDef MeasurerMethods[] = {
    {"strlen", // method name
    measurer_strlen, // function pointer
    METH_VARARGS, // Tuple arguments
    "count a string length." // method description
    },
    {NULL, NULL, 0 , NULL}
};


static struct PyModuleDef measurermodule = {
    PyModuleDef_HEAD_INIT,
    "measurer", // module name
    "This Module measures", // docs
    -1, 
    MeasurerMethods
};


PyMODINIT_FUNC
PyInit_measurer(void){
    return PyModule_Create(&measurermodule);
}