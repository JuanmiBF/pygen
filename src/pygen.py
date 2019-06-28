import os
import sys
import logging

MODEL_NAME = "foo"
TMP_RESULT_PATH = "C:/Users/juanm/OneDrive/Escritorio/Development/PycharmProjects/pygen/pygen/temp_results"
MODEL_FOLDER_ROUTE = sys.argv[3] if len(sys.argv) > 1 and sys.argv[3] is not None else "es.beyond.base"
DAO = "dao"
INTERFACES = "interfaces"

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

lower_case = lambda s: s[:1].lower() + s[1:] if s else ''


def camel_case_to_lower_case_underscore(string):
	"""
	Split string by upper case letters.

	F.e. useful to convert camel case strings to underscore separated ones.

	@return words (list)
	"""
	words = []
	from_char_position = 0
	for current_char_position, char in enumerate(string):
		if char.isupper() and from_char_position < current_char_position:
			words.append(string[from_char_position:current_char_position].lower())
			from_char_position = current_char_position
	words.append(string[from_char_position:].lower())
	return '_'.join(words)


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
		foo_dao_interface.write(generate_dao_interface())

		foo_generic_dao_interface = open("{}/I{}GenericoDAO.java".format(dao_interfaces_path, MODEL_NAME.capitalize()),
										 "w+")
		foo_generic_dao_interface.write(generate_generic_dao_interface())

		foo_dao = open("{}/{}DAO.java".format(dao_path, MODEL_NAME.capitalize()), "w+")
		foo_dao.write(generate_foo_dao())

		foo_generic_dao = open("{}/{}GenericoDAO.java".format(dao_path, MODEL_NAME.capitalize()), "w+")
		foo_generic_dao.write(generate_foo_generic_dao())

		logging.info("DAO files created successfully")
	except Exception as oops:
		logging.error("There was an error creating DAO files: \n{}".format(str(oops)))


def create_model_files(model_path):
	try:

		foo_model = open("{}/{}.java".format(model_path, MODEL_NAME.capitalize()), "w+")
		foo_model.write(generate_foo_model())

		logging.info("Model files created successfully")
	except Exception as oops:
		logging.error("There was an error creating DAO files: \n{}".format(str(oops)))


def create_service_files(service_interfaces_path, service_path):
	try:
		foo_service_interface = open("{}/I{}Service.java".format(service_interfaces_path, MODEL_NAME.capitalize()),
									 "w+")

		foo_service = open("{}/{}Service.java".format(service_path, MODEL_NAME.capitalize()), "w+")

		logging.info("Service files created successfully")
	except Exception as oops:
		logging.error("There was an error creating DAO files: \n{}".format(str(oops)))


def generate_dao_interface():
	res = '''package %s.%s.dao.interfaces;

public interface I%sDAO {

}
'''

	return res % (MODEL_FOLDER_ROUTE.lower(), lower_case(MODEL_NAME), MODEL_NAME.capitalize())


def generate_generic_dao_interface():
	res = '''package %s.%s.dao.interfaces;


import com.googlecode.genericdao.dao.hibernate.original.GenericDAO;
import %s.%s.model.%s;


public interface I%sGenericoDAO extends GenericDAO<%s, Integer> {

}

'''
	return res % (
		MODEL_FOLDER_ROUTE.lower(), lower_case(MODEL_NAME), MODEL_FOLDER_ROUTE.lower(), lower_case(MODEL_NAME),
		MODEL_NAME.capitalize(), MODEL_NAME.capitalize(),
		MODEL_NAME.capitalize())


def generate_foo_dao():
	res = '''package %s.%s.dao;


import %s.%s.dao.interfaces.I%sDAO;
import org.springframework.orm.hibernate5.support.HibernateDaoSupport;


public class %sDAO extends HibernateDaoSupport implements I%sDAO {

}'''

	return res % (
		MODEL_FOLDER_ROUTE.lower(), lower_case(MODEL_NAME), MODEL_FOLDER_ROUTE.lower(), lower_case(MODEL_NAME),
		MODEL_NAME.capitalize(), MODEL_NAME.capitalize(), MODEL_NAME.capitalize())


def generate_foo_generic_dao():
	res = '''package %s.%s.dao;


import com.googlecode.genericdao.dao.hibernate.original.GenericDAOImpl;
import %s.%s.dao.interfaces.I%sGenericoDAO;
import %s.%s.model.%s;


public class %sGenericoDAO extends GenericDAOImpl<%s, Integer> implements I%sGenericoDAO {



}
	'''

	return res % (
		MODEL_FOLDER_ROUTE.lower(), lower_case(MODEL_NAME), MODEL_FOLDER_ROUTE.lower(), lower_case(MODEL_NAME),
		MODEL_NAME.capitalize(), MODEL_FOLDER_ROUTE.lower(), lower_case(MODEL_NAME), MODEL_NAME.capitalize(),
		MODEL_NAME.capitalize(), MODEL_NAME.capitalize(), MODEL_NAME.capitalize())


def generate_foo_model():
	res = '''package %s.%s.model;


import javax.persistence.*;
import java.time.LocalDateTime;
import static javax.persistence.GenerationType.IDENTITY;


@Entity
@Table(name = "%s")
public class %s implements java.io.Serializable {


private Integer id;

// Rest of the attributes

private boolean activo = true;
private String usuarioAlta;
private LocalDateTime fechaAlta;
private String usuarioModificacion;
private LocalDateTime fechaModificacion;
private String usuarioBaja;
private LocalDateTime fechaBaja;

    @Id
    @GeneratedValue(strategy = IDENTITY)
    @Column(name = "id", unique = true, nullable = false)
    public Integer getId() {
        return this.id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    @Column(name = "activo", nullable = false)
    public boolean isActivo() {
        return this.activo;
    }

    public void setActivo(boolean activo) {
        this.activo = activo;
    }

    @Column(name = "usuario_alta", nullable = false, length = 150)
    public String getUsuarioAlta() {
        return this.usuarioAlta;
    }

    public void setUsuarioAlta(String usuarioAlta) {
        this.usuarioAlta = usuarioAlta;
    }

    @Column(name = "fecha_alta", nullable = false, length = 10)
    public LocalDateTime getFechaAlta() {
        return this.fechaAlta;
    }

    public void setFechaAlta(LocalDateTime fechaAlta) {
        this.fechaAlta = fechaAlta;
    }

    @Column(name = "usuario_modificacion", length = 150)
    public String getUsuarioModificacion() {
        return this.usuarioModificacion;
    }

    public void setUsuarioModificacion(String usuarioModificacion) {
        this.usuarioModificacion = usuarioModificacion;
    }

    @Column(name = "fecha_modificacion", length = 10)
    public LocalDateTime getFechaModificacion() {
        return this.fechaModificacion;
    }

    public void setFechaModificacion(LocalDateTime fechaModificacion) {
        this.fechaModificacion = fechaModificacion;
    }

    @Column(name = "usuario_baja", length = 150)
    public String getUsuarioBaja() {
        return this.usuarioBaja;
    }

    public void setUsuarioBaja(String usuarioBaja) {
        this.usuarioBaja = usuarioBaja;
    }

    @Column(name = "fecha_baja", length = 10)
    public LocalDateTime getFechaBaja() {
        return this.fechaBaja;
    }

    public void setFechaBaja(LocalDateTime fechaBaja) {
        this.fechaBaja = fechaBaja;
    }


}


	'''

	return res % (MODEL_FOLDER_ROUTE.lower(), lower_case(MODEL_NAME), camel_case_to_lower_case_underscore(MODEL_NAME),
				  MODEL_NAME.capitalize())


dao_path, dao_interfaces_path, model_path, service_interfaces_path, service_path = create_directories(TMP_RESULT_PATH)
create_dao_files(dao_interfaces_path, dao_path)
create_model_files(model_path)
create_service_files(service_interfaces_path, service_path)
