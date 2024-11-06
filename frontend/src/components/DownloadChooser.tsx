import '../styles/styles.css';

interface Converter {
  type: string;
}

interface FilterParams {
  minAge?: number;
  maxAge?: number;
  sex?: string;
  disease?: string;
}

interface Filter {
  params: FilterParams
}

interface DownloadChooserProps {
  converterSelected: Converter;
  fileSelected: File;
  filterSelected: Filter;
}

export default function DownloadChooser({ converterSelected, fileSelected, filterSelected }: DownloadChooserProps) {
  console.log(fileSelected);

  return (
    <div className="download-chooser">
      <div className="stepper-title ">
        Load your file
      </div>
      <div className="stepper-description">
        Converting your model
      </div>
      <div className="stepper-body">
        <div className="stepper-body-description">
          <div className="stepper-body-description-title flex">
            <span className="stepper-body-description-title-label">File name:</span>
            <div className="flex !justify-center !items-center bg-blue-500">
              {fileSelected.name}
            </div>
          </div>
          <div className="stepper-separator"></div>
          <div className="stepper-body-description-title">
            <span>Filter options selected:</span>
            <div className="stepper-body-description-row">
              <span className="stepper-body-description-title-label">Age:</span>
              {filterSelected.params.minAge} - {filterSelected.params.maxAge}
            </div>
            { filterSelected.params.sex && filterSelected.params.sex !== '' &&
              <div className="stepper-body-description-row">
                <span className="stepper-body-description-title-label">Sex:</span>
                {filterSelected.params.sex}
              </div>
            }
            { filterSelected.params.disease && filterSelected.params.disease !== '' &&
              <div className="stepper-body-description-row">
                <span className="stepper-body-description-title-label">Disease:</span>
                {filterSelected.params.disease}
              </div>
            }
          </div>
        </div>
        <div className="stepper-body-info">

        </div>
      </div>
    </div>
  );
}