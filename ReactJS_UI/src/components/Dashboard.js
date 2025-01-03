import "../App.css";
import React, { useState } from "react";
import ChatIO from "./chatio";
import Footer from "./footer";
import AiTerminal from "./AiTerminal";
import Navbar from "./SysOpsAI_Navbar";
import { TerminalContextProvider } from "react-terminal";

function Dashboard() {
  const [response, setResponse] = useState(null);
  return (
    <div
      className="main-container "
      style={{ backgroundColor: "rgb(52, 52, 52)" }}
    >
      <Navbar />
      <div className="row">
        <div className="d-flex align-items-start">
          <div className="col">
            <ChatIO setResponse={setResponse} />
          </div>
          <div className="col">
            <TerminalContextProvider>
              <AiTerminal response={response} />
            </TerminalContextProvider>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Dashboard;
