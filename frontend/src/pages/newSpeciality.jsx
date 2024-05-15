import axios from "axios";
import { useFormik } from "formik";
import { Button } from "primereact/button";
import { Card } from "primereact/card";
import { InputText } from "primereact/inputtext";
import { useNavigate } from "react-router-dom";

const NewSpeciality = () => {
  const navigate = useNavigate();

  const formik = useFormik({
    validateOnMount: true,
    initialValues: {
      speciality: '',
    },
    validate: (values) => {
      const errors = {};

      if (values.speciality === '') {
        errors.speciality = 'Especialidad no puede estar vacía';
      }

      return errors;
    },
    onSubmit: (data) => {
      handleSpecialityCreate(data);
      formik.resetForm();
    },
  });

  const handleSpecialityCreate = (data) => {
    axios.post('http://4.203.106.91:8000/speciality',{
      name: data.speciality
    })
    .then((res) => {
      navigate('/');
    })
    .catch((error) => {
      navigate('/');
    });
  };

  return(
    <div className="newSpeciality">
      <h2 className="mt-8 ml-5">Crear especialidad</h2>
      <Card>
        <label htmlFor="speciality" className="block">
          Nombre
        </label>
        <InputText
          id="speciality"
          value={formik.values.speciality}
          onChange={(e) =>
            formik.setFieldValue('speciality', e.target.value)
          }
        />
        <small className="text-red-500">{formik.errors.speciality}</small>
        <Button
          type="submit"
          label="Crear especialidad"
          disabled={formik.errors.speciality === undefined}
        />
      </Card>
    </div>
  );
};

export default NewSpeciality;