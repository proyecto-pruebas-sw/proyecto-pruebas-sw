import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import './App.css'
import MedicDetails from './pages/medicDetails';
import ListMedics from './pages/listMedics';
import EditPersonalInfo from './pages/editPersonalInfo';
import NewSpecialty from './pages/newSpecialty';
import Specialties from './pages/specialties';
import NewMedic from './pages/newMedic';
import AddEducationInfo from './pages/addEducationInfo';
import AddExperienceInfo from './pages/addExperienceInfo';
import EditEducationInfo from './pages/editEducationInfo';
import EditExperienceInfo from './pages/editExperienceInfo';

function App() {

  const router = createBrowserRouter(
    [
      {
        path: '/medics/:id/editPersonalInfo',
        element: <EditPersonalInfo />,
      },
      {
        path: '/medics/:doctorId/:educationId/edit-education',
        element: <EditEducationInfo />,
      },
      {
        path: '/medics/:doctorId/:experienceId/edit-experience',
        element: <EditExperienceInfo />,
      },
      {
        path: '/medics/:id/addEducationInfo',
        element: <AddEducationInfo />,
      },
      {
        path: '/medics/:id/addExperienceInfo',
        element: <AddExperienceInfo />,
      },
      {
        path: '/medics/:id',
        element: <MedicDetails />,
      },
      {
        path: '/medics/new',
        element: <NewMedic />,
      },
      {
        path: '/specialties/new',
        element: <NewSpecialty />,
      },
      {
        path: '/specialties',
        element: <Specialties />
      },
      {
        path: '/',
        element: <ListMedics />,
      },
    ]
  );

  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  )
}

export default App
