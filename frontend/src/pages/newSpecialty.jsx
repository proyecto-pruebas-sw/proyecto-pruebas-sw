import axios from "axios";
import { useFormik } from "formik";
import { Button } from "primereact/button";
import { Card } from "primereact/card";
import { InputText } from "primereact/inputtext";
import { Link, useNavigate } from "react-router-dom";
import { backendUrl } from "../config/backend-url";

const NewSpecialty = () => {
  const navigate = useNavigate();

  const handleSpecialtyCreate = (data) => {
    axios.post(`${backendUrl}/specialty`,{
      name: data.specialty
    })
    .then((res) => {
      console.log(res);
      navigate('/specialties',{
        state: {
          response: 'created',
        },
      });
    })
    .catch((error) => {
      console.log({error});
      navigate('/specialties',{
        state: {
          response: 'error',
        },
      });
    });
  };

  const formik = useFormik({
    validateOnMount: true,
    initialValues: {
      specialty: '',
    },
    validate: (values) => {
      const errors = {};

      if (values.specialty === '') {
        errors.specialty = 'Especialidad no puede estar vacía'; 
      }

      if (!/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/.test(values.specialty)) {
        errors.specialtyInvalid = 'Especialidad no válida';
      }

      return errors;
    },
    onSubmit: (data) => {
      console.log("submit");
      handleSpecialtyCreate(data);
      formik.resetForm();
    },
  });

  return(
    <div className="newSpecialty min-h-screen align-items-center align-content-center">
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
              id="specialty"
              key="specialty"
              className=""
              value={formik.values.specialty}
              onChange={(e) =>
                formik.setFieldValue('specialty', e.target.value)
              }
              placeholder="Ingrese Especialidad"
            />
            <p></p>
          <small className="text-red-500 text-left mt-2 ml-2">{formik.errors.specialty}{formik.errors.specialtyInvalid}</small>
          
           <div className="flex flex-row-reverse gap-3 mr-8">
            <Button
              type="submit"
              label="Crear Especialidad"
              disabled={formik.errors.specialty !== undefined}
              severity="success"
              icon="pi pi-plus"
            />
            <Link to="/specialties">
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

export default NewSpecialty;