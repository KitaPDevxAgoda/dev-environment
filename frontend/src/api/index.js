import Axios from "axios"
import { HOST } from "../const"

export const fetchMail = async () => {
  const response = await Axios.get(`${HOST}/mail`)
  return response.data
}

export const updateMail = async (subject, id) => {
  const response = await Axios.put(`${HOST}/mail`, { subject, id })
}

export const deleteMail = async (id) => {
  await Axios.post(`${HOST}/deleteMail`, { id })
}

export const createMail = async (subject) => {
  const response = await Axios.post(`${HOST}/mail`, { subject })
}
