import "./header.css";
import HeaderIcon from "../headerIcon/headerIcon";

interface HeaderProps {
  title: string;
}

const Header: React.FC<HeaderProps> = ({ title }) => {
  return (
    <div className="header-container">
      <div className="app-title">中山研カレンダー</div>
      <div className="page-title">{title}</div>
      {/* <HeaderIcon /> */}
    </div>
  );
};

export default Header;
