import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState([{ id: 1, subject: "test" }]);

  async function fetchData() {
    // const response = await readMail();
    const response = "";
    setData(response);
  }

  async function onClickUpdate(id, subject) {
    // const response = await updateMail(id, subject);
    const response = "";

    fetchData();
  }

  async function onClickDelete(id) {
    // const response = await deleteMail(id);
    const response = "";

    fetchData();
  }

  async function onClickCreate(subject) {
    // const response = await createMail(subject);
    const response = "";

    fetchData();
  }

  useEffect(() => {
    // fetchData();
  }, []);

  console.log(data);

  return (
    <div className="App">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">First</th>
            <th scope="col">Update</th>
            <th scope="col">Delete</th>
          </tr>
        </thead>
        <tbody>
          {data.map((mail) => {
            return (
              <tr>
                <th scope="row">{mail.id}</th>
                <td>{mail.subject}</td>
                <td>
                  <button onClick={onClickUpdate}>Update</button>
                </td>
                <td>
                  <button onClick={onClickDelete}>Delete</button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <button onClick={onClickCreate}>Create</button>
    </div>
  );
}

export default App;
