import CustomStepper  from './components/CustomStepper';
import './App.css'
import predictiveImage from './assets/predictive.png';

function App()  {
  return (
    <>
      <div className="navbar">
      </div>
      <div className="container mx-auto">
        <div className="title-wrapper flex">
          <img src={predictiveImage} alt="logo" className="logo" />
          <div className="title">
            <span className="title-upper">D</span>ata  
            <span className="title-upper">M</span>odel 
            <span className="title-upper">C</span>onverter 
            </div>
        </div>
        <CustomStepper />
      </div>
    </>
  )
}

export default App
