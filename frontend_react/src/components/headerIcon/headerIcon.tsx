import "./headerIcon.css";
import iconImage from "../../assets/icon_test.svg";
const HeaderIcon: React.FC = () => {
  return (
    <div className="header-icon">
      <img src={iconImage} alt="User Icon" className="user-icon" />
    </div>
  );
};

export default HeaderIcon;
