import axios from "axios";
import { useFormik } from "formik";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { InputText } from "primereact/inputtext";
import { Card } from "primereact/card";
import { MultiSelect } from "primereact/multiselect";
import { Button } from "primereact/button";

const NewMedic = () => {
  const navigate = useNavigate();

  const [specialities, setSpecialities] = useState([]);

  useEffect(() => {
    axios.get('http://4.203.106.91:8000/specialty')
      .then((res) => {
        if (Array.isArray(res.data)) {
          setSpecialities(res.data);
        } else {
          navigate('/');
        }
      })
      .catch((error) => {
        navigate('/');
      });
  }, [navigate]);

  const handleMedicCreate = (data) => {
    const specialityList = data.specialities.map((item) =>  item.id);
    axios.post('http://4.203.106.91:8000/doctor',{
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
      navigate('/');
    })
    .catch(() => {
      navigate('/');
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
      <h2 className="mt-8 ml-5">Nuevo médico</h2>
      <Card>
        <form onSubmit={formik.handleSubmit}>
          <div className="text-left">
            <div className="ml-6 my-3">
              <span className="mr-5">Nombre:</span>
              <InputText
                key="name"
                value={formik.values.name}
                onChange={(e) => {
                  formik.setFieldValue('name', e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Apellido:</span>
              <InputText
                key="lastname"
                value={formik.values.lastname}
                onChange={(e) => {
                  formik.setFieldValue('lastname', e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Rut:</span>
              <InputText
                key="rut"
                value={formik.values.rut}
                onChange={(e) => {
                  formik.setFieldValue('rut', e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Email:</span>
              <InputText
                key="email"
                value={formik.values.email}
                onChange={(e) => {
                  formik.setFieldValue('email', e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Teléfono:</span>
              <InputText
                key="phone"
                value={formik.values.phone}
                onChange={(e) => {
                  formik.setFieldValue('phone', e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Fecha de nacimiento:</span>
              <InputText
                key="birthdate"
                value={formik.values.birthdate}
                onChange={(e) => {
                  formik.setFieldValue('birthdate', e.target.value);
                }}
                placeholder="aaaa-mm-dd"
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Ciudad</span>
              <InputText
                key="city"
                value={formik.values.city}
                onChange={(e) => {
                  formik.setFieldValue('city', e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Especialidades</span>
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
          <Button
            type="submit"
            label="Crear médico"
          />
        </form>
      </Card>
    </div>
  );

};

export default NewMedic;