import { GOOGLE_CALENDER_API_KEY, GOOGLE_CALENDER_ID } from "../../config";

const Calender: React.FC = () => {
  console.log(GOOGLE_CALENDER_API_KEY);
  console.log(GOOGLE_CALENDER_ID);
  return (
    <>
      <iframe
        src={`https://calendar.google.com/calendar/embed?src=${GOOGLE_CALENDER_ID}&ctz=Asia%2FTokyo`}
        width="800"
        height="600"
      ></iframe>
    </>
  );
};

export default Calender;
