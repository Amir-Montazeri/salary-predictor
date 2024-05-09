import { useState, useEffect } from 'react';
import axios from 'axios';
import { baseApiUrl } from '../../api';
import { timeInSecondsToStatic } from '../../features';

function Accuracy({ predictedSalary }) {
  const [accuracy, setAccuracy] = useState({
    last_from_last_update: null,
    accuracy_rate: null,
  });

  useEffect(() => {
    axios
      .get(`${baseApiUrl}/get_accuracy`)
      .then((res) => {
        const { data } = res;
        setAccuracy(data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="accuracy_container">
      {!predictedSalary && accuracy.accuracy_rate ? (
        <>
          <p>Accuracy: {accuracy.accuracy_rate}%</p>
          <p>
            Last Update: {timeInSecondsToStatic(accuracy.last_from_last_update)}
          </p>
        </>
      ) : predictedSalary ? (
        <p>Predicted Salary: ${predictedSalary}</p>
      ) : (
        <div>loading</div>
      )}
    </div>
  );
}

export default Accuracy;
