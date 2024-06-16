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

  const [medicTab, setUserTab] = useState(0);

  const toastDeleteError = () => {
    toast.current?.show({
      severity: 'error',
      summary: 'Error',
      detail: 'Ocurrió un error al intentar eliminar médico.',
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

  useEffect(() => {
    handleShowToast();
    axios.get(`${backendUrl}/doctor/${id}`)
      .then((res) => {
        if (!res.data.Error) {
          console.log(res);
          setMedicData(res.data);
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
      navigate('/',{
        state: {
          response: 'removed',
        },
      });
    })
    .catch(() => {
      toastDeleteError();
    })
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

  return (
    <div className="medicDetails">
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
      <h2 className="text-left pl-8">{medicData.name} {medicData.lastname}</h2>
      <div class="grid grid-nogutter pl-8 my-2">
        <img 
          src={medicData.image_url !== '' ? medicData.image_url : '../../public/empty_profile.png'} 
          alt="Profile image" 
          width="250"
        />
      </div>
      <div className="text-left pl-8">
        <span>
          Especialista en:
          {medicData.specialties.map((speciality) =>
            <Chip key={speciality.id} className="ml-2" label={speciality.name} />
          )}
        </span>
      </div>
      <div className="grid grid-nogutter mt-4">
        <div className="text-left col-12 pl-8 my-2">
          <span className="pi pi-map-marker mr-3" />{medicData.city}
        </div>
        <div className="text-left col-12 pl-8 my-2">
          <span className="pi pi-envelope mr-3" />{medicData.email}
        </div>
        <div className="text-left col-12 pl-8 my-2">
          <span className="pi pi-phone mr-3" />{medicData.phone}
        </div>
      </div>

      <Link to='editPersonalInfo'>
        <Button id="link_edit_personal_info" label="Editar información personal" className="flex ml-8 my-5" />
      </Link>

      <Button
        id="remove_medic"
        label="Eliminar médico"
        severity="danger"
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