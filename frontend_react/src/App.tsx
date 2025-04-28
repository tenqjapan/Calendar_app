import { BrowserRouter, Routes, Route } from "react-router-dom";
import TopPage from "./pages/topPage/topPage";
import SchedulePage from "./pages/schedulePage/schedulePage";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<TopPage />} />
        <Route path="/schedule" element={<SchedulePage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
