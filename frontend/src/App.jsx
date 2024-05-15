import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import './App.css'
import MedicDetails from './pages/medicDetails';
import ListMedics from './pages/listMedics';

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
