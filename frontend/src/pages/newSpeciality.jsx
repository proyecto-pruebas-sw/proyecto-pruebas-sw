import axios from "axios";
import { useFormik } from "formik";
import { Button } from "primereact/button";
import { Card } from "primereact/card";
import { InputText } from "primereact/inputtext";
import { Link, useNavigate } from "react-router-dom";
import { backendUrl } from "../config/backend-url";

const NewSpeciality = () => {
  const navigate = useNavigate();

  const handleSpecialityCreate = (data) => {
    axios.post(`${backendUrl}/specialty`,{
      name: data.speciality
    })
    .then((res) => {
      console.log(res);
      navigate('/specialities',{
        state: {
          response: 'created',
        },
      });
    })
    .catch((error) => {
      console.log({error});
      navigate('/specialities',{
        state: {
          response: 'error',
        },
      });
    });
  };

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
      console.log("submit");
      handleSpecialityCreate(data);
      formik.resetForm();
    },
  });

  return(
    <div className="newSpeciality">
      <div className="home text-left mt-5 ml-8">
        <Link to="/">
          <Button
            className="px-4 w-1"
            icon="pi pi-home"
            size="large"
          />
        </Link>
      </div>
      <h2 className="mt-8 ml-5">Crear especialidad</h2>
      <Card>
        <form onSubmit={formik.handleSubmit}>
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
            disabled={formik.errors.speciality !== undefined}
          />
        </form>
      </Card>
    </div>
  );
};

export default NewSpeciality;