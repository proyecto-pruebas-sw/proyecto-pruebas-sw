import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import Index from './pages';
import './App.css'
import MedicDetails from './pages/medicDetails';

function App() {

  const router = createBrowserRouter(
    [
      {
        path: '/',
        element: <Index />,
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
