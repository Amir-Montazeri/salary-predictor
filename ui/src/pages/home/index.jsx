import { useState } from 'react';
import { Accuracy, PredictorForm } from '../../components';

function Home() {
  const [predictedSalary, setPredictedSalary] = useState(null);

  return (
    <div className="home_container">
      <Accuracy predictedSalary={predictedSalary} />
      <PredictorForm onChangeSalary={setPredictedSalary} />
    </div>
  );
}

export default Home;
