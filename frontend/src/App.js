import React, { useEffect, useState } from "react"
import EditableLabel from "react-inline-editing"
import "./App.css"
import { deleteMail, fetchMail, updateMail, createMail } from "./api"

function App() {
  const [data, setData] = useState([])

  async function fetchData() {
    setData(await fetchMail())
  }

  async function handleUpdate(subject, id) {
    await updateMail(subject, id)
    await fetchData()
  }

  async function handleDelete(id) {
    await deleteMail(id)
    await fetchData()
  }

  async function handleCreate() {
    var subject = window.prompt("subject", "subject")
    await createMail(subject)
    await fetchData()
  }

  useEffect(async () => {
    await fetchData()
  }, [])

  return (
    <div className="App">
      <table className="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Subject</th>
            <th scope="col">Delete</th>
          </tr>
        </thead>
        <tbody>
          {data.map(({ id, subject }) => {
            return (
              <tr key={Math.random()}>
                <th scope="row">{id}</th>
                <td>
                  <EditableLabel
                    text={subject}
                    onFocusOut={(subject) => handleUpdate(subject, id)}
                  />
                </td>
                <td>
                  <button onClick={() => handleDelete(id)}>Delete</button>
                </td>
              </tr>
            )
          })}
        </tbody>
      </table>
      <button onClick={handleCreate}>Create</button>
    </div>
  )
}

export default App
