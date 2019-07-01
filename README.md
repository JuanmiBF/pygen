## Welcome to Pygen webpage

Pygen allows you to generate Java models and extra necessary files by giving some parameters, those models are based on DAO pattern and work over Spring MVC framework.

## How to use it

To use this tool you must download it and open a terminal in the folder ```pygen/src```. Once there you can make it work by typing:
```python pygen.py <model_name> <model_folder_route> <result_path>```

- ```<model_name>``` is the name of the model you want to create, it is optional, if you do not set it, it will become ```foo``` automatically.
- ```<model_folder_route>``` is the route in the project where the model will be created, separated by dots, it is optional, if you do not set it, it will become ```es.beyond.base``` automatically.
- ```<result_path>``` is the path where you want the files to be saved, it is optional, if you do not set it, it will become the current working directory.

Those three parameters are optional as said before, but if they are used, they must be set in the order that is shown in this section.

This is the directory structure that will be generated:

```
foo/
|-- dao/
|   |-- interfaces/
|   |   |-- IFooDAO.java
|   |   |-- IFooGenericoDAO.java
|   |-- FooDAO.java
|   |-- FooGenericoDAO.java
|-- model/
|   |-- Foo.java
|-- service/
|   |--interfaces/
|   |   |-- IFooService.java
|   |-- FooService.java
```


## Requirements
- Python 3.6 or above
