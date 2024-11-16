import React, { useState } from 'react';

const RiskInputView = () => {
  const [riskData, setRiskData] = useState({
    riskName: '',
    riskDescription: '',
    riskLevel: '',
    measures: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setRiskData({
      ...riskData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
  };

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">Risk Input View</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="riskName">
            Risk Name
          </label>
          <input
            type="text"
            name="riskName"
            id="riskName"
            value={riskData.riskName}
            onChange={handleChange}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="riskDescription">
            Risk Description
          </label>
          <textarea
            name="riskDescription"
            id="riskDescription"
            value={riskData.riskDescription}
            onChange={handleChange}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="riskLevel">
            Risk Level
          </label>
          <input
            type="text"
            name="riskLevel"
            id="riskLevel"
            value={riskData.riskLevel}
            onChange={handleChange}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="measures">
            Measures
          </label>
          <input
            type="text"
            name="measures"
            id="measures"
            value={riskData.measures}
            onChange={handleChange}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div className="flex items-center justify-between">
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  );
};

export default RiskInputView;
