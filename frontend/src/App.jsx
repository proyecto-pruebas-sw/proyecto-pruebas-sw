import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import './App.css'
import MedicDetails from './pages/medicDetails';
import ListMedics from './pages/listMedics';
import EditPersonalInfo from './pages/editPersonalInfo';

function App() {

  const router = createBrowserRouter(
    [
      {
        path: '/',
        element: < ListMedics/>,
      },
      {
        path: '/medics/search',
        element: <span>search</span>,
      },
      {
        path: '/medics/:id/editPersonalInfo',
        element: <EditPersonalInfo />
      },
      {
        path: '/medics/:id',
        element: <MedicDetails />
      }
    ]
  );

  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  )
}

export default App
