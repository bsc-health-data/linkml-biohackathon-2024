import * as React from 'react';
import { useState } from 'react';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FileChooser from './FileChooser';
import SelectionChooser from './SelectionChooser';
import ConverterChooser from './ConverterChooser';
import DownloadChooser from './DownloadChooser';
import AttachFileIcon from '@mui/icons-material/AttachFile';
import FilterAltIcon from '@mui/icons-material/FilterAlt';
import SyncAltIcon from '@mui/icons-material/SyncAlt';
import DownloadIcon from '@mui/icons-material/Download';

const steps = ['Upload File', 'Choose By', 'Convert Type', 'Download File'];

interface FilterParams {
  minAge?: number;
  maxAge?: number;
  sex?: string;
  disease?: string;
}

interface Filter {
  params: FilterParams
}

interface Converter {
  type: string;
}

export default function HorizontalLinearStepper() {
  const [activeStep, setActiveStep] = useState(0);
  const [activeNext, setActiveNext] = useState(false);
  const [skipped, setSkipped] = useState(new Set<number>());
  const [file, setFile] = useState<File | null>(null);
  const [filterSelected, setFilterSelected] = useState<Filter | null>({
    params: {
      minAge: 20,
      maxAge: 40,
      sex: '',
      disease: ''
  }});
  const [converterSelected, setConverterSelected] = useState<Converter | null>({ type: 'BBMRI CRC cohort' });

  const isStepSkipped = (step: number) => {
    return skipped.has(step);
  };

  const handleNext = () => {
    let newSkipped = skipped;
    if (isStepSkipped(activeStep)) {
      newSkipped = new Set(newSkipped.values());
      newSkipped.delete(activeStep);
    }

    if (activeStep === 0 || activeStep === 1 || activeStep === 2) {
      setActiveNext(true);
    }

    setActiveStep((prevActiveStep) => prevActiveStep + 1);
    setSkipped(newSkipped);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);

    if (activeStep === 1 || activeStep === 2) {
      setActiveNext(false);
    } else {
      setActiveNext(true);
    }
  };

  const handleFileChange = (file: File) => {
    setFile(file);
    setActiveNext(true);
  }

  const handleFilterChange = (filter: Filter) => {
    setFilterSelected(filterSelected);
  }

  const handleConverterChange = (converter: Converter) => {
    setConverterSelected(converter);
  }

  const handleReset = () => {
    setActiveStep(0);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Stepper activeStep={activeStep}>
        {steps.map((label, index) => {
          const stepProps: { completed?: boolean } = {};
          const labelProps: {
            optional?: React.ReactNode;
          } = {};
          if (isStepSkipped(index)) {
            stepProps.completed = false;
          }
          return (
            <Step key={label} {...stepProps}>
              <StepLabel {...labelProps} className="flex">
                { index === 0 &&
                <AttachFileIcon/>
                }
                { index === 1 && 
                  <FilterAltIcon />
                }
                { index === 2 && 
                  <SyncAltIcon />
                }
                { index === 3 && 
                  <DownloadIcon />
                }
                {label}
              </StepLabel>
            </Step>
          );
        })}
      </Stepper>
      {activeStep === steps.length ? (
        <React.Fragment>
          <Typography sx={{ mt: 2, mb: 1 }}>
            All steps completed - you&apos;re finished
          </Typography>
          <Box sx={{ display: 'flex', flexDirection: 'row', pt: 2 }}>
            <Box sx={{ flex: '1 1 auto' }} />
            <Button onClick={handleReset}>Reset</Button>
          </Box>
        </React.Fragment>
      ) : (
        <React.Fragment>
          <Typography component="div" sx={{ mt: 2, mb: 1 }}>
            {activeStep === 0 ?
              <FileChooser
                onFileChange={handleFileChange}
              /> : null}
            {activeStep === 1 ?
              <SelectionChooser
                onFilterChange={handleFilterChange}
                filter={filterSelected}
              /> : null
            }
            {activeStep === 2 ?
              <ConverterChooser
                onConverterChange={handleConverterChange}
                converter={converterSelected}
              /> : null}
            {activeStep === 3 ? 
            <div className="">
              <DownloadChooser 
                converterSelected={converterSelected}
                fileSelected={file}
                filterSelected={filterSelected}
                 />
            </div> : null}
          </Typography>
          <Box sx={{ display: 'flex', flexDirection: 'row', pt: 2 }}>
            <Button
              color="inherit"
              disabled={activeNext}
              onClick={handleBack}
              sx={{ mr: 1 }}
            >
              Back
            </Button>
            <Box sx={{ flex: '1 1 auto' }} />
            <Button onClick={handleNext}
            disabled={!activeNext}>
              {
                (activeStep === (steps.length - 1)) ? 'Finish' : 'Next'
              }
            </Button>
          </Box>
        </React.Fragment>
      )}
    </Box>
  );
}