import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios, { Axios } from "axios";
import { InputText } from "primereact/inputtext";
import { Card } from "primereact/card";
import { useFormik } from "formik";
import { Button } from "primereact/button";
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
        navigate('/');
      });
  }, [id, navigate]);

  const handleChangeName = (name) => {
    setMedicData({ ...medicData, name: name });
  };

  const handleChangeLastname = (lastname) => {
    setMedicData({ ...medicData, lastname: lastname });
  };

  const handleChangeRut = (rut) => {
    setMedicData({ ...medicData, rut: rut });
  };

  const handleChangeEmail = (email) => {
    setMedicData({ ...medicData, email: email });
  };

  const handleChangePhone = (phone) => {
    setMedicData({ ...medicData, phone: phone });
  };

  const handleChangeBirthdate = (birthdate) => {
    setMedicData({ ...medicData, birthdate: birthdate });
  };

  const handleChangeCity = (city) => {
    setMedicData({ ...medicData, city: city });
  };

  const handleModifyMedic = (e) => {
    e.preventDefault();
    axios.put(`http://localhost:8000/doctor/${id}`,{
      name: medicData.name,
      lastname: medicData.lastname,
      rut: medicData.rut,
      email: medicData.email,
      phone: medicData.phone,
      birthdate: medicData.birthdate,
      city: medicData.city,
    })
    .then(() => {
      console.log("modified");
      navigate(`/medics/${id}`);
    })
    .catch((error) => {
      console.log("error");
      navigate(`/medics/${id}`);
    });
  };

  return (
    <div className="editPersonalInfo pt-6">
      <h2 className="text-left ml-5">Editar información personal</h2>
      <Card className="mx-5">
        <form onSubmit={handleModifyMedic}>
          <div className="text-left">
            <div className="ml-6 my-3">
              <span className="mr-5">Nombre:</span>
              <InputText
                id="input_name"
                key="name"
                value={medicData.name}
                onChange={(e) => {
                  handleChangeName(e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Apellido:</span>
              <InputText
                id="input_lastname"
                key="lastname"
                value={medicData.lastname}
                onChange={(e) => {
                  handleChangeLastname(e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Rut:</span>
              <InputText
                id="input_rut"
                key="rut"
                value={medicData.rut}
                onChange={(e) => {
                  handleChangeRut(e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Email:</span>
              <InputText
                id="input_email"
                key="email"
                value={medicData.email}
                onChange={(e) => {
                  handleChangeEmail(e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Teléfono:</span>
              <InputText
                id="input_phone"
                key="phone"
                value={medicData.phone}
                onChange={(e) => {
                  handleChangePhone(e.target.value);
                }}
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Fecha de nacimiento:</span>
              <InputText
                id="input_birthdate"
                key="birthdate"
                value={medicData.birthdate}
                onChange={(e) => {
                  handleChangeBirthdate(e.target.value);
                }}
                placeholder="dd-mm-aaaa"
              />
            </div>
            <div className="ml-6 my-3">
              <span className="mr-5">Ciudad</span>
              <InputText
                id="input_city"
                key="city"
                value={medicData.city}
                onChange={(e) => {
                  handleChangeCity(e.target.value);
                }}
              />
            </div>
          </div>
          <Button
            id="save_changes"
            type="submit"
            label="Guardar cambios"
          />
        </form>
      </Card>
    </div>
  );
};

export default EditPersonalInfo;