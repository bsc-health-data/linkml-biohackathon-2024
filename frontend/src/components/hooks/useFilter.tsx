import { useState, useEffect } from 'react';

// Define the types for the filter parameters
interface FilterParams {
  minAge?: number;
  maxAge?: number;
  sex?: string[];
  disease?: string[];
}

// Define the Filter object type
interface Filter {
  type: string;
  params: FilterParams;
}

// The custom hook that manages the filter state
const useFilter = (initialParams: FilterParams = {}) => {
  const [filter, setFilter] = useState<Filter>({
    type: 'checkbox',
    params: initialParams,
  });

  const setAge = (age: number[]) => {
    setFilter((prevFilter) => ({
      ...prevFilter,
      params: {
        ...prevFilter.params,
        minAge: age[0],
        maxAge: age[1],
      },
    }));
  };

  const setSex = (sex: string[]) => {
    setFilter((prevFilter) => ({
      ...prevFilter,
      params: {
        ...prevFilter.params,
        sex,
      },
    }));
  };

  const setDisease = (disease: string[]) => {
    setFilter((prevFilter) => ({
      ...prevFilter,
      params: {
        ...prevFilter.params,
        disease,
      },
    }));
  };

  return { filter, setAge, setSex, setDisease };
};

export default useFilter;
