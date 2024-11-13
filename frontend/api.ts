import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const getRisks = async () => {
  try {
    const response = await axios.get(`${API_URL}/risks/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching risks:', error);
    throw error;
  }
};

export const createRisk = async (riskData) => {
  try {
    const response = await axios.post(`${API_URL}/risks/`, riskData);
    return response.data;
  } catch (error) {
    console.error('Error creating risk:', error);
    throw error;
  }
};

export const updateRisk = async (riskId, riskData) => {
  try {
    const response = await axios.put(`${API_URL}/risks/${riskId}`, riskData);
    return response.data;
  } catch (error) {
    console.error('Error updating risk:', error);
    throw error;
  }
};

export const deleteRisk = async (riskId) => {
  try {
    const response = await axios.delete(`${API_URL}/risks/${riskId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting risk:', error);
    throw error;
  }
};

export const getMeasures = async () => {
  try {
    const response = await axios.get(`${API_URL}/measures/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching measures:', error);
    throw error;
  }
};

export const createMeasure = async (measureData) => {
  try {
    const response = await axios.post(`${API_URL}/measures/`, measureData);
    return response.data;
  } catch (error) {
    console.error('Error creating measure:', error);
    throw error;
  }
};

export const updateMeasure = async (measureId, measureData) => {
  try {
    const response = await axios.put(`${API_URL}/measures/${measureId}`, measureData);
    return response.data;
  } catch (error) {
    console.error('Error updating measure:', error);
    throw error;
  }
};

export const deleteMeasure = async (measureId) => {
  try {
    const response = await axios.delete(`${API_URL}/measures/${measureId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting measure:', error);
    throw error;
  }
};

export const getRubrix = async () => {
  try {
    const response = await axios.get(`${API_URL}/rubrix/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching rubrix:', error);
    throw error;
  }
};
