import { useEffect, useState } from 'react';
import axios from 'axios';
import { SelectInput } from '..';
import { baseApiUrl } from '../../api';

function Form({ onChangeSalary }) {
  const [uniqueFeatures, setUniqueFeatures] = useState({}),
    [currentValues, setCurrentValues] = useState({}),
    [errors, setErrors] = useState(null);

  useEffect(() => {
    axios
      .get(`${baseApiUrl}/get_unique_features`)
      .then((res) => {
        let renderedUniqueFeatures = {};
        Object.keys(res.data).map((uniqueFeature) => {
          let renderedUniqueFeatureValues = [];
          res.data[uniqueFeature].map(
            (value) =>
              (renderedUniqueFeatureValues = [
                ...renderedUniqueFeatureValues,
                { value, label: value.toString() },
              ])
          );
          renderedUniqueFeatures = {
            ...renderedUniqueFeatures,
            [uniqueFeature]: renderedUniqueFeatureValues,
          };
        });
        setUniqueFeatures(renderedUniqueFeatures);
      })
      .catch((err) => setErrors(err.message));
  }, []);

  const submitHandler = (e) => {
    e.preventDefault();
    onChangeSalary(null);
    if (
      Object.keys(currentValues).length == Object.keys(uniqueFeatures).length
    ) {
      setErrors(null);
      let renderedValues = {};
      Object.keys(currentValues).map((currentFeature) => {
        renderedValues = {
          ...renderedValues,
          [currentFeature]: currentValues[currentFeature].value,
        };
      });

      axios
        .get(`${baseApiUrl}/predict`, {
          params: renderedValues,
        })
        .then((res) => onChangeSalary(res.data))
        .catch((err) => console.log('oops - ', err.response.data.detail));
    } else {
      setErrors(['Some required fields has not been filled!']);
    }
  };

  const renderedSelectInput = Object.keys(uniqueFeatures).map(
    (uniqueFeature) => (
      <SelectInput
        key={uniqueFeature}
        options={uniqueFeatures[uniqueFeature]}
        placeholder={uniqueFeature + '*'}
        currentValue={
          currentValues[uniqueFeature] || uniqueFeatures[uniqueFeature].value
        }
        onChange={(val) =>
          setCurrentValues((prevState) => ({
            ...prevState,
            [uniqueFeature]: val,
          }))
        }
      />
    )
  );

  return uniqueFeatures ? (
    <div className="predictor_form_container">
      <form onSubmit={submitHandler} className="predictor_form">
        <div className="flex flex-wrap justify-center">
          {renderedSelectInput}
        </div>
        <div className="w-full flex flex-col justify-center items-center my-3">
          <button
            type="submit"
            className="block bg-[#024950] w-3/4 py-3 text-gray-300 rounded-[5px]"
          >
            Predict
          </button>
          <div className="mx-4">
            {errors ? (
              errors.map((error) => (
                <p key={error} className="text-red-900 text-sm">
                  {error}
                </p>
              ))
            ) : (
              <p className="text-red-900 text-sm">‌</p>
            )}
          </div>
        </div>
      </form>
    </div>
  ) : (
    <div>loading...</div>
  );
}

export default Form;
