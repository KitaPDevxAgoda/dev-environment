import React, { useEffect, useState } from "react"
import EditableLabel from "react-inline-editing"
import "./App.css"
import { deleteMail, fetchMail } from "./api"

function App() {
  const [data, setData] = useState([{ id: 1, subject: "test" }])

  async function fetchData() {
    setData(await fetchMail())
  }

  async function handleUpdate(id, subject) {
    // const response = await updateMail(id, subject);
    const response = ""

    fetchData()
  }

  async function handleDelete(id) {
    await deleteMail(id)
    await fetchData()
  }

  // async function onClickCreate(subject) {
  //   const response = ""

  //   fetchData()
  // }

  useEffect(() => {
    fetchData()
  }, [])

  console.log(data)

  return (
    <div className="App">
      <table className="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Subject</th>
            <th scope="col">Update</th>
            <th scope="col">Delete</th>
          </tr>
        </thead>
        <tbody>
          {data.map(({ id, subject }) => {
            return (
              <tr key={Math.random()}>
                <th scope="row">{id}</th>
                <td>
                  <EditableLabel text={subject} />
                </td>
                <td>
                  <button onClick={() => handleDelete(id)}>Delete</button>
                </td>
              </tr>
            )
          })}
        </tbody>
      </table>
      {/* <button onClick={onClickCreate}>Create</button> */}
    </div>
  )
}

export default App
