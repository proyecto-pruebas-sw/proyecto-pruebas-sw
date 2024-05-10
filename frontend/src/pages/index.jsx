import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { InputText } from 'primereact/inputtext';
import { Button } from 'primereact/button';

const Index = () => {
  const navigate = useNavigate();

  const [input, setInput] = useState('');

  const handleSearch = () => {
    navigate('/search',{
      state: {
        name: input,
      },
    });
  };

  return(
    <div className="Index h-screen align-items-center align-content-center">
      <InputText
        className="w-7 my-auto"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter")
            handleSearch();
        }}
        placeholder="Buscar médico"
      />
      <Button label="Buscar" onClick={handleSearch} className="w-1 ml-2"/>
    </div>
  );
};

export default Index;