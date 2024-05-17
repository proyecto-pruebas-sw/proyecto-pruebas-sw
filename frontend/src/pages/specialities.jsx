import { useEffect, useState } from "react";
import axios from "axios";
import { Button } from "primereact/button";
import { Column } from "primereact/column";
import { DataTable } from "primereact/datatable";
import { Link, useNavigate } from "react-router-dom";
import { backendUrl } from "../config/backend-url";

const Specialities = () => {
  const navigate = useNavigate();

  const [specialities, setSpecialities] = useState([]);

  useEffect(() => {
    axios.get(`${backendUrl}/specialty`)
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

  return (
    <div className="specialities">
      <Link to='new'>
        <Button id="link_new_speciality" label="Nueva especialidad" />
      </Link>
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
  );
};

export default Specialities;