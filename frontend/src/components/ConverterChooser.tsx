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
  title: string;
  subtitle: string;
}

export default function ConverterChooser({ onConverterChange, title, subtitle }: ConverterChooserProps) {
  const [converter, setConverter] = useState<Converter | null>({ type: 'BBMRI CRC cohort' });

  const handleConverterChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const newConverter = { type: event.target.value };
    setConverter(newConverter);
    onConverterChange(newConverter);
  };

  return (
    <div className="converter-chooser">
      <div className="stepper-title ">
        {title}
      </div>
      <div className="stepper-description">
        {subtitle}
      </div>
      <div className="stepper-body">
      <FormControl>
        <RadioGroup
          aria-labelledby="demo-radio-buttons-group-label"
          defaultValue={converter?.type }
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