import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";

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
  })

  useEffect(() => {
    axios.get(`localhost:8000/doctor/${id}`)
    .then((res) => {
      console.log(res.data);
    })
    .catch(() => {
      navigate('/');
    });
  },[]);

  return(
    <div className="medicDetails">
      <h1>Detalles</h1>
    </div>
  );
};

export default MedicDetails;