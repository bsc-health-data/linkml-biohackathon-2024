import { useState } from 'react';
import '../styles/styles.css';

interface FileChooserProps {
  onFileChange: (file: File) => void;
}

export default function FileChooser({ onFileChange }: FileChooserProps) {
  const [file, setFile] = useState<File | null>(null);
  const defaultFileName = 'Attachment';

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      console.llg(e.target.files[0]);
      setFile(e.target.files[0]);
      onFileChange(e.target.files[0]);    }
  };

  return(
    <div className="file-chooser">
      <div className="stepper-title ">
        Choose a file to upload
      </div>
      <div className="stepper-description">
        <div className="stepper-description-content">
          Please select the file you would like to convert. Once chosen, the system will guide you through the steps to complete the conversion process. Make sure the file format is supported for smooth processing. After uploading, you'll be able to choose your preferred output format and settings.
          <br/>
          Custom formats supported are: .CSV, .DB, .JSON
        </div>
      </div>
      <div className="stepper-body">
        <label className="uploadFile">
          <i className="fas fa-paperclip fa-md mr-2"></i>
          <span className="filename">
            { file ? file.name : defaultFileName }
            </span>
          <input type="file" className="inputfile form-control" name="file" />
        </label>
      </div>
    </div>
  );
}