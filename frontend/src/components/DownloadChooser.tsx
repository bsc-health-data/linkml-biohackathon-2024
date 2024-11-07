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
  converterOutput: Converter;
}

interface Converter {
  type: string;
}

export default function DownloadChooser({ converterSelected, fileSelected, filterSelected, converterOutput }: DownloadChooserProps) {
  return (
    <div className="download-chooser">
      <div className="stepper-title ">
        Download Resume
      </div>
      <div className="stepper-description">
        There is a quick resume about your download parameters
      </div>
      <div className="stepper-body-block">
        <div className="download-chooser-item">
          <div className="download-chooser-item-title">
            Upload File Name:
          </div>
          <div className="download-chooser-item-value">
            {fileSelected ? fileSelected.name : 'No file selected'}
          </div>
        </div>
        <div className="stepper-separator"></div>
        <div className="download-chooser-item">
          <div className="download-chooser-item-title">
            Converter From:
          </div>
          <div className="download-chooser-item-value">
            {converterSelected.type}
          </div>
        </div>
        <div className="stepper-separator"></div>
        <div className="download-chooser-item">
          <div className="download-chooser-item-title">
            Converter To:
          </div>
          <div className="download-chooser-item-value">
            {converterOutput.type}
          </div>
        </div>
        <div className="stepper-separator"></div>
        <div className="download-chooser-item">
          <div className="download-chooser-item-title">
            Applied Filters:
          </div>
          <div className="download-chooser-item-value">
            Age ranges: {filterSelected.params.minAge} - {filterSelected.params.maxAge}
          </div>
          <hr />
          <div className="download-chooser-item-value">
            Sex: {filterSelected.params.sex }
          </div>
          <hr />
          <div className="download-chooser-item-value">
            Disease: {filterSelected.params.disease }
          </div>
        </div>
      </div>
      <div className="stepper-body-block-footer">
        <button type="button" className="btn btn-primary">Download</button>
      </div>
    </div>
  );
}