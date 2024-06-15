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

const EditEducationInfo = () => {
  const { doctorId, educationId } = useParams();
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

  const [education, setEducation] = useState({
    doctor_id: '',
    degree: '',
    description: '',
    institution: '',
    city: '',
    country: '',
    start_date: '',
    end_date: '',
  });

  useEffect(() => {
    axios.get(`${backendUrl}/doctor/${doctorId}`)
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
    axios.get(`${backendUrl}/educations/${educationId}`)
      .then((res) => {
        setEducation(res.data);
      })
      .catch(() => {
        navigate('/', {
          state: {
            response: 'notFound',
          },
        });
      });
  }, [doctorId, educationId, navigate]);

  const handleEducationEdit = (data) => {
    axios.put(`${backendUrl}/educations/${educationId}`, {
      degree: data.degree,
      description: data.description,
      institution: data.institution,
      city: data.city,
      country: data.country,
      start_date: data.startDate,
      end_date: data.endDate,
    })
      .then((res) => {
        console.log(res);
        navigate(`/medics/${doctorId}`, {
          state: {
            response: 'educationEdited',
          },
        });
      })
      .catch(() => {
        navigate(`/medics/${doctorId}`, {
          state: {
            response: 'educationEditError',
          },
        });
      });
  };

  const formik = useFormik({
    validateOnMount: true,
    enableReinitialize: true,
    initialValues: {
      degree: education.degree,
      description: education.description,
      institution: education.institution,
      city: education.city,
      country: education.country,
      startDate: education.start_date,
      endDate: education.end_date,
    },
    validate: (values) => {
      const errors = {};

      if (values.degree === '') {
        errors.degreeInvalid = 'Título no puede estar vacío';
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
      handleEducationEdit(data);
      formik.resetForm();
    },
  });

  return (
    <div className="AddEducationInfo">
      <div className="home text-left pt-5 ml-5">
        <Link to="/">
          <Button
            className="px-4 w-1"
            icon="pi pi-home"
            size="large"
            text
            plain
          />
        </Link>
      </div>
      <Card>
        <h2 className="mt-3 mb-5">Editar antecedente académico a {medicData.name} {medicData.lastname}</h2>
        <form onSubmit={formik.handleSubmit}>
          <h3 className="text-left ml-8">Grado</h3>
          <div className="degreeInfo grid grid-nogutter my-5 mx-8">
            <div className="col-4 px-8">
              <FloatLabel>
                <InputText
                  id="input_degree"
                  key="degree"
                  className="w-full"
                  value={formik.values.degree}
                  onChange={(e) => {
                    formik.setFieldValue('degree', e.target.value);
                  }}
                />
                <label htmlFor="degree">Título</label>
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
              label="Añadir antecedente"
              disabled={Object.keys(formik.errors).length !== 0}
            />
            <Link to="/">
              <Button
                label="Cancelar"
                text
              />
            </Link>
          </div>
        </form>
      </Card>
    </div>
  );
};

export default EditEducationInfo;