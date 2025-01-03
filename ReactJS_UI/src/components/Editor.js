import React, { useState } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { javascript } from "@codemirror/lang-javascript";

const Editor = () => {
  const [code, setCode] = useState("// Start coding!");

  const handleCodeChange = (value) => {
    setCode(value);
  };

  return (
    <div class="container">
      <div
        style={{
          margin: "20px",
          border: "1px solid #ccc",
          borderRadius: "4px",
        }}
      >
        <CodeMirror
          value={code}
          height="540px"
          extensions={[javascript()]}
          onChange={handleCodeChange}
        />
      </div>
    </div>
  );
};

export default Editor;
