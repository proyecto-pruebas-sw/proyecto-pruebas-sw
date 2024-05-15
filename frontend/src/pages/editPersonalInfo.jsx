import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import { InputText } from "primereact/inputtext";
import { InputMask } from "primereact/inputmask";

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
    axios.get(`localhost:8000/doctor/${id}`)
    .then((res) => {
      setMedicData(res.data);
    })
    .catch(() => {
      navigate('/');
    });
  },[id, navigate]);

  const handleChangeName = (name) => {
    setMedicData({...medicData, name: name});
  };

  const handleChangeLastname = (lastname) => {
    setMedicData({...medicData, lastname: lastname});
  };

  const handleChangeRut = (rut) => {
    setMedicData({...medicData, rut: rut});
  };

  const handleChangeEmail = (email) => {
    setMedicData({...medicData, email: email});
  };

  const handleChangePhone = (phone) => {
    setMedicData({...medicData, phone: phone});
  };

  const handleChangeBirthdate = (birthdate) => {
    setMedicData({...medicData, birthdate: birthdate});
  };

  const handleChangeCity = (city) => {
    setMedicData({...medicData, city: city});
  };

  return(
    <div className="editPersonalInfo">
      <div>
        <span>Nombre</span>
        <InputText
          key="name"
          value={medicData.name}
          onChange={(e) => {
            handleChangeName(e.target.value);
          }}
        />
      </div>
      <div>
        <span>Apellido</span>
        <InputText
          key="lastname"
          value={medicData.lastname}
          onChange={(e) => {
            handleChangeLastname(e.target.value);
          }}
        />
      </div>
      <div>
        <span>Rut</span>
        <InputMask
          key="rut"
          value={medicData.rut}
          mask="99.999.999-*"
          onChange={(e) => {
            handleChangeRut(e.target.value);
          }}
        />
      </div>
      <div>
        <span>Email</span>
        <InputText
          key="email"
          value={medicData.email}
          onChange={(e) => {
            handleChangeEmail(e.target.value);
          }}
        />
      </div>
      <div>
        <span>Teléfono</span>
        <InputText
          key="phone"
          value={medicData.phone}
          onChange={(e) => {
            handleChangePhone(e.target.value);
          }}
        />
      </div>
      <div>
        <span>Fecha de nacimiento</span>
        <InputMask
          key="birthdate"
          value={medicData.birthdate}
          onChange={(e) => {
            handleChangeBirthdate(e.target.value);
          }}
          mask="99-99-9999"
          placeholder="dd-mm-aaaa"
        />
      </div>
      <div>
        <span>Ciudad</span>
        <InputText
          key="city"
          value={medicData.city}
          onChange={(e) => {
            handleChangeCity(e.target.value);
          }}
        />
      </div>
    </div>
  );
};
  
export default EditPersonalInfo;