import Axios from "axios"
import { HOST } from "../const"

export const fetchMail = async () => {
  const response = await Axios.get(`${HOST}/emails`)
  return response.data
}
// new Promise(async (resolve, reject) => {
// setTimeout(() => resolve([{ id: 1, subject: "tanakorn" }]), 3000)
// })

// export const updateMail = async () =>
// new Promise((resolve, reject) => {
//   setTimeout(resolve([{ id: 1, subject: "tanakorn" }]), 10000)
// })

export const deleteMail = (id) => Axios.delete(`${HOST}/emails/${id}`)

// export const createMail = async () =>
//   new Promise((resolve, reject) => {
//     setTimeout(10000, resolve([{ id: 1, subject: "tanakorn" }]))
//   })
