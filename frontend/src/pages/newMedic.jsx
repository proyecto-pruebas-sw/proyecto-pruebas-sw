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

      if (values.name === '') {
        errors.name = 'Nombre no puede estar vacío';
      }

      if (values.lastname === '') {
        errors.lastname = 'Apellido no puede estar vacío';
      }

      if (values.rut === '') {
        errors.rut = 'Rut no puede estar vacío';
      }

      if (values.email === '') {
        errors.email = 'Email no puede estar vacío';
      }

      if (values.phone === '') {
        errors.phone = 'Teléfono no puede estar vacío';
      }

      if (values.birthdate === '') {
        errors.birthdate = 'Fecha de nacimiento no puede estar vacía';
      }

      if (values.city === '') {
        errors.city = 'Ciudad no puede estar vacía';
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
    <div className="newMedic">
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
        <h2 className="mt-3 mb-5">Nuevo médico</h2>
        <form onSubmit={formik.handleSubmit}>
          <h3 className="text-left ml-8">Datos personales</h3>
          <div className="personalInfo grid grid-nogutter my-5 mx-8">
            <div className="col-4 px-8">
              <FloatLabel>
                <InputText
                  id="name"
                  key="name"
                  className="w-full"
                  value={formik.values.name}
                  onChange={(e) => {
                    formik.setFieldValue('name', e.target.value);
                  }}
                />
                <label htmlFor="name">Nombre</label>
              </FloatLabel>
            </div>
            <div className="col-4 px-8">
              <FloatLabel>
                <InputText
                  id="lastname"
                  key="lastname"
                  className="w-full"
                  value={formik.values.lastname}
                  onChange={(e) => {
                    formik.setFieldValue('lastname', e.target.value);
                  }}
                />
                <label htmlFor="lastname">Apellido</label>
              </FloatLabel>
            </div>
            <div className="col-4 px-8">
              <FloatLabel>
                <InputText
                  id="rut"
                  key="rut"
                  className="w-full"
                  value={formik.values.rut}
                  onChange={(e) => {
                    formik.setFieldValue('rut', e.target.value);
                  }}
                />
                <label htmlFor="rut">RUT</label>
              </FloatLabel>
            </div>
            <div className="col-6 px-8 mt-6">
              <Calendar id="birthdate" key="birthdate" value={formik.values.birthdate} onChange={(e) => {
                formik.setFieldValue('birthdate', e.target.value);
              }} placeholder="Fecha de nacimiento" />
            </div>
            <div className="col-6 px-8 mt-6">
              <FloatLabel>
                <InputText
                  id="city"
                  key="city"
                  className="w-full"
                  value={formik.values.city}
                  onChange={(e) => {
                    formik.setFieldValue('city', e.target.value);
                  }}
                />
                <label htmlFor="city">Ciudad</label>
              </FloatLabel>
            </div>
          </div>
          <h3 className="text-left ml-8">Datos de contacto</h3>
          <div className="contactInfo grid grid-nogutter my-5 mx-8">
            <div className="col-6 px-8">
              <FloatLabel>
                <InputText
                  id="email"
                  key="email"
                  className="w-full"
                  value={formik.values.email}
                  onChange={(e) => {
                    formik.setFieldValue('email', e.target.value);
                  }}
                />
                <label htmlFor="email">Email</label>
              </FloatLabel>
            </div>
            <div className="col-6 px-8">
              <div className="p-inputgroup flex-1 w-full">
                <span className="p-inputgroup-addon">
                  +56
                </span>
                <InputText
                  id="phone"
                  key="phone"
                  placeholder="Teléfono"
                  value={formik.values.phone}
                  onChange={(e) => {
                    formik.setFieldValue('phone', e.target.value);
                  }}
                />
              </div>
            </div>
          </div>
          <h3 className="text-left ml-8">Especialidades</h3>
          <div className="specialties my-5 mx-8">
            <div className="px-8">
              <MultiSelect
                value={formik.values.specialities}
                onChange={(e) => formik.setFieldValue('specialities', e.value)}
                options={specialities}
                display="chip"
                optionLabel="name"
                placeholder="Seleccione especialidad"
              />
            </div>
          </div>
          <div className="flex flex-row-reverse gap-3 mr-8">
            <Button
              type="submit"
              label="Crear médico"
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