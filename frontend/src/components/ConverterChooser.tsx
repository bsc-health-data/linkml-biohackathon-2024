import { useState } from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import '../styles/styles.css';

interface Converter {
  type: string;
}

interface ConverterChooserProps {
  onConverterChange: (converter: Converter) => void;
  converter: Converter;
}

export default function ConverterChooser({ onConverterChange }: ConverterChooserProps) {
  const [converterSelected, setConverterSelected] = useState<Converter | null>({ type: 'BBMRI CRC cohort' });

  const handleConverterChange = () => {
    setConverterSelected(converterSelected);
    if (converterSelected) {
      onConverterChange(converterSelected);
    }
  };

  return (
    <div className="converter-chooser">
      <div className="stepper-title ">
        Choose a converter
      </div>
      <div className="stepper-description">
        Choose the converter you want to use
      </div>
      <div className="stepper-body">
      <FormControl>
        <RadioGroup
          aria-labelledby="demo-radio-buttons-group-label"
          defaultValue={converterSelected?.type }
          onChange={handleConverterChange}
          name="radio-buttons-group"
        >
          <FormControlLabel value="BBMRI CRC cohort" control={<Radio />} label="BBMRI CRC cohort" />
          <FormControlLabel value="B1MG" control={<Radio />} label="B1MG" />
          <FormControlLabel value="OMOP" control={<Radio />} label="OMOP" />
          <FormControlLabel value="Phenopackets" control={<Radio />} label="Phenopackets" />
        </RadioGroup>
      </FormControl>
      </div>
    </div>
  );
}