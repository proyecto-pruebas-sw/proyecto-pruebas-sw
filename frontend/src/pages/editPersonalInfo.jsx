import { useState, useEffect } from "react";
import { useFormik } from "formik";
import { Link, useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import { InputText } from "primereact/inputtext";
import { Card } from "primereact/card";
import { Button } from "primereact/button";
import { FloatLabel } from 'primereact/floatlabel';
import { Calendar } from 'primereact/calendar';
import { backendUrl } from "../config/backend-url";

const EditPersonalInfo = () => {
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

  const formik = useFormik({
    validateOnMount: true,
    enableReinitialize: true,
    initialValues: {
      name: medicData.name,
      lastname: medicData.lastname,
      rut: medicData.rut,
      email: medicData.email,
      phone: medicData.phone,
      birthdate: medicData.birthdate,
      city: medicData.city,
    },
    validate: (values) => {
      const errors = {};
      const nameRegex = /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/;
      const emailRegex = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;


      if(!nameRegex.test(values.name)) {
        errors.nameInvalid = 'Nombre no válido';
      }

      if(!nameRegex.test(values.lastname)) {
        errors.lastnameInvalid = 'Apellido no válido';
      }

      if(!/^(\d{1,3}(?:\d{1,3}){2}-[\dkK])$/.test(values.rut)) {
        errors.rutInvalid = 'Rut no válido'
      }

      if (!emailRegex.test(values.email)) {
        errors.emailInvalid = 'Email no válido';
      }

      if (!/^\d{9}$/.test(values.phone)) {
        errors.phoneInvalid = 'Teléfono no válido';
      }

      if (!/^\d{4}-\d{1,2}-\d{1,2}$/.test(values.birthdate)) {
        errors.birthdateInvalid = 'Fecha de nacimiento no válida';
      }

      if (!nameRegex.test(values.city)) {
        errors.cityInvalid = 'Ciudad no válida';
      }

      return errors;
    },
    onSubmit: (data) => {
      console.log("submit");
      handleModifyMedic(data);
      formik.resetForm();
    },
  });

  const handleModifyMedic = (data) => {
    axios.put(`${backendUrl}/doctor/${id}`,{
      name: data.name,
      lastname: data.lastname,
      rut: data.rut,
      email: data.email,
      phone: data.phone,
      birthdate: data.birthdate,
      city: data.city,
    })
    .then(() => {
      console.log("modified");
      navigate(`/medics/${id}`, {
        state: {
          response: 'modified',
        },
      });
    })
    .catch(() => {
      console.log("error");
      navigate(`/medics/${id}`, {
        state: {
          response: 'modifyError',
        },
      });
    });
  };

  return (
    <div className="editPersonalInfo min-h-screen align-items-center align-content-center">
      
      <Card style={{margin: "100px"}}>
      <div className="home text-left mt-5 ml-8">
        <Link to="/">
          <Button
            className="px-4 w-1"
            icon="pi pi-home"
            size="large"
          />
        </Link>
      </div>
      <h2 className="mb-8">Editar información personal</h2>
        <form onSubmit={formik.handleSubmit}>
        <div className="personalInfo grid grid-nogutter my-5 mx-8">
            <div className="col-4 px-8">
              <FloatLabel>
                <InputText
                  id="input_name"
                  key="name"
                  className="w-full"
                  value={formik.values.name}
                  onChange={(e) => {
                    formik.setFieldValue('name', e.target.value);
                  }}
                />
                <label htmlFor="name">Nombre</label>
              </FloatLabel>
              <small className="text-red-500">{formik.errors.nameInvalid}</small>
            </div>
            <div className="col-4 px-8">
              <FloatLabel>
                <InputText
                  id="input_lastname"
                  key="lastname"
                  className="w-full"
                  value={formik.values.lastname}
                  onChange={(e) => {
                    formik.setFieldValue('lastname', e.target.value);
                  }}
                />
                <label htmlFor="lastname">Apellido</label>
              </FloatLabel>
              <small className="text-red-500">{formik.errors.lastnameInvalid}</small>
            </div>
            <div className="col-4 px-8">
              <FloatLabel>
                <InputText
                  id="input_rut"
                  key="rut"
                  className="w-full"
                  value={formik.values.rut}
                  onChange={(e) => {
                    formik.setFieldValue('rut', e.target.value);
                  }}
                />
                <label htmlFor="rut">RUT (sin puntos y con guión)</label>
              </FloatLabel>
              <small className="text-red-500">{formik.errors.rutInvalid}</small>
            </div>
            <div className="col-6 px-8 mt-6">
              <div>
                <Calendar id="input_birthdate" key="birthdate" dateFormat="yy-mm-dd" value={formik.values.birthdate} onChange={(e) => {
                  formik.setFieldValue('birthdate', e.target.value.toISOString().split('T')[0]);
                }} placeholder="Fecha de nacimiento" />
              </div>
              <small className="text-red-500">{formik.errors.birthdateInvalid}</small>
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
              <small className="text-red-500">{formik.errors.cityInvalid}</small>
            </div>
          </div>
          <h3 className="text-left ml-8">Datos de contacto</h3>
          <div className="contactInfo grid grid-nogutter my-5 mx-8">
            <div className="col-6 px-8">
              <FloatLabel>
                <InputText
                  id="input_email"
                  key="email"
                  className="w-full"
                  value={formik.values.email}
                  onChange={(e) => {
                    formik.setFieldValue('email', e.target.value);
                  }}
                />
                <label htmlFor="email">Email</label>
              </FloatLabel>
              <small className="text-red-500">{formik.errors.emailInvalid}</small>
            </div>
            <div className="col-6 px-8">
              <div className="p-inputgroup flex-1 w-full">
                <span className="p-inputgroup-addon">
                  +56
                </span>
                <InputText
                  id="input_phone"
                  key="phone"
                  placeholder="Teléfono"
                  value={formik.values.phone}
                  onChange={(e) => {
                    formik.setFieldValue('phone', e.target.value);
                  }}
                />
              </div>
              <small className="text-red-500">{formik.errors.phoneInvalid}</small>
            </div>
          </div>
          <div className="flex flex-row-reverse gap-3 mr-8">
            <Button
              type="submit"
              label="Guardar cambios"
              disabled={Object.keys(formik.errors).length !== 0}
              severity="success"
              icon="pi pi-save"
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

export default EditPersonalInfo;