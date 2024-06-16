import { useEffect, useState, useRef } from "react";
import axios from "axios";
import { Button } from "primereact/button";
import { Column } from "primereact/column";
import { DataTable } from "primereact/datatable";
import { Link, useNavigate, useLocation } from "react-router-dom";
import { Toast } from 'primereact/toast';
import { backendUrl } from "../config/backend-url";
import { Toolbar } from "primereact/toolbar";

const Specialities = () => {
  const navigate = useNavigate();

  const location = useLocation();
  const toast = useRef(null);

  const [specialities, setSpecialities] = useState([]);

  const handleShowToast = () => {
    if (location.state !== null && location.state.response) {
      switch (location.state.response) {
        case 'created':
          toast.current?.show({
            severity: 'success',
            summary: 'Especialidad creada',
            detail: 'Especialidad ha sido creada correctamente.',
            life: 5000,
          });
          location.state = null;
          break;
        case 'error':
          toast.current?.show({
            severity: 'error',
            summary: 'Error',
            detail: 'Ocurrió un error al intentar crear especialidad.',
            life: 5000,
          });
          location.state = null;
          break;
        default:
          break;
      }
    }
  };

  const leftToolbarTemplate = () => {
    return (
      <>
        <Link to='new'>
          <Button 
          id="link_new_speciality" 
          label="Crear Especialidad" 
          severity="success"
          icon="pi pi-plus"
          />
        </Link>
      </>
    );
  };

  useEffect(() => {
    console.log(backendUrl);
    handleShowToast();
    axios.get(`${backendUrl}/specialty`)
      .then((res) => {
        if (Array.isArray(res.data)) {
          setSpecialities(res.data);
        } else {
          navigate('/');
        }
      })
      .catch(() => {
        navigate('/');
      });
  }, [navigate]);

  return (
    <div className="specialities min-h-screen align-items-center align-content-center">
      <Toast ref={toast} />
      <div style={{ margin: "50px" }}>
      <div className="home text-left mt-5 mb-4 ml-4">
        <Link to="/">
          <Button
            className="px-4 w-1"
            icon="pi pi-home"
            size="large"
          />
        </Link>
      </div>
        <Toolbar className="mb-4" left={leftToolbarTemplate}></Toolbar>
        <DataTable
          className="p-datatable-striped"
          value={specialities}
          paginator
          rows={8}
          >
          <Column field="id" header="ID" />
          <Column field="name" header="Especialidad" />
        </DataTable>
      </div>
    </div>
  );
};

export default Specialities;