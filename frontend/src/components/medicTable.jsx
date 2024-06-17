import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';


const MedicTable = ({ medics }) => {

  const [selectedMedic, setSelectedMedic] = useState(null);
  const navigate = useNavigate();

  const handleRowClick = (e) => {
    navigate(`/medics/${e.value.id}`);
  }

  const ConstructName = (rowData) => {
    return (
      <span id={`r${rowData.id}_name`}>
        {rowData.name} {rowData.lastname}
      </span>
    );
  };

  const ConstructCity = (rowData) => {
    return (
      <span id={`r${rowData.id}_city`}>
        {rowData.city}
      </span>
    );
  };

  const ConstructSpecialty = (rowData) => {
    return (
      <span id={`r${rowData.id}_specialties`}>
        {
          rowData.specialties.map((specialty, index) =>
            <div key={index} id={`r${rowData.id}_specialty_${index}`}>
              {specialty.name}
            </div>
          )
        }
      </span>
    );
  };

  const ConstructEmail = (rowData) => {
    return (
      <span id={`r${rowData.id}_email`}>
        {rowData.email}
      </span>
    );
  };

  const ConstructPhone = (rowData) => {
    return (
      <span id={`r${rowData.id}_phone`}>
        {rowData.phone}
      </span>
    );
  };

  return (
    <DataTable value={medics} paginator rows={8} className="p-datatable-striped" selectionMode="single" selection={selectedMedic} onSelectionChange={handleRowClick}>
      <Column header="Nombre" body={ConstructName} />
      <Column header="Ciudad" body={ConstructCity} />
      <Column header="Especialidades" body={ConstructSpecialty} />
      <Column header="Email" body={ConstructEmail} />
      <Column header="Teléfono" body={ConstructPhone} />
    </DataTable>
  );
}

export default MedicTable