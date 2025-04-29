import Calender from "../../components/calender/calender";
import Header from "../../components/header/header";
import "./schedulePage.css";

const SchedulePage: React.FC = () => {
  return (
    <>
      <Header title="スケジュール" />
      <div className="calender-container">
        <Calender />
      </div>
    </>
  );
};

export default SchedulePage;
