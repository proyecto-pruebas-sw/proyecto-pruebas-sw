import {DataTable} from 'primereact/datatable';
import {Column} from 'primereact/column';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';


const MedicTable = ({medics}) => {

    const [selectedMedic, setSelectedMedic] = useState(null);
    const navigate = useNavigate();

    const handleRowClick = (e) => {
        navigate(`/medics/${e.value.id}`);
    }

    const ConstructName = (rowData) => {
        return (
            <span>
                {rowData.name} {rowData.lastname}
            </span>
        );
    };

    const ConstructSpecialty = (rowData) => {
        return (
            <span>
                {
                rowData.specialties.map((specialty, index) =>
                    <div key={index}>
                        {specialty.name}
                    </div> 
                )
                }
            </span>
        );
    }

    return (
        <DataTable value={medics} paginator rows={8} className="p-datatable-striped" selectionMode="single" selection={selectedMedic} onSelectionChange={handleRowClick}>
            <Column header="Nombre" body={ConstructName}/>
            <Column field="city" header="Ciudad" />
            <Column header="Especialidades" body={ConstructSpecialty}/>
            <Column field="email" header="Email"/>
            <Column field="phone" header="Teléfono"/>
        </DataTable>
    );
}

export default MedicTable