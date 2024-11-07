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

const steps = ['Upload File', 'Filters', 'Output File Format', 'Download File'];

interface FilterParams {
  minAge?: number;
  maxAge?: number;
  sex?: object;
  disease?: object;
}

interface FilterAppliedParams {
  minAge?: number;
  maxAge?: number;
  sex?: string;
  disease?: string[];
}

interface Filter {
  params: FilterParams
}

interface FilterApplied {
  params: FilterAppliedParams
}

interface Converter {
  type: string;
}

export default function HorizontalLinearStepper() {
  const [activeStep, setActiveStep] = useState(0);
  const [activeNext, setActiveNext] = useState(false);
  const [skipped, setSkipped] = useState(new Set<number>());
  const [file, setFile] = useState<File | null>(null);
  const [loadingInput, setLoadingInput] = useState(false);
  const [inputData, setInputData] = useState<any>(null);
  const [converterSelected, setConverterSelected] = useState<Converter | null>({ type: 'BBMRI CRC cohort' });
  const [converterOutput, setConverterOutput] = useState<Converter | null>({ type: 'BBMRI CRC cohort' });
  const [filterSelected, setFilterSelected] = useState<Filter | null>({
    params: {
      minAge: 20,
      maxAge: 40,
      sex:{},
      disease: {}
  }});
  const [filterApplied, setFilterApplied] = useState<FilterApplied | null>({
    params: {
      minAge: 0,
      maxAge: 0,
      sex: "",
      disease: []
    }
  });

  const isStepSkipped = (step: number) => {
    return skipped.has(step);
  };

  const handleNext = () => {
    let newSkipped = skipped;
    if (isStepSkipped(activeStep)) {
      newSkipped = new Set(newSkipped.values());
      newSkipped.delete(activeStep);
    }

    if (activeStep === 0 || activeStep === 1) {
      setActiveNext(true);
    }

    setActiveStep((prevActiveStep) => prevActiveStep + 1);
    setSkipped(newSkipped);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleFileChange = (newFile: File | null) => {
    setFile(newFile);
    setActiveNext(true);
  }

  const handleConverterChange = (converter: Converter) => {
    setConverterSelected(converter);
  }

  const handleConverterOutputChange = (converter: Converter) => {
    setConverterOutput(converter);
  }

  const handleFilterChange = (updatedFilterData) => {
    setFilterApplied((prevData) => ({
      ...prevData,
      params: { ...prevData.params, ...updatedFilterData }
    }));
  };

  const handleLoadingInput = () => {
    setLoadingInput(true);
    setActiveStep((prevActiveStep) => prevActiveStep + 1);

    const inputFile = file?.name;
    const inputFormat = converterSelected?.type;
    const inputPath = "C:/biohack/linkml-biohackathon-2024/extractCohort/data/";

    fetch("http://127.0.0.1:5000/cohortRetrieval?model=" + inputFormat + "&path=" + inputPath + inputFile)
      .then(response => response.json())
      .then(data => {
        const ageMin = data.age[0];
        const ageMax = data.age[1];
        const sex = data.sex;
        let sexObj = [];
        if(sex.MALE) {
          const temp = {
            type: 'Male'
          }
          sexObj.push(temp);
        }
        if(sex.FEMALE) {
          const temp = {
            type: 'Female'
          }
        }
        let diseases = [];
        if(data.diseases) {
          const diseaseArray = Object.entries(data.diseases).map(([key, value]) => {
            return `${key} - ${value}`;
          });
          diseases = diseaseArray;
        }

        const filter: Filter = {
          params: {
            minAge: ageMin,
            maxAge: ageMax,
            sex: sexObj,
            disease: diseases
        }};

        const defaultDisease =  diseases.length > 0 ? [diseases[0]] : [];

        // default filter values
        const filterApplied: FilterApplied = {
          params: {
            minAge: parseInt(ageMin),
            maxAge: parseInt(ageMax),
            sex: sexObj[0].type,
            disease: defaultDisease
          }
        };

        setFilterSelected(filter);
        setFilterApplied(filterApplied);
        setLoadingInput(false);
    })
    .catch(error => console.error("Error:", error));
}

const handleReset = () => {
  setActiveStep(0);
};

return (
  <Box sx={{ width: '100%' }}>
    <div className="stepper-wrapper">
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
          {activeStep === 0 ? (
            <>
              <FileChooser
                onFileChange={handleFileChange}
              />
              {file ?
                <div className="stepper-separator"></div>
                : null
              }
              {file ?
              <ConverterChooser
                onConverterChange={handleConverterChange}
                converter={converterSelected}
                title="Choose a converter"
                subtitle='Choose the converter you want to use'
              /> : null }
              </>
            ) : null}
            {activeStep === 1 ?
              <SelectionChooser
                onFilterChange={handleFilterChange}
                filterData={filterSelected}
                filterApplied={filterApplied}
                loadingInput={loadingInput}
              /> : null
            }
            {activeStep === 2 ? 
            <div className="">
              <ConverterChooser
                onConverterChange={handleConverterOutputChange}
                converter={converterOutput}
                title="Choose a converter for OutputFile"
                subtitle='Choose the converter you want to use'
              /> 
            </div> : null}
            {activeStep === 3? 
            <div className="">
              <DownloadChooser 
                converterSelected={converterSelected}
                fileSelected={file}
                filterSelected={filterApplied}
                converterOutput={converterOutput}
                />
            </div> : null}
          </Typography>
          <Box sx={{ display: 'flex', flexDirection: 'row', pt: 2 }}>
            <Button
              color="inherit"
              disabled={activeStep === 0}
              onClick={handleBack}
              sx={{ mr: 1 }}
            >
              Back
            </Button>
            <Box sx={{ flex: '1 1 auto' }} />
            { activeStep ===0 && !inputData  ? (
              <Button onClick={handleLoadingInput}
              disabled={!activeNext}>
                {
                  (activeStep === (steps.length - 1)) ? 'Finish' : 'Next'
                }
              </Button>
            ) : (
            <Button onClick={handleNext}
              disabled={!activeNext}>
                {
                  (activeStep === (steps.length - 1)) ? '' : 'Next'
                }
              </Button>
            )}
          </Box>
        </React.Fragment>
      )}
    </div>
    </Box>
  );
}