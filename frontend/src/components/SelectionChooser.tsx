
import { useState } from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import '../styles/styles.css';

interface FilterParams {
  minVAlue?: number;
  maxValue?: number;
  sex?: string;
  disease?: string;
}

interface Filter {
  type: string;
  params: FilterParams
}

interface SelectionChooserProps {
  onFilterChange: (filter: Filter) => void;
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

export default function SelectionChooser({ onFilterChange }: SelectionChooserProps) {
  const [filter, setFilter] = useState<Filter | null>(null);
  const [sex, setSex] = useState('');
  const [age, setAge] = useState([20, 40]);
  const [disease, setDisease] = useState('');
  const filters = [
    { index: 0, label: 'Age', minValue: 0, maxValue: 100 },
    { index: 1, label: 'Sex', sex: ''},
    { index: 2, label: 'Disease', disease: ''},
  ]

  const handleFilterChange = () => {
    console.log("we are moving to next step")
    const filter: Filter = {
      type: 'checkbox',
      params: {
        minVAlue: age[0],
        maxValue: age[1],
        sex: sex,
        disease: disease
      }
    }
    onFilterChange(filter);
  };

  function handleAgeChange(event: Event, value: number | number[]) {
    console.log("age has change: ", value)
    setAge(value as number[]);
    handleFilterChange();
  }

  function valuetext(value: number) {
    return `${value} years`;
  }

  function handleSexChange(event: SelectChangeEvent) {
    setSex(event.target.value as string);
    handleFilterChange();
  }

  return(
    <div className="file-chooser">
      <div className="stepper-title ">
        Choose by cohort selection
      </div>
      <div className="stepper-description">
        Choose the file you want to convert
      </div>
      <div className="stepper-body-block">
        {filters.map((f) => (
          <div className="stepper-row" key={f.index}>
            {f.label === 'Age' ? (
              <div className="stepper-inner-row">
                <div className="stepper-inner-row-label">Age</div>
                <Slider
                  getAriaLabel={() => 'Sex range'}
                  defaultValue={20}
                  getAriaValueText={valuetext}
                  step={10}
                  value={age}
                  valueLabelDisplay="auto"
                  onChange={handleAgeChange}
                  marks={AgeMarks}
                />
              </div>
            ) : f.label === 'Sex' ? (
              <div className="stepper-inner-row">
                  <div className="stepper-inner-row-label">Sex</div>
                  <Box sx={{ minWidth: 200 }}>
                    <FormControl fullWidth>
                    <InputLabel id="demo-simple-select-standard-label">Sex</InputLabel>
                      <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        value={sex}
                        label="Sex"
                        onChange={handleSexChange}
                      >
                        <MenuItem value="male">Male</MenuItem>
                        <MenuItem value="female">Female</MenuItem>
                      </Select>
                    </FormControl>
                  </Box>
              </div>
            ) : f.label === 'Disease' ? (
              <div className="stepper-inner-row">
                <div className="stepper-inner-row-label">Disease</div>

              </div>
            ) : null}
          </div>
        ))}
      </div>
    </div>
  );
}

