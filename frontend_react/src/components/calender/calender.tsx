interface CalenderProps {
  calenderId: string;
}

const Calender: React.FC<CalenderProps> = ({ calenderId }) => {
  console.log(calenderId);
  return (
    <>
      <iframe
        src={`https://calendar.google.com/calendar/embed?src=${calenderId}&ctz=Asia%2FTokyo`}
        width="800"
        height="600"
      ></iframe>
    </>
  );
};

export default Calender;
