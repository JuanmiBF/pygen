import os
import sys
import logging
from src.utilities import *

MODEL_NAME = "foo"
TMP_RESULT_PATH = "C:/Users/juanm/OneDrive/Escritorio/Development/PycharmProjects/pygen/pygen/temp_results"
MODEL_FOLDER_ROUTE = sys.argv[3] if len(sys.argv) > 1 and sys.argv[3] is not None else "es.beyond.base"
DAO = "dao"
INTERFACES = "interfaces"

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def create_directories(result_path):
	src_path = "{}/{}".format(result_path, lower_case(MODEL_NAME))  # foo
	dao_path = "{}/{}".format(src_path, DAO)  # foo/dao
	dao_interfaces_path = "{}/{}".format(dao_path, INTERFACES)  # foo/dao/interfaces

	model_path = "{}/{}".format(src_path, "model")  # foo/model
	service_path = "{}/{}".format(src_path, "service")  # foo/service
	service_interfaces_path = "{}/{}".format(service_path, INTERFACES)  # foo/service/interfaces

	try:
		os.mkdir(src_path)
		os.mkdir(dao_path)
		os.mkdir(dao_interfaces_path)
		os.mkdir(model_path)
		os.mkdir(service_path)
		os.mkdir(service_interfaces_path)

		logging.info("Directories created successfully")

		return dao_path, dao_interfaces_path, model_path, service_interfaces_path, service_path
	except OSError as oops:
		logging.error("There was an error creating directories: \n{}".format(str(oops)))


def create_dao_files(dao_interfaces_path, dao_path):
	try:
		foo_dao_interface = open("{}/I{}DAO.java".format(dao_interfaces_path, MODEL_NAME.capitalize()), "w+")
		foo_dao_interface.write(generate_dao_interface(MODEL_FOLDER_ROUTE, MODEL_NAME))

		foo_generic_dao_interface = open("{}/I{}GenericoDAO.java".format(dao_interfaces_path, MODEL_NAME.capitalize()),
										 "w+")
		foo_generic_dao_interface.write(generate_generic_dao_interface(MODEL_FOLDER_ROUTE, MODEL_NAME))

		foo_dao = open("{}/{}DAO.java".format(dao_path, MODEL_NAME.capitalize()), "w+")
		foo_dao.write(generate_foo_dao(MODEL_FOLDER_ROUTE, MODEL_NAME))

		foo_generic_dao = open("{}/{}GenericoDAO.java".format(dao_path, MODEL_NAME.capitalize()), "w+")
		foo_generic_dao.write(generate_foo_generic_dao(MODEL_FOLDER_ROUTE, MODEL_NAME))

		logging.info("DAO files created successfully")
	except Exception as oops:
		logging.error("There was an error creating DAO files: \n{}".format(str(oops)))


def create_model_files(model_path):
	try:

		foo_model = open("{}/{}.java".format(model_path, MODEL_NAME.capitalize()), "w+")
		foo_model.write(generate_foo_model(MODEL_FOLDER_ROUTE, MODEL_NAME))

		logging.info("Model files created successfully")
	except Exception as oops:
		logging.error("There was an error creating DAO files: \n{}".format(str(oops)))


def create_service_files(service_interfaces_path, service_path):
	try:
		foo_service_interface = open("{}/I{}Service.java".format(service_interfaces_path, MODEL_NAME.capitalize()),
									 "w+")
		foo_service_interface.write(generate_service_interface(MODEL_FOLDER_ROUTE, MODEL_NAME))

		foo_service = open("{}/{}Service.java".format(service_path, MODEL_NAME.capitalize()), "w+")
		foo_service.write(generate_service(MODEL_FOLDER_ROUTE, MODEL_NAME))

		logging.info("Service files created successfully")
	except Exception as oops:
		logging.error("There was an error creating DAO files: \n{}".format(str(oops)))


dao_path, dao_interfaces_path, model_path, service_interfaces_path, service_path = create_directories(TMP_RESULT_PATH)
create_dao_files(dao_interfaces_path, dao_path)
create_model_files(model_path)
create_service_files(service_interfaces_path, service_path)
