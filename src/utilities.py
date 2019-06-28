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


def generate_dao_interface(model_folder_route, model_name):
	res = '''package %s.%s.dao.interfaces;

public interface I%sDAO {

}
'''

	return res % (model_folder_route.lower(), lower_case(model_name), model_name.capitalize())


def generate_generic_dao_interface(model_folder_route, model_name):
	res = '''package %s.%s.dao.interfaces;


import com.googlecode.genericdao.dao.hibernate.original.GenericDAO;
import %s.%s.model.%s;


public interface I%sGenericoDAO extends GenericDAO<%s, Integer> {

}

'''
	return res % (
		model_folder_route.lower(), lower_case(model_name), model_folder_route.lower(), lower_case(model_name),
		model_name.capitalize(), model_name.capitalize(),
		model_name.capitalize())


def generate_foo_dao(model_folder_route, model_name):
	res = '''package %s.%s.dao;


import %s.%s.dao.interfaces.I%sDAO;
import org.springframework.orm.hibernate5.support.HibernateDaoSupport;


public class %sDAO extends HibernateDaoSupport implements I%sDAO {

}'''

	return res % (
		model_folder_route.lower(), lower_case(model_name), model_folder_route.lower(), lower_case(model_name),
		model_name.capitalize(), model_name.capitalize(), model_name.capitalize())


def generate_foo_generic_dao(model_folder_route, model_name):
	res = '''package %s.%s.dao;


import com.googlecode.genericdao.dao.hibernate.original.GenericDAOImpl;
import %s.%s.dao.interfaces.I%sGenericoDAO;
import %s.%s.model.%s;


public class %sGenericoDAO extends GenericDAOImpl<%s, Integer> implements I%sGenericoDAO {



}
	'''

	return res % (
		model_folder_route.lower(), lower_case(model_name), model_folder_route.lower(), lower_case(model_name),
		model_name.capitalize(), model_folder_route.lower(), lower_case(model_name), model_name.capitalize(),
		model_name.capitalize(), model_name.capitalize(), model_name.capitalize())


def generate_foo_model(model_folder_route, model_name):
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

	return res % (model_folder_route.lower(), lower_case(model_name), camel_case_to_lower_case_underscore(model_name),
				  model_name.capitalize())
