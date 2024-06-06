import { useState, useEffect, useRef } from "react";
import { Link, useLocation } from "react-router-dom";
import { InputText } from "primereact/inputtext";
import { Button } from "primereact/button";
import { Dropdown } from "primereact/dropdown";
import { Toolbar } from "primereact/toolbar";
import { Toast } from "primereact/toast";
import MedicTable from "../components/medicTable";
import { backendUrl } from "../config/backend-url";

const ListMedics = () => {

  const location = useLocation();
  const toast = useRef(null);

  const [medics, setMedics] = useState([]);
  const [specialties, setSpecialties] = useState([]);

  const [name, setName] = useState(null);
  const [specialty, setSpecialty] = useState(null);
  const [city, setCity] = useState(null);

  const [loading, setLoading] = useState(false);
  const [urlParams, setUrlParams] = useState("");

  const handleShowToast = () => {
    if (location.state !== null && location.state.response) {
      switch (location.state.response) {
        case 'created':
          toast.current?.show({
            severity: 'created',
            summary: 'Médico creado',
            detail: 'Médico ha sido creado correctamente.',
            life: 5000,
          });
          location.state = null;
          break;
        case 'notFound':
          toast.current?.show({
            severity: 'error',
            summary: 'Error',
            detail: 'Médico no encontrado.',
            life: 5000,
          });
          location.state = null;
          break;
        case 'removed':
          toast.current?.show({
            severity: 'info',
            summary: 'Removido',
            detail: 'Médico ha sido removido del sistema.',
            life: 5000,
          });
          location.state = null;
          break;
        case 'specialityError':
          toast.current?.show({
            severity: 'error',
            summary: 'Error',
            detail: 'Ocurrió un error al intentar recuperar especialidad.',
            life: 5000,
          });
          location.state = null;
          break;
        case 'error':
          toast.current?.show({
            severity: 'error',
            summary: 'Error',
            detail: 'Ocurrió un error al intentar crear médico.',
            life: 5000,
          });
          location.state = null;
          break;
        default:
          break;
      }
    }
  };

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
      <>
        <Link to='/medics/new'>
          <Button
            label="Crear Médico"
            icon="pi pi-plus"
            severity="success"
          />
        </Link>
        <Link  to='/specialities'>
          <Button
            className="ml-3"
            label="Especialidades"
            severity="success"
          />
        </Link>
      </>
    );
  };

  const handleClean = () => {
    setName("");
    setSpecialty("");
    setCity("");
    setUrlParams("");
  };

  useEffect(() => {
    handleShowToast();
    setLoading(true);
    fetch(`${backendUrl}/doctor?${urlParams}`)
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setMedics(data);
        }
        console.log(data);
        setLoading(false);
      })
      .catch(() => {
        setLoading(false);
      });

    fetch(`${backendUrl}/specialty`)
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setSpecialties(data);
        }
        console.log(data);
        setLoading(false);
      })
      .catch(() => {
        setLoading(false);
      });
  }, [urlParams]);

  return (
    <div className="min-h-screen align-items-center align-content-center">
      <Toast ref={toast} />
      <div className="home text-left ml-5">
        <Link to="/">
          <Button
            icon="pi pi-plus"
            label="Salud Integral"
            size="large"
            text
            plain
          />
        </Link>
      </div>
      <h2>Especialistas Médicos</h2>
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

        <Button label="Buscar" onClick={handleSearch} className="w-1 ml-2" loading={loading} />
        <Button label="Limpiar" onClick={handleClean} className="w-1 ml-2" loading={loading} />
      </div>


      <div className="" style={{ margin: "20px" }}>
        <Toolbar className="mb-4" left={leftToolbarTemplate}></Toolbar>
        <MedicTable medics={medics} />
      </div>
    </div>
  );
};

export default ListMedics;
