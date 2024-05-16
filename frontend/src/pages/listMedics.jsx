import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { InputText } from "primereact/inputtext";
import { Button } from "primereact/button";
import { Dropdown } from "primereact/dropdown";
import { Toolbar } from "primereact/toolbar";
import { useEffect } from "react";
import MedicTable from "../components/medicTable";
import { backendUrl } from "../config/backend-url";

const ListMedics = () => {
  const [medics, setMedics] = useState([]);
  const [specialties, setSpecialties] = useState([]);

  const [name, setName] = useState(null);
  const [specialty, setSpecialty] = useState(null);
  const [city, setCity] = useState(null);

  const [loading, setLoading] = useState(false);
  const [urlParams, setUrlParams] = useState("");

  const handleSearch = () => {
    let params = "";
    if (name) {
      params += `&doctor_name=${name}`;
    }
    if (specialty) {
      params += `&specialty_id=${specialty}`;
    }
    if (city) {
      params += `&doctor_city=${city}`;
    }
    setUrlParams(params);
  };

  const leftToolbarTemplate = () => {
    return (
      <Link to='/medics/new'>
        <Button
          label="Crear Médico"
          icon="pi pi-plus"
          severity="success"
        />
      </Link>
    );
  };

  const handleClean = () => {
    setName("");
    setSpecialty("");
    setCity("");
    setUrlParams("");
  };

  useEffect(() => {
    setLoading(true);
    fetch(`${backendUrl}/doctor?` + urlParams)
      .then((res) => res.json())
      .then((data) => {
        setMedics(data);
        console.log(data);
        setLoading(false);
      });

    fetch(`${backendUrl}/specialty`)
      .then((res) => res.json())
      .then((data) => {
        setSpecialties(data);
        console.log(data);
        setLoading(false);
      });
  }, [urlParams]);

  return (
    <div className="h-screen align-items-center align-content-center">
      <h1>Especialistas Médicos</h1>
      <div className="">
        <InputText
          className="w-3 my-auto m-1"
          value={name}
          onChange={(e) => setName(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleSearch();
          }}
          placeholder="Nombre"
        />
        <InputText
          className="w-3 my-auto m-1"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleSearch();
          }}
          placeholder="Ciudad"
        />
        <Dropdown
          className="w-1 my-auto m-1"
          value={specialty}
          onChange={(e) => setSpecialty(e.target.value)}
          options={specialties}
          optionLabel="name"
          optionValue="id"
          placeholder="Especialidad"
          filter
        />
        
        <Button label="Buscar" onClick={handleSearch} className="w-1 ml-2" loading={loading}/>
        <Button label="Limpiar" onClick={handleClean}className="w-1 ml-2" loading={loading}/>
      </div>
      

      <div className="" style={{ margin: "20px" }}>
        <Toolbar className="mb-4" left={leftToolbarTemplate}></Toolbar>
        <MedicTable medics={medics} />
      </div>
    </div>
  );
};

export default ListMedics;
