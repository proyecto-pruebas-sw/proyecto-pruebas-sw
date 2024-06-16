import { useState, useEffect, useRef } from "react";
import { Link, useParams, useNavigate, useLocation } from "react-router-dom";
import axios from "axios";
import { TabMenu } from "primereact/tabmenu";
import { Divider } from "primereact/divider";
import { Chip } from 'primereact/chip';
import { Button } from "primereact/button";
import { confirmDialog, ConfirmDialog } from 'primereact/confirmdialog'; // For confirmDialog method
import { Toast } from "primereact/toast";
import { backendUrl } from "../config/backend-url";
import { Card } from "primereact/card";
import emptyProfileImage from "../assets/empty_profile.png";

const MedicDetails = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const location = useLocation();
  const toast = useRef(null);

  const [medicData, setMedicData] = useState({
    name: '',
    lastname: '',
    rut: '',
    email: '',
    phone: '',
    birthdate: '',
    city: '',
    image_url: '',
    specialties: [],
    experiences: [],
    educations: [],
  });

  const [educations, setEducations] = useState([]);
  const [experiences, setExperiences] = useState([]);

  const [medicTab, setMedicTab] = useState(0);

  const toastDeleteError = () => {
    toast.current?.show({
      severity: 'error',
      summary: 'Error',
      detail: 'Ocurrió un error al intentar eliminar elemento.',
      life: 5000,
    });
  };

  const toastRemoved = () => {
    toast.current?.show({
      severity: 'info',
      summary: 'Eliminado',
      detail: 'Se eliminó antecedente.',
      life: 5000,
    });
  };

  const handleShowToast = () => {
    if (location.state !== null && location.state.response) {
      switch (location.state.response) {
        case 'modified':
          toast.current?.show({
            severity: 'success',
            summary: 'Cambios guardados',
            detail: 'Información personal de médico ha sido actualizada.',
            life: 5000,
          });
          location.state = null;
          break;
        case 'modifyError':
          toast.current?.show({
            severity: 'error',
            summary: 'Error',
            detail: 'Ocurrió un error al intentar editar información personal de médico.',
            life: 5000,
          });
          location.state = null;
          break;
        default:
          break;
      }
    }
  };

  const getEducation = () => {
    axios.get(`${backendUrl}/educations/${id}`)
      .then((res) => {
        setEducations(res.data);
      })
      .catch(() => {
        navigate('/', {
          state: {
            response: 'notFound',
          },
        });
      });
  };

  const getExperience = () => {
    axios.get(`${backendUrl}/experiences/${id}`)
      .then((res) => {
        setExperiences(res.data);
      })
      .catch(() => {
        navigate('/', {
          state: {
            response: 'notFound',
          },
        });
      });
  };

  useEffect(() => {
    handleShowToast();
    axios.get(`${backendUrl}/doctor/${id}`)
      .then((res) => {
        if (!res.data.Error) {
          setMedicData(res.data);
          getEducation();
          getExperience();
        }
        else {
          navigate('/', {
            state: {
              response: 'notFound',
            },
          });
        }
      })
      .catch(() => {
        navigate('/');
      });
  }, [id, navigate]);

  const handleRemoveMedic = () => {
    axios.delete(`${backendUrl}/doctor/${id}`)
      .then(() => {
        navigate('/', {
          state: {
            response: 'removed',
          },
        });
      })
      .catch(() => {
        toastDeleteError();
      })
  };

  const handleRemoveEducation = (id) => {
    axios.delete(`${backendUrl}/education/${id}`)
    .then(() => {
      toastRemoved();
    })
    .catch(() => {
      toastDeleteError();
    });
  };

  const handleRemoveExperience = (id) => {
    axios.delete(`${backendUrl}/experience/${id}`)
    .then(() => {
      toastRemoved();
    })
    .catch(() => {
      toastDeleteError();
    });
  };

  const confirmRemoval = () => {
    confirmDialog({
      message: 'Advertencia: esta operación no se puede deshacer.',
      header: 'Eliminar médico',
      icon: 'pi pi-exclamation-triangle',
      defaultFocus: 'reject',
      acceptLabel: 'Eliminar',
      rejectLabel: 'Cancelar',
      accept: () => {
        handleRemoveMedic();
      },
    });
  };

  const confirmEducationRemove = (id) => {
    confirmDialog({
      message: 'Advertencia: esta operación no se puede deshacer.',
      header: 'Eliminar antecedente académico',
      icon: 'pi pi-exclamation-triangle',
      defaultFocus: 'reject',
      acceptLabel: 'Eliminar',
      rejectLabel: 'Cancelar',
      accept: () => {
        handleRemoveEducation(id);
      },
    });
  };

  const confirmExperienceRemove = (id) => {
    confirmDialog({
      message: 'Advertencia: esta operación no se puede deshacer.',
      header: 'Eliminar antecedente laboral',
      icon: 'pi pi-exclamation-triangle',
      defaultFocus: 'reject',
      acceptLabel: 'Eliminar',
      rejectLabel: 'Cancelar',
      accept: () => {
        handleRemoveExperience(id);
      },
    });
  };

  const tabItems = [
    {
      label: 'Educación',
    },
    {
      label: 'Experiencia',
    },
  ];

  const handleMedicTab = (e) => {
    setMedicTab(e.index);
  };

  return (
    <div className="medicDetails min-h-screen align-items-center align-content-center" >
    <Card className="" style={{margin: "50px"}}>
      <ConfirmDialog />
      <div className="home text-left mt-5 ml-8">
        <Link to="/">
          <Button
            className="px-4 w-1"
            icon="pi pi-home"
            size="large"
          />
        </Link>
      </div>
      <Toast ref={toast} />
      <h2 className="">{medicData.name} {medicData.lastname}</h2>
      <div>
        <img 
          src={medicData.image_url !== null ? medicData.image_url : emptyProfileImage} 
          alt="Profile image" 
          width="250"
        />
      </div>
      <div className="">
        <span>
          Especialista en:
          {medicData.specialties.map((speciality) =>
            <Chip key={speciality.id} className="ml-2" label={speciality.name} />
          )}
        </span>
      </div>
      <div className="grid grid-nogutter mt-4">
        <div className="col-12 my-2">
          <span className="pi pi-map-marker mr-3" />{medicData.city}
        </div>
        <div className="col-12 my-2">
          <span className="pi pi-envelope mr-3" />{medicData.email}
        </div>
        <div className="col-12 my-2">
          <span className="pi pi-phone mr-3" />{medicData.phone}
        </div>
      </div>
      <div className="flex justify-content-center">
      <Link to='editPersonalInfo' style={{textDecoration: "None"}}>
        <Button id="link_edit_personal_info" label="Editar Información Personal" className="flex ml-8 my-5" severity="success" icon="pi pi-user-edit"/>
      </Link>
      <Link to='addEducationInfo' style={{textDecoration: "None"}}>
        <Button id="link_add_education_info" label="Crear Antecedente Académico" className="flex ml-8 my-5" severity="success" icon="pi pi-plus"/>
      </Link>
      <Link to='addExperienceInfo' style={{textDecoration: "None"}}>
        <Button id="link_add_education_info" label="Crear Antecedente Laboral" className="flex ml-8 my-5" severity="success" icon="pi pi-plus"/>
      </Link>
      </div>

      <Button
        id="remove_medic"
        label="Eliminar médico"
        severity="danger"
        icon="pi pi-times"
        onClick={confirmRemoval}
      />

      <TabMenu
        className="mt-3"
        model={tabItems}
        activeIndex={medicTab}
        onTabChange={handleMedicTab}
      />

      {medicTab === 0 && (
        <div>
          {educations.map((education) => (
            <>
              <h4>{education.degree}</h4>
              <span className="block">{education.institution}</span>
              <span className="block">{education.city}, {education.country}</span>
              <span className="block">Fecha de egreso: {education.end_date}</span>
              <Link to={`${education.id}/edit-education`}>
                <Button label="Editar" icon="pi pi-file-edit" severity="warning" className="m-2"/> 
              </Link>
              <Button label="Eliminar" icon="pi pi-times" severity="danger" className="m-2" onClick={() => confirmEducationRemove(education.id)} />
              <Divider />
            </>
          ))}
        </div>
      )}

      {medicTab === 1 && (
        <div>
          {experiences.map((experience) => (
            <>
              <h4>{experience.job_title}</h4>
              <span className="block">{experience.institution}</span>
              <span className="block">{experience.city}, {experience.country}</span>
              <span className="block">Fecha inicio: {experience.start_date}</span>
              <span className="block">Fecha término: {experience.end_date}</span>
              <Link to={`${experience.id}/edit-experience`}>
                <Button label="Editar" severity="warning" icon="pi pi-file-edit" className="m-2" /> 
              </Link>
              <Button label="Eliminar" icon="pi pi-times" severity="danger" className="m-2" onClick={() => confirmExperienceRemove(experience.id)} />
              <Divider />
            </>
          ))}
        </div>
      )}
    </Card>
    </div>
  );
};

export default MedicDetails;