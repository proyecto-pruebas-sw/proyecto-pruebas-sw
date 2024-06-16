import { useState, useEffect } from "react";
import { Link, useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import { useFormik } from "formik";
import { InputText } from "primereact/inputtext";
import { Card } from "primereact/card";
import { Button } from "primereact/button";
import { FloatLabel } from 'primereact/floatlabel';
import { Calendar } from 'primereact/calendar';
import { InputTextarea } from 'primereact/inputtextarea';
import { backendUrl } from "../config/backend-url";

const AddExperienceInfo = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [medicData, setMedicData] = useState({
    name: '',
    lastname: '',
    rut: '',
    email: '',
    phone: '',
    birthdate: '',
    city: '',
    specialties: [],
    experiences: [],
    educations: [],
  });

  useEffect(() => {
    axios.get(`${backendUrl}/doctor/${id}`)
      .then((res) => {
        setMedicData(res.data);
      })
      .catch(() => {
        navigate('/', {
          state: {
            response: 'notFound',
          },
        });
      });
  }, [id, navigate]);

  const handleExperienceCreate = (data) => {
    axios.post(`${backendUrl}/experiences/${id}`, {
      job_title: data.jobTitle,
      description: data.description,
      institution: data.institution,
      city: data.city,
      country: data.country,
      start_date: data.startDate,
      end_date: data.endDate,
      doctor_id: id,
    })
      .then((res) => {
        console.log(res);
        navigate(`/medics/${id}`, {
          state: {
            response: 'ExperienceEdited',
          },
        });
      })
      .catch(() => {
        navigate(`/medics/${id}`, {
          state: {
            response: 'experienceEditError',
          },
        });
      });
  };

  const formik = useFormik({
    validateOnMount: true,
    initialValues: {
      jobTitle: '',
      description: '',
      institution: '',
      city: '',
      country: '',
      startDate: '',
      endDate: '',
    },
    validate: (values) => {
      const errors = {};

      if (values.jobTitle === '') {
        errors.jobTitle = 'Puesto de trabajo no puede estar vacío';
      }

      if (values.description === '') {
        errors.description = 'Descripción no puede estar vacía';
      }

      if (values.institution === '') {
        errors.institution = 'Institución no puede estar vacía';
      }

      if (values.city === '') {
        errors.city = 'Ciudad no puede estar vacía';
      }

      if (values.country === '') {
        errors.country = 'País no puede estar vacío';
      }

      if (!/^\d{4}-\d{1,2}-\d{1,2}$/.test(values.startDate)) {
        errors.startDate = 'Fecha de inicio no válida';
      }

      if (!/^\d{4}-\d{1,2}-\d{1,2}$/.test(values.endDate)) {
        errors.endDate = 'Fecha de inicio no válida';
      }

      const startDate = new Date(values.startDate);
      const endDate = new Date(values.endDate);

      if (startDate > endDate) {
        errors.dateInvalid = 'Fecha de inicio no puede ocurrir después de la fecha de término';
      }

      return errors;
    },
    onSubmit: (data) => {
      console.log("submit");
      handleExperienceCreate(data);
      formik.resetForm();
    },
  });

  return (
    <div className="AddExperienceInfo min-h-screen align-items-center align-content-center">
      <Card style={{margin: "100px"}}>
        <div className="home text-left pt-5 ml-5">
          <Link to="/">
            <Button
              className="px-4 w-1"
              icon="pi pi-home"
              size="large"
            />
          </Link>
        </div>
        <h2 className="mt-3 mb-5">Agregar experiencia laboral a {medicData.name} {medicData.lastname}</h2>
        <form onSubmit={formik.handleSubmit}>
          <h3 className="text-left ml-8">Experiencia</h3>
          <div className="experienceInfo grid grid-nogutter my-5 mx-8">
            <div className="col-4 px-8">
              <FloatLabel>
                <InputText
                  id="input_job_title"
                  key="jobTitle"
                  className="w-full"
                  value={formik.values.jobTitle}
                  onChange={(e) => {
                    formik.setFieldValue('jobTitle', e.target.value);
                  }}
                />
                <label htmlFor="jobTitle">Nombre del puesto</label>
              </FloatLabel>
              <small className="text-red-500">{formik.errors.degreeInvalid}</small>
            </div>
            <div className="col-4 px-8">
              <FloatLabel>
                <InputTextarea
                  id="input_description"
                  key="description"
                  className="w-full"
                  value={formik.values.description}
                  onChange={(e) => {
                    formik.setFieldValue('description', e.target.value);
                  }}
                />
                <label htmlFor="description">Descripción</label>
              </FloatLabel>
              <small className="text-red-500">{formik.errors.description}</small>
            </div>
            <div className="col-4 px-8">
              <FloatLabel>
                <InputText
                  id="input_institution"
                  key="institution"
                  className="w-full"
                  value={formik.values.institution}
                  onChange={(e) => {
                    formik.setFieldValue('institution', e.target.value);
                  }}
                />
                <label htmlFor="institution">Institución</label>
              </FloatLabel>
              <small className="text-red-500">{formik.errors.institution}</small>
            </div>
            <div className="col-6 px-8 mt-6">
              <FloatLabel>
                <InputText
                  id="input_city"
                  key="city"
                  className="w-full"
                  value={formik.values.city}
                  onChange={(e) => {
                    formik.setFieldValue('city', e.target.value);
                  }}
                />
                <label htmlFor="city">Ciudad</label>
              </FloatLabel>
              <small className="text-red-500">{formik.errors.city}</small>
            </div>
            <div className="col-6 px-8 mt-6">
              <FloatLabel>
                <InputText
                  id="input_country"
                  key="country"
                  className="w-full"
                  value={formik.values.country}
                  onChange={(e) => {
                    formik.setFieldValue('country', e.target.value);
                  }}
                />
                <label htmlFor="country">País</label>
              </FloatLabel>
              <small className="text-red-500">{formik.errors.country}</small>
            </div>
          </div>
          <div className="col-6 px-8 mt-6">
            <div>
              <Calendar id="input_start" key="startDate" dateFormat="yy-mm-dd" value={formik.values.startDate} onChange={(e) => {
                formik.setFieldValue('startDate', e.target.value.toISOString().split('T')[0]);
              }} placeholder="Fecha de inicio" />
            </div>
            <small className="text-red-500">{formik.errors.startDate}</small>
          </div>
          <div className="col-6 px-8 mt-6">
            <div>
              <Calendar id="input_end" key="endDate" dateFormat="yy-mm-dd" value={formik.values.endDate} onChange={(e) => {
                formik.setFieldValue('endDate', e.target.value.toISOString().split('T')[0]);
              }} placeholder="Fecha de término" />
            </div>
            <small className="text-red-500">{formik.errors.endDate}</small>
          </div>
          <div className="flex flex-row-reverse gap-3 mr-8">
            <Button
              type="submit"
              label="Crear antecedente"
              disabled={Object.keys(formik.errors).length !== 0}
              severity="success"
              icon="pi pi-plus"
            />
            <Link to={`/medics/${id}`}>
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

export default AddExperienceInfo;