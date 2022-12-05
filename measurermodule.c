#include <Python.h>


// Python Object 
static PyObject* measurer_strlen(PyObject *self, PyObject *args)
{
    char* str;
    int len;
    // string
    if(!PyArg_ParseTuple(args,"s",&str)) return NULL;
    len = strlen(str);
    return Py_BuildValue("i",len); // return Interger
}

static PyObject* measurer_division(PyObject *self, PyObject *args){
    int quotient=0;
    int dividend, divisor = 0;

    if(!PyArg_ParseTuple(args,"ii",&dividend,&divisor)) return NULL;

    
    if(divisor){
        quotient = dividend/divisor;
    }else{
        PyErr_SetString(PyExc_ZeroDivisionError, "divisor must not be zero");
        return NULL;
    }

    return Py_BuildValue("i",quotient);
}

// define method name and description
static PyMethodDef MeasurerMethods[] = {
    {
        "strlen", // method name
        measurer_strlen, // function pointer
        METH_VARARGS, // Tuple arguments
        "count a string length." // method description
    },
    {
        "division",
        measurer_division,
        METH_VARARGS,
        "division function"
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


PyMODINIT_FUNC PyInit_measurer(void){
    return PyModule_Create(&measurermodule);
}