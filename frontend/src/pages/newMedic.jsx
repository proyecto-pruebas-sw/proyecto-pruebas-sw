import axios from "axios";
import { useFormik } from "formik";
import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { InputText } from "primereact/inputtext";
import { Card } from "primereact/card";
import { MultiSelect } from "primereact/multiselect";
import { Button } from "primereact/button";
import { FloatLabel } from 'primereact/floatlabel';
import { Calendar } from 'primereact/calendar';
import { backendUrl } from "../config/backend-url";

const NewMedic = () => {
  const navigate = useNavigate();

  const [specialities, setSpecialities] = useState([]);

  useEffect(() => {
    axios.get(`${backendUrl}/specialty`)
      .then((res) => {
        if (Array.isArray(res.data)) {
          setSpecialities(res.data);
        } else {
          navigate('/', {
            state: {
              response: 'specialityError',
            },
          });
        }
      })
      .catch(() => {
        navigate('/', {
          state: {
            response: 'specialityError',
          },
        });
      });
  }, [navigate]);

  const handleMedicCreate = (data) => {
    const specialityList = data.specialities.map((item) => item.id);
    axios.post(`${backendUrl}/doctor`, {
      name: data.name,
      lastname: data.lastname,
      rut: data.rut,
      email: data.email,
      phone: data.phone,
      birthdate: data.birthdate,
      city: data.city,
      specialties: specialityList,
      educations: [],
      experiences: [],
    })
      .then((res) => {
        console.log(res);
        navigate('/', {
          state: {
            response: 'created',
          },
        });
      })
      .catch(() => {
        navigate('/', {
          state: {
            response: 'error',
          },
        });
      })
  };

  const formik = useFormik({
    validateOnMount: true,
    initialValues: {
      name: '',
      lastname: '',
      rut: '',
      email: '',
      phone: '',
      birthdate: '',
      city: '',
      specialities: [],
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

      if (values.specialities.length === 0) {
        errors.specialities = 'Debe tener al menos una especialidad';
      }

      return errors;
    },
    onSubmit: (data) => {
      console.log("submit");
      handleMedicCreate(data);
      formik.resetForm();
    },
  });

  return (
    <div className="newMedic min-h-screen align-items-center align-content-center" >
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
        <h2 className="mt-3 mb-5">Crear Médico</h2>
        <form onSubmit={formik.handleSubmit}>
          <h3 className="text-left ml-8">Datos personales</h3>
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
          <h3 className="text-left ml-8">Especialidades</h3>
          <div className="specialties my-5 mx-8">
            <div className="px-8">
              <MultiSelect
                id="multiselect_specialities"
                value={formik.values.specialities}
                onChange={(e) => formik.setFieldValue('specialities', e.value)}
                options={specialities}
                display="chip"
                optionLabel="name"
                placeholder="Seleccione especialidad"
              />
            </div>
            <small className="text-red-500">{formik.errors.specialities}</small>
          </div>
          <div className="flex flex-row-reverse gap-3 mr-8">
            <Button
              type="submit"
              label="Crear médico"
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

export default NewMedic;