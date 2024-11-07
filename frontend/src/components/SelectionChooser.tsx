
import { useState, useEffect } from 'react';
import Slider from '@mui/material/Slider';
import MenuItem from '@mui/material/MenuItem';
import Box from '@mui/material/Box';
import FormControl from '@mui/material/FormControl';
import Grid from '@mui/material/Grid2';
import OutlinedInput from '@mui/material/OutlinedInput';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import '../styles/styles.css';
import useFilter from './hooks/useFilter'; // Import the custom hook

interface FilterParams {
  minAge?: number;
  maxAge?: number;
  sex?: object;
  disease?: string[];
}

interface FilterAppliedParams {
  minAge?: number;
  maxAge?: number;
  sex?: string;
  disease?: string[];
}

interface Filter {
  type: string;
  params: FilterParams
}

interface FilterApplied {
  params: FilterAppliedParams
}

interface SelectionChooserProps {
  onFilterChange: (filterData: Partial<FilterParams>) => void;
  loadingInput: boolean;
  filterData: FilterParams
}

const AgeMarks = [
  {
    value: 0,
    label: '0 years',
  },
  {
    value: 20,
    label: '20 years',
  },
  {
    value: 40,
    label: '40 years',
  },
  {
    value: 60,
    label: '60 years',
  },
  {
    value: 80,
    label: '80 years',
  },
];

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 350,
    },
  },
};

export default function SelectionChooser({ onFilterChange, filterData, filterApplied, loadingInput }: SelectionChooserProps) {
  const [age, setAge] = useState<number[]>(filterData.params.minAge && filterData.params.maxAge ? [filterData.params.minAge, filterData.params.maxAge] : [20, 40]);
  const [sex, setSex] = useState<string[]>(filterData.params.sex || []);
  const [disease, setDisease] = useState<string[]>(filterData.params.disease || []);

  const filters = [
    { index: 0, label: 'Age', minValue: 0, maxValue: 100 },
    { index: 1, label: 'Sex', sex: []},
    { index: 2, label: 'Disease', disease: []},
  ];

  useEffect(() => {
    if (filterData.params.minAge !== undefined && filterData.params.maxAge !== undefined) {
      setAge([filterData.params.minAge, filterData.params.maxAge]);
    }
    if (filterData.params.sex) {
      setSex(filterData.params.sex);
    }
    if (filterData.params.disease) {
      setDisease(filterData.params.disease);
    }
  },  [JSON.stringify(filterData)]);


  // Handlers for sex change
  const handleAgeChange = (event: Event, value: number | number[]) => {
    const updatedAge = value as number[];
    setAge(updatedAge);
    onFilterChange({ minAge: updatedAge[0], maxAge: updatedAge[1] });
  };

  const handleSexChange = (event: SelectChangeEvent) => {
    const updatedSex = [event.target.value];
    setSex(updatedSex);
    onFilterChange({ sex: updatedSex });
  };
  
  function handleDiseaseChange(event: SelectChangeEvent) {
    const updatedDisease = [event.target.value];
    setDisease(updatedDisease);
    onFilterChange({ disease: updatedDisease });
  }

  return(
    <div className="file-chooser">
      <div className="stepper-title ">
        Choose by cohort selection
      </div>
      <div className="stepper-description">
        Choose the file you want to convert
      </div>
      { loadingInput ? (
        <div>Loading...</div>
      ): (
        <div className="stepper-body-block">
          <div className="stepper-inner-row">
            <Grid container spacing={2}>
            { filters.map((f) => {
              if (f.label === 'Age' && filterData.params.minAge && filterData.params.maxAge) {
                return (
                  <Grid size={12} key="age">
                    <div className="stepper-inner-row w-100 p-b-50">
                      <div className="stepper-inner-row-label">Age:</div>
                        <Slider
                          getAriaLabel={() => 'Ages'}
                          value={
                            filterApplied.params.minAge !== undefined && filterApplied.params.maxAge !== undefined
                              ? [filterApplied.params.minAge, filterApplied.params.maxAge]
                              : [20, 40]
                          }
                          onChange={handleAgeChange}
                          valueLabelDisplay="auto"
                          step={10}
                          valueLabelFormat={(value) => `${value} years`}
                          marks={AgeMarks}
                        />
                    </div>
                    <div className="stepper-separator"></div>
                  </Grid>
                );
              }
              if (f.label === 'Sex' && filterData.params.sex && filterData.params.sex.length > 0) {
                return (
                  <Grid size={6} key="sex">
                    <div className="stepper-inner-row p-b-50">
                      <div className="stepper-inner-row-label">Sex:</div>
                      <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        value={filterApplied.params.sex || ''}                        
                        label="Sex"
                        onChange={handleSexChange}
                      >
                        {filterData.params.sex.map((filter) => (
                          <MenuItem key={filter.type} value={filter.type}>
                            {filter.type}
                          </MenuItem>
                        ))}
                      </Select>
                      <hr />
                    </div>
                    
                  </Grid>
                );
              }
              if (f.label === 'Disease' && filterData.params.disease && filterData.params.disease.length > 0) {
                return (
                  <Grid size={6} key="disease">
                    <div className="stepper-inner-row">
                      <div className="stepper-inner-row-label">Disease:</div>
                      <Box sx={{ m: 1, width: 300 }}>                        <Select
                          labelId="demo-simple-select-label"
                          id="demo-simple-select-disease"
                          multiple
                          label="Disease"
                          value={filterApplied.params.disease || []}                        
                          onChange={handleDiseaseChange}
                          input={<OutlinedInput label="Disease" />}
                          MenuProps={MenuProps}
                          autoWidth
                        >
                          {filterData.params.disease.map((filter) => (
                            <MenuItem key={filter} value={filter}>
                              {filter}
                            </MenuItem>
                          ))}
                        </Select>
                      </Box>
                    </div>
                  </Grid>
                );
              }
            })
            }
            </Grid>
          </div>
        </div>
      )}
    </div>
  );
}

