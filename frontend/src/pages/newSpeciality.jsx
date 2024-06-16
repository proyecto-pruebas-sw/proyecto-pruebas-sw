import axios from "axios";
import { useFormik } from "formik";
import { Button } from "primereact/button";
import { Card } from "primereact/card";
import { InputText } from "primereact/inputtext";
import { Link, useNavigate } from "react-router-dom";
import { backendUrl } from "../config/backend-url";
import { FloatLabel } from "primereact/floatlabel";

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

      if (!/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/.test(values.speciality)) {
        errors.specialityInvalid = 'Especialidad no válida';
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
    <div className="newSpeciality min-h-screen align-items-center align-content-center">
      <Card className="" style={{margin: "100px"}}>
      <div className="home text-left mt-5 ml-8">
        <Link to="/">
            <Button
              className="px-4 w-1"
              icon="pi pi-home"
              size="large"
              severity="info"
            />
          </Link>
      </div>
      <h2 className="mt-3 mb-5">Crear Especialidad</h2>
        <form onSubmit={formik.handleSubmit}>
          
            <InputText
              id="speciality"
              key="speciality"
              className=""
              value={formik.values.speciality}
              onChange={(e) =>
                formik.setFieldValue('speciality', e.target.value)
              }
              placeholder="Ingrese Especialidad"
            />
            <p></p>
          <small className="text-red-500 text-left mt-2 ml-2">{formik.errors.speciality}{formik.errors.specialityInvalid}</small>
          
           <div className="flex flex-row-reverse gap-3 mr-8">
            <Button
              type="submit"
              label="Crear Especialidad"
              disabled={formik.errors.speciality !== undefined}
              severity="success"
              icon="pi pi-plus"
            />
            <Link to="/specialities">
              <Button
                label="Cancelar"
                severity="danger"
                icon="pi pi-times"
              />
            </Link>
          </div>
        </form>
      </Card>
    </div>
  );
};

export default NewSpeciality;