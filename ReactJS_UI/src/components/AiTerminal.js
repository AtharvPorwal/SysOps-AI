import React, { useEffect, useState } from "react";
import { ReactTerminal } from "react-terminal";

const AiTerminal = ({ response }) => {
  // Each key is a command name. The value can be a string or a function returning a string.
  const [terminalOutput, setTerminalOutput] = useState([]);

  useEffect(() => {
    if (response && response.reversed) {
      // Add the latest response to the terminal output
      setTerminalOutput((prevOutput) => [
        ...prevOutput,
        `Server Response: Reversed text: ${response.data}`,
      ]);
    }
  }, [response]);

  const commands = {
    greet: (name = "") => `Hello, ${name}! Nice to meet you.`,
    help: () =>
      "Available commands: greet <name>, clear. Server responses are displayed automatically.",
    clear: () => {
      setTerminalOutput([]);
      return "Terminal cleared!";
    },
  };

  return (
    <div
      style={{
        position: "relative",
        height: "580px",
      }}
    >
      <ReactTerminal
        welcomeMessage="Welcome to the AI Terminal! Type 'help' for available commands."
        commands={commands}
        errorMessage="Command not recognized. Type 'help' for available commands." // fallback for unknown
        prompt=">>"
      />
    </div>
  );
};

export default AiTerminal;
