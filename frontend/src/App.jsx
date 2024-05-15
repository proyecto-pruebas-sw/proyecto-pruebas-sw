import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import './App.css'
import MedicDetails from './pages/medicDetails';
import ListMedics from './pages/listMedics';
import EditPersonalInfo from './pages/editPersonalInfo';
import NewSpeciality from './pages/newSpeciality';
import Specialities from './pages/specialities';
import NewMedic from './pages/newMedic';

function App() {

  const router = createBrowserRouter(
    [
      {
      path: '/medics/:id/editPersonalInfo',
      element: <EditPersonalInfo />,
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
        path: '/specialities/new',
        element: <NewSpeciality />,
      },
      {
        path: '/specialities',
        element: <Specialities />
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
