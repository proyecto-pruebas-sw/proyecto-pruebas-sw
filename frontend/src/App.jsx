import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import Index from './pages';
import './App.css'

function App() {

  const router = createBrowserRouter(
    [
      {
        path: '/',
        element: <Index />
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
