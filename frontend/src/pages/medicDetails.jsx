import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import { TabMenu } from "primereact/tabmenu";
import { Divider } from "primereact/divider";

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
    axios.get(`http://4.203.106.91:8000/doctor/${id}`)
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
    <div className="medicDetails">
      <h2>{medicData.name} {medicData.lastname}</h2>
      <div>
        <span>
          Especialista en:
          {medicData.specialties.map((speciality) => 
            <>{speciality.name}</>
          )}
        </span>
      </div>
      <div className="grid grid-nogutter">
        <div className="col-6">
          {medicData.city}
        </div>
        <div className="col-6">
          {medicData.email}
        </div>
        <div className="col-6">
          {medicData.phone}
        </div>
        <div className="col-6">
          {medicData.birthdate}
        </div>
      </div>

      <TabMenu
        model={tabItems}
        activeIndex={medicTab}
        onTabChange={handleMedicTab}
      />

      {medicTab === 0 && (
        <div>
          {medicData.educations.map((education) => (
            <>
              <h4>{education.degree}</h4>
              <span>{education.institution}</span>
              <span>{education.city}, {education.country}</span>
              <span>{education.end_date}</span>
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
              <span>{experience.institution}</span>
              <span>{experience.city}, {experience.country}</span>
              <span>{experience.start_date}</span>
              <span>{experience.end_date}</span>
              <Divider />
            </>
          ))}
        </div>
      )}
    </div>
  );
};

export default MedicDetails;