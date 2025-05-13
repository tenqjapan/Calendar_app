import Header from "../../components/header/header";
import Calender from "../../components/calender/calender";
import { GOOGLE_CALENDER_ID } from "../../config";

const TopPage: React.FC = () => {
  //ログインしているユーザーが管理者か学生かを判定して、表示するコンポーネントを切り替える
  return (
    <>
      <Header title="トップ" />
      <Calender calenderId={GOOGLE_CALENDER_ID}/>
    </>
  );
};

export default TopPage;
