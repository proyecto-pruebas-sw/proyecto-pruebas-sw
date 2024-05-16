import { useState, useEffect } from "react";
import { Link, useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import { TabMenu } from "primereact/tabmenu";
import { Divider } from "primereact/divider";
import { Chip } from 'primereact/chip';
import { Button } from "primereact/button";

const MedicDetails = () => {
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

  const [medicTab, setUserTab] = useState(0);

  useEffect(() => {
    axios.get(`http://localhost:8000/doctor/${id}`)
    .then((res) => {
      if(!res.data.Error) {
        console.log(res);
        setMedicData(res.data);
      }
      else {
        navigate('/');  
      }
    })
    .catch(() => {
      navigate('/');
    });
  },[id, navigate]);

  const tabItems = [
    {
      label: 'Educación',
    },
    {
      label: 'Experiencia',
    },
  ];

  const handleMedicTab = (e) => {
    setUserTab(e.index);
  };

  return(
    <div className="medicDetails pt-5">
      <h2 className="text-left pl-8">{medicData.name} {medicData.lastname}</h2>
      <div className="text-left pl-8">
        <span>
          Especialista en:
          {medicData.specialties.map((speciality) => 
            <Chip className="ml-2" label={speciality.name} />
          )}
        </span>
      </div>
      <div className="grid grid-nogutter mt-4">
        <div className="text-left col-12 pl-8 my-2">
          <span className="pi pi-map-marker mr-3"/>{medicData.city}
        </div>
        <div className="text-left col-12 pl-8 my-2">
          <span className="pi pi-envelope mr-3"/>{medicData.email}
        </div>
        <div className="text-left col-12 pl-8 my-2">
          <span className="pi pi-phone mr-3"/>{medicData.phone}
        </div>
      </div>

      <Link to='editPersonalInfo'>
        <Button label="Editar información personal" className="flex ml-8 my-5"/>
      </Link>

      <TabMenu
        className="mt-3"
        model={tabItems}
        activeIndex={medicTab}
        onTabChange={handleMedicTab}
      />

      {medicTab === 0 && (
        <div>
          {medicData.educations.map((education) => (
            <>
              <h4>{education.degree}</h4>
              <span className="block">{education.institution}</span>
              <span className="block">{education.city}, {education.country}</span>
              <span className="block">Fecha de egreso: {education.end_date}</span>
              <Divider />
            </>
          ))}
        </div>
      )}

      {medicTab === 1 && (
        <div>
          {medicData.experiences.map((experience) => (
            <>
              <h4>{experience.job_title}</h4>
              <span className="block">{experience.institution}</span>
              <span className="block">{experience.city}, {experience.country}</span>
              <span className="block">Fecha inicio: {experience.start_date}</span>
              <span className="block">Fecha término: {experience.end_date}</span>
              <Divider />
            </>
          ))}
        </div>
      )}
    </div>
  );
};

export default MedicDetails;