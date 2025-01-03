import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
const ChatIO = ({ setResponse }) => {
  const [errorMessage, setErrorMessage] = useState("");
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hi! How can I help you today?" },
  ]);
  const [input, setInput] = useState("");

  // Reference to the chat container
  const chatBodyRef = useRef(null);

  // Scroll to the bottom when messages change
  useEffect(() => {
    if (chatBodyRef.current) {
      chatBodyRef.current.scrollTop = chatBodyRef.current.scrollHeight;
    }
  }, [messages]);

  // Handle input change
  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  // Handle sending message
  const handleSendMessage = async (event) => {
    event.preventDefault();

    if (input.trim() === "") return;
    // Add user message
    const userMessage = { sender: "user", text: input };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    // Clear input field
    setInput("");

    // Generate bot response
    const botMessage = {
      // sender: "bot",
      // text: `Fetching from terminal for.... "${input}". `,
    };

    // Simulate bot response after a short delay
    setTimeout(() => {
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    }, 500);

    if (input.trim() === "") {
      return;
    }

    try {
      let response = await axios.post("http://localhost:5000/reverse", {
        text: input,
      });

      console.log(response.data.reversed);
      const output = response.data.reversed;

      // print the output into the chat
      const botResponseMessage = {
        sender: "bot",
        text: `Reversed Text: "${output}"`,
      };
      setMessages((prevMessages) => [...prevMessages, botResponseMessage]);
    } catch (error) {
      console.error("Error occurred:", error);
      setErrorMessage("Error connecting to the server.");
    }
  };

  return (
    <div className="container">
      <section className="chat">
        <div className="card" id="chat2">
          <div
            className="card-header justify-content-between align-items-center p-3"
            style={{ backgroundColor: "rgb(52, 52, 52)" }}
          >
            <h5 className="mb-0" style={{ color: "rgb(243, 243, 243)" }}>
              Live Chat
            </h5>
          </div>
          <div
            className="card-body"
            ref={chatBodyRef} // Attach reference to chat body
            style={{
              backgroundColor: "rgb(52, 52, 52)",
              position: "relative",
              height: "423px",
              overflow: "auto",
            }}
          >
            {messages.map((message, index) => (
              <div
                key={index}
                className={`d-flex flex-row justify-content-${
                  message.sender === "user" ? "end" : "start"
                } mb-4`}
              >
                <div>
                  <p
                    className="small p-2 rounded-3"
                    style={{
                      backgroundColor:
                        message.sender === "user"
                          ? "rgb(243, 243, 243)"
                          : "rgb(233, 220, 190)",
                      color:
                        message.sender === "user" ? "rgb(52, 52, 52)" : "black",
                    }}
                  >
                    {message.text}
                  </p>
                </div>
              </div>
            ))}
          </div>
          <div
            className="card-footer text-muted d-flex justify-content-start align-items-center p-3"
            style={{ backgroundColor: "rgb(52, 52, 52)" }}
          >
            <input
              type="text"
              className="form-control form-control-lg"
              value={input}
              onChange={handleInputChange}
              placeholder="Type message"
            />
            <button
              className="p-2 rounded-3 bg-light ms-3"
              style={{ width: "80px" }}
              onClick={handleSendMessage}
            >
              Send
            </button>
          </div>
        </div>
      </section>
    </div>
  );
};

export default ChatIO;
