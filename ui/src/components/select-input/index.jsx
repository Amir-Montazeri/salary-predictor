import Select from 'react-tailwindcss-select';

function SelectInput({ currentValue, options, onChange, placeholder }) {
  const handleChange = (value) => {
    onChange(value);
  };

  return (
    <div className="sm:w-[calc(50%-0.5rem)] w-full mb-1 mx-1">
      <Select
        primaryColor="teal"
        placeholder={placeholder}
        value={currentValue}
        onChange={handleChange}
        options={options}
      />
    </div>
  );
}

export default SelectInput;
